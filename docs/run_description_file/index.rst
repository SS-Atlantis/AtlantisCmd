.. Copyright 2021, Salish Sea Atlantis project contributors,
.. The University of British Columbia, and CSIRO
..
.. Licensed under the Apache License, Version 2.0 (the "License");
.. you may not use this file except in compliance with the License.
.. You may obtain a copy of the License at
..
..    https://www.apache.org/licenses/LICENSE-2.0
..
.. Unless required by applicable law or agreed to in writing, software
.. distributed under the License is distributed on an "AS IS" BASIS,
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
.. See the License for the specific language governing permissions and
.. limitations under the License.

.. _RunDescriptionFileStructure:

******************************
Run Description File Structure
******************************

:program:`atlantis` run description files are written in YAML_.
They contain key-value pairs that define the names and locations of files and directories that :program:`atlantis` uses to manage runs of the CSIRO Atlantis ecosystem model and their results.

.. _YAML: https://pyyaml.org/wiki/PyYAMLDocumentation

Run description files are typically stored under version control in a sub-directory of your clone of the Atlantis model configuration repository you are using;
e.g. `salish-sea-atlantis-model`_.

.. _salish-sea-atlantis-model: https://bitbucket.csiro.au/users/por07g/repos/salish-sea-atlantis-model/browse

.. toctree::
   :maxdepth: 3

   yaml_file
