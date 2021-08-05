#  Copyright 2021, Salish Sea Atlantis project contributors, The University of British Columbia,
#  and CSIRO.
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
#
"""Shared fixtures for AtlantisCmd unit and integration tests.
"""
import os
import textwrap
from pathlib import Path

import pytest
import yaml

import atlantis_cmd.run


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


@pytest.fixture
def mock_load_run_desc_return(run_desc, monkeypatch):
    def mock_return(*args):
        return run_desc

    monkeypatch.setattr(atlantis_cmd.run.nemo_cmd.prepare, "load_run_desc", mock_return)


@pytest.fixture
def mock_calc_tmp_run_dir_return(run_desc, monkeypatch):
    def mock_return(*args):
        runs_dir = Path(run_desc["paths"]["runs directory"])
        return runs_dir / "SS-Atlantis_2021-08-04T105443-0700"

    monkeypatch.setattr(atlantis_cmd.run, "_calc_tmp_run_dir", mock_return)


@pytest.fixture
def mock_record_vcs_revisions(run_desc, monkeypatch):
    def mock_return(*args):
        pass

    if os.environ.get("GITHUB_ACTIONS") == "true":
        monkeypatch.setattr(atlantis_cmd.run, "_record_vcs_revisions", mock_return)
