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

.. _AtlantisCmdInstallation:

***************************************
:kbd:`AtlantisCmd` Package Installation
***************************************

:kbd:`AtlantisCmd` is a Python package that provides the :program:`atlantis` command-line tool for managing runs of the CSIRO Atlantis ecosystem model.

Installation of :kbd:`AtlantisCmd` is a 3 step process:

#. Clone the `SS-Atlantis/AtlantisCmd`_ and `SalishSeaCast/NEMO-Cmd`_ repositories from GitHub
#. Create the :kbd:`atlantis-cmd` conda environment
#. Install the :kbd:`NEMO-Cmd` and :kbd:`AtlantisCmd` packages in the :kbd:`atlantis-cmd` environment

.. _SS-Atlantis/AtlantisCmd: https://github.com/SS-Atlantis/AtlantisCmd
.. _SalishSeaCast/NEMO-Cmd: https://github.com/SalishSeaCast/NEMO-Cmd

The following sections assume that the base directory for your Atlantis work is :file:`/ocean/$USER/Atlantis/`.

Once you have completed the installation,
please see :ref:`AtlantisCmdSubcommands` for information about how to use the :program:`atlantis` command,
and :ref:`RunDescriptionFileStructure` for information about how to construct the run description YAML files that it uses.


Clone Repositories
==================

The :kbd:`AtlantisCmd` package relies on the `NEMO-Cmd`_ package for some of its functionality.

.. _NEMO-Cmd: https://nemo-cmd.readthedocs.io/en/latest/

Clone the repositories from GitHub with:

.. code-block:: bash

    $ cd /ocean/$USER/Atlantis/
    $ git clone git@github.com:SalishSeaCast/NEMO-Cmd.git
    $ git clone git@github.com:SS-Atlantis/AtlantisCmd.git

.. note::

    The :kbd:`git clone` command above assumes that you are `connecting to GitHub using SSH`_.
    If it fails,
    please follow the instructions in our :ref:`moaddocs:SecureRemoteAccess` docs to set up your SSH keys and :ref:`moaddocs:CopyYourPublicSshKeyToGitHub`.

    .. _connecting to GitHub using SSH: https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh


Create Conda Environment
========================

Create an isolated `Conda`_ environment for :kbd:`AtlantisCmd` to avoid conflicts with other Python packages installed on your system.
Assuming that you have `Miniconda3`_ installed,
you can create and activate an environment called :kbd:`atlantis-cmd` that will have all of the Python packages necessary to use the :program:`atlantis` command that is provided by the :kbd:`AtlantisCmd` package.
The environment will also include additional packages that are used for development,
testing,
and building the package documentation.

.. _Conda: https://conda.io/en/latest/
.. _Miniconda3: https://docs.conda.io/en/latest/miniconda.html

.. code-block:: bash

    $ cd AtlantisCmd
    $ conda env create -f envs/environment-dev.yaml

Whenever you want to use the :program:`atlantis` command you will need to activate the :kbd:`atlantis-cmd` environment with the command:

.. code-block:: bash

    $ conda activate atlantis-cmd

You can tell that the environment is activated because your command-line prompt changes to includes the environment name in parenthesis like:

.. code-block:: bash

    (atlantis-cmd)$

To deactivate the environment use:

.. code-block:: bash

    (atlantis-cmd)$ conda deactivate


Install Packages
================

Activate your :kbd:`atlantis-cmd` environment and install the :kbd:`NEMO-Cmd` and :kbd:`AtlantisCmd` packages in it.
You only need to do this once when you are setting things up.
After that,
activating the :kbd:`atlantis-cmd` environment makes the :program:`atlantis` command available for use.

.. code-block:: bash


    $ cd AtlantisCmd
    $ conda activate atlantis-cmd
    (atlantis-cmd)$ pip install --editable ../NEMO-Cmd
    (atlantis-cmd)$ pip install --editable .

The :kbd:`--editable` option in the :command:`pip install` commands above install the packages from the cloned repos via symlinks so that the installed packages will be automatically updated as their repos evolve.

You can confirm that the :kbd:`AtlantisCmd` package is installed and learn which version it is using with the command:

.. code-block:: bash

    (atlantis-cmd)$ atlantis --version

The output of that command should be something like:

.. code-block:: text

    atlantis 21.1.dev0
