# Copyright 2021, Salish Sea Atlantis project contributors, The University of British Columbia, and CSIRO
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
"""AtlantisCmd - A command-line tool for doing various operations associated with the
Salish Sea Atlantis project version of the CSIRO Atlantis ecosystem model.
AtlantisCmd is based on, and provides Atlantis-specific extensions for
https://github.com/SalishSeaCast/NEMO-Cmd.
"""
import setuptools


setuptools.setup(
    entry_points={
        # The atlantis command:
        "console_scripts": ["atlantis = atlantis_cmd.main:main"],
        # Sub-command plug-ins:
        "atlantis.app": [
            "gather = nemo_cmd.gather:Gather",
            "run = atlantis_cmd.run:Run",
        ],
    }
)
