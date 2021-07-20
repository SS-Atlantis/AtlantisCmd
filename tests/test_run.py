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
