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
"""Functional tests for symlinks and file copies created by cookiecutter
post_gen_project hook script.
"""
from pathlib import Path

import atlantis_cmd.run


class TestPostGenProject:
    """Functional tests for symlinks and file copies created by cookiecutter
    post_gen_project hook script."""

    def test_atlantis_exe_symlink(
        self,
        mock_load_run_desc_return,
        mock_calc_tmp_run_dir_return,
        mock_record_vcs_revisions,
        run_desc,
        tmp_path,
    ):
        results_dir = tmp_path / "results_dir"
        atlantis_cmd.run.run(
            tmp_path / "atlantis.yaml",
            results_dir,
            no_submit=True,
        )
        tmp_run_dir = (
            Path(run_desc["paths"]["runs directory"])
            / "SS-Atlantis_2021-08-04T105443-0700"
        )
        assert (tmp_run_dir / "atlantisMerged").is_symlink()
