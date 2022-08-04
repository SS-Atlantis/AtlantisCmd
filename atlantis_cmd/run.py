#  Copyright 2021 – present by the Salish Sea Atlantis project contributors,
#  The University of British Columbia, and CSIRO.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# SPDX-License-Identifier: Apache-2.0


"""AtlantisCmd command plug-in for run sub-command.

Prepare for, execute, and gather the results of a run of the CSIRO Atlantis ecosystem model.
"""
import logging
import os
import shlex
import subprocess
from pathlib import Path

import arrow
import cliff.command
import cookiecutter.main
import nemo_cmd.prepare

logger = logging.getLogger(__name__)


class Run(cliff.command.Command):
    """Prepare, execute, and gather results from a CSIRO Atlantis ecosystem model run."""

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.description = """
            Prepare, execute, and gather the results from an Atlantis
            run described in DESC_FILE.
            The results files from the run are gathered in RESULTS_DIR.

            If RESULTS_DIR does not exist it will be created.
        """
        parser.add_argument(
            "desc_file",
            metavar="DESC_FILE",
            type=Path,
            help="run description YAML file",
        )
        parser.add_argument(
            "results_dir",
            metavar="RESULTS_DIR",
            type=Path,
            help="directory to store results into",
        )
        parser.add_argument(
            "--no-submit",
            dest="no_submit",
            action="store_true",
            help="""
            Prepare the temporary run directory, and the bash script to
            execute the Atlantis run, but don't launch the run.
            This is useful during development runs when you want to hack on
            the bash script and/or use the same temporary run directory
            more than once.
            """,
        )
        parser.add_argument(
            "-q",
            "--quiet",
            action="store_true",
            help="don't show the run directory path",
        )
        return parser

    def take_action(self, parsed_args):
        """Execute the `atlantis run` sub-command.

        :param parsed_args: Arguments and options parsed from the command-line.
        :type parsed_args: :class:`argparse.Namespace` instance
        """
        launched_job_msg = run(
            parsed_args.desc_file,
            parsed_args.results_dir,
            no_submit=parsed_args.no_submit,
            quiet=parsed_args.quiet,
        )
        if launched_job_msg and not parsed_args.quiet:
            logger.info(launched_job_msg)


def run(desc_file, results_dir, no_submit=False, quiet=False):
    """Create and populate a temporary run directory, and a run script, and launch the run.

    The run script is stored in :file:`Atlantis.sh` in the temporary run directory.
    That script is launched in a subprocess.

    :param desc_file: File path/name of the YAML run description file.
    :type desc_file: :py:class:`pathlib.Path`

    :param results_dir: Path of the directory in which to store the run results;
                        it will be created if it does not exist.
    :type results_dir: :py:class:`pathlib.Path`

    :param boolean no_submit: Prepare the temporary run directory,
                              and the run script to execute the Atlantis run,
                              but don't launch the run.

    :param boolean quiet: Don't show the run directory path message;
                          the default is to show the temporary run directory
                          path.

    :returns: Message confirming launch of the run script.
    :rtype: str
    """
    run_desc = nemo_cmd.prepare.load_run_desc(desc_file)
    run_id = nemo_cmd.prepare.get_run_desc_value(run_desc, ("run id",))
    runs_dir = nemo_cmd.prepare.get_run_desc_value(
        run_desc, ("paths", "runs directory"), resolve_path=True
    )
    tmp_run_dir = _calc_tmp_run_dir(runs_dir, run_id)
    cookiecutter_context = _calc_cookiecutter_context(
        run_desc, run_id, desc_file, tmp_run_dir, results_dir
    )
    # Symlinks and copied files in temporary run directory are created by
    # cookiecutter/hooks/post_gen_project.py script
    cookiecutter.main.cookiecutter(
        os.fspath(Path(__file__).parent.parent / "cookiecutter"),
        no_input=True,
        output_dir=runs_dir,
        extra_context=cookiecutter_context,
    )
    run_script_file = tmp_run_dir / "Atlantis.sh"
    _record_vcs_revisions(run_desc, tmp_run_dir)
    if not quiet:
        logger.info(f"Created temporary run directory: {tmp_run_dir}")
    if no_submit:
        return
    launch_cmd = f"{run_script_file}"
    subprocess.Popen(shlex.split(launch_cmd))
    return f"launched {run_id} run via {run_script_file}"


def _calc_tmp_run_dir(runs_dir, run_id):
    """Compose a uniquely named temporary run directory name from the run id and a date/time stamp.

    :param runs_dir: Path of the directory in which to create the temporary run directory.
    :type runs_dir: :py:class:`pathlib.Path`

    :param str run_id: Run identifier.

    :return: Temporary run directory path.
    :rtype: :py:class:`pathlib.Path`
    """
    tmp_run_dir_timestamp = arrow.now().format("YYYY-MM-DDTHHmmss.SSSSSSZ")
    tmp_run_dir = runs_dir / f"{run_id}_{tmp_run_dir_timestamp}"
    return tmp_run_dir


def _calc_cookiecutter_context(run_desc, run_id, desc_file, tmp_run_dir, results_dir):
    """Calculate the cookiecutter context for creation of the temporary run directory.

    :param dict run_desc: Run description dictionary.

    :param str run_id: Run identifier.

    :param desc_file: File path/name of the YAML run description file.
    :type desc_file: :py:class:`pathlib.Path`

    :param tmp_run_dir: Temporary run directory path.
    :type tmp_run_dir: :py:class:`pathlib.Path`

    :param results_dir: Path of the directory in which to store the run results.
    :type results_dir: :py:class:`pathlib.Path`

    :return: Cookiecutter context for creation of the temporary run directory.
    :rtype: dict
    """
    atlantis_repo = nemo_cmd.prepare.get_run_desc_value(
        run_desc, ("paths", "atlantis code"), resolve_path=True, run_dir=tmp_run_dir
    )
    # Build parameters and forcing dicts item-by-item instead of via dict comprehensions
    # so that we can fail fast if any of the files do not exist
    params_dict = nemo_cmd.prepare.get_run_desc_value(run_desc, ("parameters",))
    parameters = {}
    for key, path in params_dict.items():
        parameters[key] = nemo_cmd.prepare.get_run_desc_value(
            run_desc, ("parameters", key), resolve_path=True, run_dir=tmp_run_dir
        )
    forcing_dict = nemo_cmd.prepare.get_run_desc_value(run_desc, ("forcing",))
    forcing = {}
    for key, path in forcing_dict.items():
        forcing[key] = nemo_cmd.prepare.get_run_desc_value(
            run_desc,
            ("forcing", key, "link to"),
            resolve_path=True,
            run_dir=tmp_run_dir,
        )
    atlantis_executable_name = nemo_cmd.prepare.get_run_desc_value(
        run_desc, ("paths", "atlantis executable name")
    )
    atlantis_executable = atlantis_repo.joinpath(
        "atlantis", "atlantismain", atlantis_executable_name
    )
    if not atlantis_executable.exists():
        logger.error(f"{atlantis_executable} not found - did you forget to build it?")
        nemo_cmd.prepare.remove_run_dir(tmp_run_dir)
        raise SystemExit(2)
    cookiecutter_context = {
        "run_id": run_id,
        "run_desc_yaml": _resolve_path(desc_file),
        "tmp_run_dir": tmp_run_dir,
        "results_dir": _resolve_path(results_dir),
        "atlantis_executable": atlantis_executable,
        "atlantis_executable_name": atlantis_executable_name,
        "atlantis_cmd": nemo_cmd.prepare.get_run_desc_value(
            run_desc,
            ("paths", "atlantis command"),
            resolve_path=True,
            run_dir=tmp_run_dir,
        ),
        "boxes": nemo_cmd.prepare.get_run_desc_value(
            run_desc, ("boxes",), resolve_path=True, run_dir=tmp_run_dir
        ),
        "init_conditions": nemo_cmd.prepare.get_run_desc_value(
            run_desc, ("initial conditions",), resolve_path=True, run_dir=tmp_run_dir
        ),
        "groups": nemo_cmd.prepare.get_run_desc_value(
            run_desc, ("groups",), resolve_path=True, run_dir=tmp_run_dir
        ),
        "migrations": nemo_cmd.prepare.get_run_desc_value(
            run_desc, ("migrations",), resolve_path=True, run_dir=tmp_run_dir
        ),
        "fisheries": nemo_cmd.prepare.get_run_desc_value(
            run_desc, ("fisheries",), resolve_path=True, run_dir=tmp_run_dir
        ),
        "parameters": parameters,
        "output_filename_base": nemo_cmd.prepare.get_run_desc_value(
            run_desc, ("output filename base",)
        ),
        "forcing": forcing,
    }
    return cookiecutter_context


def _resolve_path(path):
    """Expand environment variables and :file:`~` in :kbd:`path` and resolve it to an absolute path.

    :param path: Path of the directory/file to resolve.
    :type path: :py:class:`pathlib.Path`

    :return: :py:class:`pathlib.Path`
    """
    path = Path(os.path.expandvars(path)).expanduser().resolve()
    return path


def _record_vcs_revisions(run_desc, tmp_run_dir):
    """Record revision and status information from version control system
    repositories in files in the temporary run directory.

    :param dict run_desc: Run description dictionary.

    :param tmp_run_dir: Path of the temporary run directory.
    :type tmp_run_dir: :py:class:`pathlib.Path`
    """
    if "vcs revisions" not in run_desc:
        return
    vcs_funcs = {
        "git": nemo_cmd.prepare.get_git_revision,
        "hg": nemo_cmd.prepare.get_hg_revision,
    }
    vcs_tools = nemo_cmd.prepare.get_run_desc_value(
        run_desc, ("vcs revisions",), run_dir=tmp_run_dir
    )
    for vcs_tool in vcs_tools:
        repos = nemo_cmd.prepare.get_run_desc_value(
            run_desc, ("vcs revisions", vcs_tool), run_dir=tmp_run_dir
        )
        for repo in repos:
            nemo_cmd.prepare.write_repo_rev_file(
                Path(repo), tmp_run_dir, vcs_funcs[vcs_tool]
            )
