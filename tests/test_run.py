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
import yaml

import atlantis_cmd.main
import atlantis_cmd.run


@pytest.fixture
def run_cmd():
    return atlantis_cmd.run.Run(atlantis_cmd.main.AtlantisCmdApp, [])


@pytest.fixture()
def run_desc(tmp_path):
    atlantis_code_dir = tmp_path / "atlantis-trunk"
    atlantis_code_dir.mkdir()
    runs_dir = tmp_path / "runs_dir"
    runs_dir.mkdir()
    atlantis_cmd = tmp_path / "atlantis"
    atlantis_cmd.write_text("")
    model_config = tmp_path / "salish-sea-atlantis-model"
    model_config.mkdir()
    init_conditions = model_config / "SS_init.nc"
    init_conditions.write_bytes(b"")
    groups_csv = model_config / "SS_grps.csv"
    groups_csv.write_text("")
    run_params = model_config / "SS_run.prm"
    run_params.write_text("")
    forcing_params = model_config / "SS_forcing.prm"
    forcing_params.write_text("")
    physics_params = model_config / "SS_physics.prm"
    physics_params.write_text("")
    biology_params = model_config / "SS_biology.prm"
    biology_params.write_text("")
    atlantis_cmd_repo = Path(__file__).parent.parent

    atlantis_yaml = tmp_path / "wwatch3.yaml"
    atlantis_yaml.write_text(
        textwrap.dedent(
            f"""\
            run id: SS-Atlantis

            paths:
              atlantis code: {atlantis_code_dir}
              runs directory: {runs_dir}
              atlantis command: {atlantis_cmd}

            initial conditions: {init_conditions}

            parameters:
              run: {run_params}
              groups: {groups_csv}
              forcing: {forcing_params}
              physics: {physics_params}
              biology: {biology_params}

            output filename base: outputSalishSea

            vcs revisions:
              git:
                - {atlantis_cmd_repo}
            """
        )
    )
    with atlantis_yaml.open("rt") as f:
        run_desc = yaml.safe_load(f)
    return run_desc


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

    @staticmethod
    @pytest.fixture
    def mock_load_run_desc_return(run_desc, monkeypatch):
        def mock_return(*args):
            return run_desc

        monkeypatch.setattr(
            atlantis_cmd.run.nemo_cmd.prepare, "load_run_desc", mock_return
        )

    @staticmethod
    @pytest.fixture
    def mock_calc_tmp_run_dir_return(run_desc, monkeypatch):
        def mock_return(*args):
            runs_dir = Path(run_desc["paths"]["runs directory"])
            return runs_dir / "SS-Atlantis_2021-08-04T105443-0700"

        monkeypatch.setattr(atlantis_cmd.run, "_calc_tmp_run_dir", mock_return)

    def test_no_submit(
        self,
        mock_load_run_desc_return,
        mock_calc_tmp_run_dir_return,
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
        assert len(context) == 13

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

    def test_atlantis_code(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["atlantis_code"] == Path(run_desc["paths"]["atlantis code"])

    def test_atlantis_cmd(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["atlantis_cmd"] == Path(run_desc["paths"]["atlantis command"])

    def test_init_conditions(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["init_conditions"] == Path(run_desc["initial conditions"])

    def test_groups_csv(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["groups"] == Path(run_desc["parameters"]["groups"])

    def test_run_params(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["run_params"] == Path(run_desc["parameters"]["run"])

    def test_forcing_params(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["forcing_params"] == Path(run_desc["parameters"]["forcing"])

    def test_physics_params(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["physics_params"] == Path(run_desc["parameters"]["physics"])

    def test_biology_params(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["biology_params"] == Path(run_desc["parameters"]["biology"])

    def test_output_filename_base(self, run_desc, args):
        context = atlantis_cmd.run._calc_cookiecutter_context(
            run_desc, args.run_id, args.desc_file, args.tmp_run_dir, args.results_dir
        )
        assert context["output_filename_base"] == run_desc["output filename base"]


@pytest.mark.skipif(
    os.environ.get("GITHUB_ACTIONS"), reason="Doesn't work in GitHub Actions workflow"
)
class TestRecordVCSRevisions:
    """Unit tests for `atlantis run` _record_vcs_revisions() function."""

    def test_record_vcs_revisions(self, run_desc):
        tmp_run_dir = Path(run_desc["paths"]["runs directory"], "tmp_run_dir")
        tmp_run_dir.mkdir()
        atlantis_cmd.run._record_vcs_revisions(run_desc, tmp_run_dir)
        assert (tmp_run_dir / "AtlantisCmd_rev.txt").exists()
