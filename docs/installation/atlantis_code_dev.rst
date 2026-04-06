.. Copyright 2021 – present by the Salish Sea Atlantis project contributors,
.. The University of British Columbia, and CSIRO.
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

.. SPDX-License-Identifier: Apache-2.0


.. _AtlantisCodeDevEnv:

*************************************
Atlantis Code Development Environment
*************************************

The :py:obj:`AtlantisCmd` package includes an environment called ``atlantis-code`` for doing
development and debugging of the Atlantis code,
as well as analysis of model run results using R via the CSIRO Shiny apps and Python using Jupyter Lab.

These instructions assume that you have installed the Pixi_ package and environments manager
(`installation instructions`_),
and that you have already set up the Atlantis command processor package
(:ref:`AtlantisCmdInstallation`).

  .. _Pixi: https://pixi.prefix.dev/latest/
  .. _`installation instructions`: https://pixi.prefix.dev/latest/installation/

Use Pixi to create the isolated ``atlantis-code`` environment to avoid conflicts the
:py:obj:`AtlantisCmd` environment or with other Python packages installed on your system.

.. code-block:: bash

    $ cd AtlantisCmd
    $ pixi install -e atlantis-code

You can then run commands that use the ``atlantis-code`` environment by prefixing them with
:command:`pixi run -m /ocean/$USER/Atlantis/AtlantisCmd -e atlantis-code`.
Alternatively,
you can launch a sub-shell in the ``atlantis-code`` environment with
:command:`pixi shell -e atlantis-code`.
In the sub-shell,
you can use commands without the :command:`pixi run ...` prefix.
That can be convenient when you are working in the edit-make-run-evaluate cycle.
Use :command:`exit` to end the sub-shell.
