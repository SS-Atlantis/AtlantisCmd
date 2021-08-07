# Copyright 2021, Salish Sea Atlantis project contributors, The University of British Columbia,
# and CSIRO.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""AtlantisCmd run sub-command plug-in unit and integration tests.
"""
import logging
import os
import textwrap
from pathlib import Path
from types import SimpleNamespace

import pytest

import atlantis_cmd.main
import atlantis_cmd.run


@pytest.fixture
def run_cmd():
    return atlantis_cmd.run.Run(atlantis_cmd.main.AtlantisCmdApp, [])


class TestParser:
    """Unit tests for `atlantis run` sub-command command-line parser."""

    def test_get_parser(self, run_cmd):
        parser = run_cmd.get_parser("atlantis run")
        assert parser.prog == "atlantis run"

    def test_cmd_description(self, run_cmd):
        parser = run_cmd.get_parser("atlantis run")
        assert parser.description.strip().startswith(
            "Prepare, execute, and gather the results from an Atlantis"
        )

    def test_desc_file_argument(self, run_cmd):
        parser = run_cmd.get_parser("atlatnis run")
        assert parser._actions[1].dest == "desc_file"
        assert parser._actions[1].metavar == "DESC_FILE"
        assert parser._actions[1].type == Path
        assert parser._actions[1].help

    def test_results_dir_argument(self, run_cmd):
        parser = run_cmd.get_parser("atlantis run")
        assert parser._actions[2].dest == "results_dir"
        assert parser._actions[2].metavar == "RESULTS_DIR"
        assert parser._actions[2].type == Path
        assert parser._actions[2].help

    def test_no_submit_option(self, run_cmd):
        parser = run_cmd.get_parser("atlantis run")
        assert parser._actions[3].dest == "no_submit"
        assert parser._actions[3].option_strings == ["--no-submit"]
        assert parser._actions[3].const is True
        assert parser._actions[3].default is False
        assert parser._actions[3].help

    def test_quiet_option(self, run_cmd):
        parser = run_cmd.get_parser("atlantis run")
        assert parser._actions[4].dest == "quiet"
        assert parser._actions[4].option_strings == ["-q", "--quiet"]
        assert parser._actions[4].const is True
        assert parser._actions[4].default is False
        assert parser._actions[4].help

    def test_parsed_args_defaults(self, run_cmd):
        parser = run_cmd.get_parser("atlantis run")
        parsed_args = parser.parse_args(["foo.yaml", "results/foo/"])
        assert parsed_args.desc_file == Path("foo.yaml")
        assert parsed_args.results_dir == Path("results/foo/")
        assert not parsed_args.no_submit
        assert not parsed_args.quiet

    @pytest.mark.parametrize("flag", ["-q", "--quiet"])
    def test_parsed_args_quiet_options(self, flag, run_cmd):
        parser = run_cmd.get_parser("atlantis run")
        parsed_args = parser.parse_args(["foo.yaml", "results/foo/", flag])
        assert parsed_args.quiet is True

    def test_parsed_args_no_submit_option(self, run_cmd):
        parser = run_cmd.get_parser("atlantis run")
        parsed_args = parser.parse_args(["foo.yaml", "results/foo/", "--no-submit"])
        assert parsed_args.no_submit is True


class TestTakeAction:
    """Unit tests for `atlantis run` sub-command take_action() method."""

    @staticmethod
    @pytest.fixture
    def mock_run_submit_return(monkeypatch):
        def mock_run_return(*args, **kwargs):
            return "launched job msg"

        monkeypatch.setattr(atlantis_cmd.run, "run", mock_run_return)

    def test_take_action(self, mock_run_submit_return, run_cmd, caplog):
        parsed_args = SimpleNamespace(
            desc_file=Path("desc file"),
            results_dir=Path("results dir"),
            no_submit=False,
            quiet=False,
        )
        caplog.set_level(logging.INFO)

        run_cmd.take_action(parsed_args)

        assert caplog.messages[0] == "launched job msg"

    def test_take_action_quiet(self, mock_run_submit_return, run_cmd, caplog):
        parsed_args = SimpleNamespace(
            desc_file=Path("desc file"),
            results_dir=Path("results dir"),
            no_submit=False,
            quiet=True,
        )
        caplog.set_level(logging.INFO)

        run_cmd.take_action(parsed_args)

        assert not caplog.messages

    def test_take_action_no_submit(self, run_cmd, caplog, monkeypatch):
        def mock_run_no_submit_return(*args, **kwargs):
            return None

        parsed_args = SimpleNamespace(
            desc_file=Path("desc file"),
            results_dir=Path("results dir"),
            no_submit=True,
            quiet=False,
        )
        monkeypatch.setattr(atlantis_cmd.run, "run", mock_run_no_submit_return)
        caplog.set_level(logging.INFO)

        run_cmd.take_action(parsed_args)

        assert not caplog.messages


class TestRun:
    """Unit tests for `atlantis run` run() function."""

    def test_no_submit(
        self,
        mock_load_run_desc_return,
        mock_calc_tmp_run_dir_return,
        mock_record_vcs_revisions,
        tmp_path,
    ):
        results_dir = tmp_path / "results_dir"
        launch_job_msg = atlantis_cmd.run.run(
            tmp_path / "atlantis.yaml",
            results_dir,
            no_submit=True,
        )
        assert launch_job_msg is None

    def test_submit(
        self,
        mock_load_run_desc_return,
        mock_calc_tmp_run_dir_return,
        mock_record_vcs_revisions,
        run_desc,
        tmp_path,
    ):
        results_dir = tmp_path / "results_dir"
        launch_job_msg = atlantis_cmd.run.run(
            tmp_path / "atlantis.yaml",
            results_dir,
        )
        run_id = run_desc["run id"]
        runs_dir = Path(run_desc["paths"]["runs directory"])
        expected = (
            f"launched {run_id} run via "
            f"{runs_dir}/SS-Atlantis_2021-08-04T105443-0700/Atlantis.sh"
        )
        assert launch_job_msg == expected


class TestCalcCookiecutterContext:
    """Unit tests for `atlantis run` _calc_cookiecutter_context() function."""

    @staticmethod
    @pytest.fixture
    def args():
        return SimpleNamespace(
            run_id="SS-Atlantis",
            desc_file=Path(
                "/ocean/dlatorne/Atlantis/salish-sea-atlantis-model/atlantis.yaml"
            ),
            tmp_run_dir=Path(
                "/ocean/dlatorne/Atlantis/runs/SS-Atlantis_20210722T165443.123456+0700"
            ),
            results_dir=Path("/ocean/dlatorne/Atlantis/runs/SS-Atlantis-test/"),
        )

    def test_len_context(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert len(context) == 12

    def test_run_id(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["run_id"] == args.run_id

    def test_run_desc_yaml(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["run_desc_yaml"] == args.desc_file

    def test_tmp_run_dir(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["tmp_run_dir"] == args.tmp_run_dir

    def test_results_dir(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["results_dir"] == args.results_dir

    def test_atlantis_executable(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        expected = Path(run_desc["paths"]["atlantis code"]).joinpath(
            "atlantis", "atlantismain", "atlantisMerged"
        )
        assert context["atlantis_executable"] == expected

    def test_atlantis_cmd(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["atlantis_cmd"] == Path(run_desc["paths"]["atlantis command"])

    def test_boxes(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["boxes"] == Path(run_desc["boxes"])

    def test_init_conditions(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["init_conditions"] == Path(run_desc["initial conditions"])

    def test_groups_csv(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["groups"] == Path(run_desc["groups"])

    def test_len_params(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert len(context["parameters"]) == 4

    def test_run_params(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["parameters"]["run"] == Path(run_desc["parameters"]["run"])

    def test_len_forcing(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert len(context["forcing"]) == 3

    def test_forcing_params(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["parameters"]["forcing"] == Path(
            run_desc["parameters"]["forcing"]
        )

    def test_physics_params(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["parameters"]["physics"] == Path(
            run_desc["parameters"]["physics"]
        )

    def test_biology_params(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["parameters"]["biology"] == Path(
            run_desc["parameters"]["biology"]
        )

    def test_hydro_forcing(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["forcing"]["SS_hydro.nc"] == Path(
            run_desc["forcing"]["SS_hydro.nc"]["link to"]
        )

    def test_temperature_forcing(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["forcing"]["SS_temp.nc"] == Path(
            run_desc["forcing"]["SS_temp.nc"]["link to"]
        )

    def test_salinity_forcing(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["forcing"]["SS_salt.nc"] == Path(
            run_desc["forcing"]["SS_salt.nc"]["link to"]
        )

    def test_output_filename_base(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["output_filename_base"] == run_desc["output filename base"]


@pytest.mark.skipif(
    os.environ.get("GITHUB_ACTIONS") == "true",
    reason="Doesn't work in GitHub Actions workflow",
)
class TestRecordVCSRevisions:
    """Unit tests for `atlantis run` _record_vcs_revisions() function."""

    def test_record_vcs_revisions(self, run_desc):
        tmp_run_dir = Path(run_desc["paths"]["runs directory"], "tmp_run_dir")
        tmp_run_dir.mkdir()
        atlantis_cmd.run._record_vcs_revisions(run_desc, tmp_run_dir)
        assert (tmp_run_dir / "AtlantisCmd_rev.txt").exists()


class TestAtlantisBashScript:
    """Unit test for contents of Atlantis.sh generated by cookiecutter."""

    def test_atlantis_sh(
        self,
        mock_load_run_desc_return,
        mock_calc_tmp_run_dir_return,
        mock_record_vcs_revisions,
        run_desc,
        tmp_path,
    ):
        results_dir = tmp_path / "results_dir"
        run_desc_yaml = tmp_path / "atlantis.yaml"
        atlantis_cmd.run.run(run_desc_yaml, results_dir, no_submit=True)
        tmp_run_dir = (
            Path(run_desc["paths"]["runs directory"])
            / "SS-Atlantis_2021-08-04T105443-0700"
        )
        expected = textwrap.dedent(
            f"""\
            #!/bin/bash

            set -e  # abort on first error
            set -u  # abort if undefined variable is encountered

            RUN_ID="{run_desc['run id']}"
            RUN_DESC="{run_desc_yaml}"
            WORK_DIR="{tmp_run_dir}"
            RESULTS_DIR="{results_dir}"
            GATHER="{run_desc["paths"]["atlantis command"]} gather"

            mkdir -p ${{RESULTS_DIR}}

            cd ${{WORK_DIR}}
            echo "working dir: $(pwd)" >${{RESULTS_DIR}}/stdout

            echo "Starting run at $(date)" >>${{RESULTS_DIR}}/stdout
            ./atlantisMerged -i init_conditions.nc 0 -o {run_desc["output filename base"]}.nc \\
              -r run.prm -f forcing.prm -p physics.prm -b biology.prm -s groups.csv \\
              -d ${{RESULTS_DIR}} &>>${{RESULTS_DIR}}/stdout
            ATLANTIS_EXIT_CODE=$?
            echo "Ended run at $(date)" >>${{RESULTS_DIR}}/stdout

            echo "Results gathering started at $(date)" >>${{RESULTS_DIR}}/stdout
            ${{GATHER}} ${{RESULTS_DIR}} --debug &>>${{RESULTS_DIR}}/stdout
            echo "Results gathering ended at $(date)" >>${{RESULTS_DIR}}/stdout

            chmod -v go+rx ${{RESULTS_DIR}} &>>${{RESULTS_DIR}}/stdout
            chmod -v g+rw ${{RESULTS_DIR}}/* &>>${{RESULTS_DIR}}/stdout
            chmod -v o+r ${{RESULTS_DIR}}/* &>>${{RESULTS_DIR}}/stdout

            echo "Deleting run directory" >>${{RESULTS_DIR}}/stdout
            rmdir -v $(pwd) &>>${{RESULTS_DIR}}/stdout
            echo "Finished at $(date)" >>${{RESULTS_DIR}}/stdout
            exit ${{ATLANTIS_EXIT_CODE}}
            """
        )
        tmp_run_dir_lines = [
            line.strip()
            for line in (tmp_run_dir / "Atlantis.sh").read_text().splitlines()
        ]
        assert tmp_run_dir_lines == [line.strip() for line in expected.splitlines()]
