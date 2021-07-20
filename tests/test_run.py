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
import pytest

import atlantis_cmd.main
import atlantis_cmd.run


@pytest.fixture
def run_cmd():
    return atlantis_cmd.run.Run(atlantis_cmd.main.AtlantisCmdApp, [])


class TestParser:
    """Unit tests for `atlantis run` sub-command command-line parser.
    """

    def test_get_parser(self, run_cmd):
        parser = run_cmd.get_parser("atlantis run")
        assert parser.prog == "atlantis run"
