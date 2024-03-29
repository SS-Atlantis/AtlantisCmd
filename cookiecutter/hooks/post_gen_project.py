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


"""Post-rendering script to set up symlinks and copied files in temporary run directory
for a run of the CSIRO Atlantis ecosystem model.
"""
import json
import shutil
from pathlib import Path


shutil.copy2(Path("{{ cookiecutter.run_desc_yaml }}"), Path.cwd())

Path("{{ cookiecutter.atlantis_executable_name }}").symlink_to(
    Path("{{ cookiecutter.atlantis_executable }}")
)

shutil.copy2(Path("{{ cookiecutter.boxes }}"), Path.cwd())

shutil.copy2(Path("{{ cookiecutter.init_conditions }}"), "init_conditions.nc")

shutil.copy2(Path("{{ cookiecutter.groups }}"), "groups.csv")

shutil.copy2(Path("{{ cookiecutter.migrations }}"), "migrations.csv")

shutil.copy2(Path("{{ cookiecutter.fisheries }}"), "fisheries.csv")

# Deserializing the parameters and forcing dicts from cookiecutter.json is a bit hacky,
# especially because of the necessary single-quote to double-quote substitution.
parameters = "{{ cookiecutter.parameters }}"
parameters = json.loads(parameters.replace("'", '"'))
for key, path in parameters.items():
    shutil.copy2(Path(path), f"{key}.prm")

forcing = "{{ cookiecutter.forcing }}"
forcing = json.loads(forcing.replace("'", '"'))
for link_name, target in forcing.items():
    Path(link_name).symlink_to(Path(target))
