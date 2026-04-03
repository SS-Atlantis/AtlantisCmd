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


.. _AtlantisCmdInstallation:

******************************************
:py:obj:`AtlantisCmd` Package Installation
******************************************

:py:obj:`AtlantisCmd` is a Python package that provides the :program:`atlantis` command-line tool
for managing runs of the CSIRO Atlantis ecosystem model.
It is an extension of the `SalishSeaCast/NEMO-Cmd`_ package customized for working with
the Atlantis ecosystem model.

.. _SalishSeaCast/NEMO-Cmd: https://github.com/SalishSeaCast/NEMO-Cmd

These instructions assume that you have installed the Pixi_ package and environments manager
(`installation instructions`_).

  .. _Pixi: https://pixi.prefix.dev/latest/
  .. _`installation instructions`: https://pixi.prefix.dev/latest/installation/

Installation of :py:obj:`AtlantisCmd` is a 2 step process:

#. Clone the `SS-Atlantis/AtlantisCmd`_ repository from GitHub
#. Use Pixi to install Python and the packages needed to run :py:obj:`AtlantisCmd`

.. _SS-Atlantis/AtlantisCmd: https://github.com/SS-Atlantis/AtlantisCmd

The following sections assume that the base directory for your Atlantis work is :file:`/ocean/$USER/Atlantis/`.

Once you have completed the installation,
please see :ref:`AtlantisCmdSubcommands` for information about how to use the :program:`atlantis` command,
and :ref:`RunDescriptionFileStructure` for information about how to construct the run description YAML files that it uses.

For doing development,
testing,
and documentation of the :py:obj:`AtlantisCmd` package,
please see the :ref:`AtlantisCmdPackagedDevelopment` section.


Clone Repository
================

Clone the repository from GitHub with:

.. code-block:: bash

    $ cd /ocean/$USER/Atlantis/
    $ git clone git@github.com:SS-Atlantis/AtlantisCmd.git

.. note::

    The :kbd:`git clone` command above assumes that you are `connecting to GitHub using SSH`_.
    If it fails,
    please follow the instructions in our :ref:`moaddocs:SecureRemoteAccess` docs to set up
    your SSH keys and :ref:`moaddocs:CopyYourPublicSshKeyToGitHub`.

    .. _connecting to GitHub using SSH: https://docs.github.com/en/authentication/connecting-to-github-with-ssh


Install Python and Dependency Packages
======================================

Use Pixi to create an isolated environment for :py:obj:`AtlantisCmd` to avoid conflicts with other Python packages installed on your system.
That environment will have all of the Python packages necessary to use the :program:`atlantis` command that is provided by the :py:obj:`AtlantisCmd` package.

.. code-block:: bash

    $ cd AtlantisCmd
    $ pixi install

When you are in the :file:`AtlantisCmd/` directory
(or a sub-directory)
you can run the :program:`atlantis` command with with the :command:`pixi run` command.
Example:

.. code-block:: bash

    $ pixi run atlantis help

A common use-case is to execute the :command:`atlantis run` command in the directory containing your run description YAML file.
To accomplish that,
we have to tell Pixi where to find the :file:`AtlantisCmd/` directory so that it can use the correct environment.
We do that by using the ``-m`` or ``--manifest`` option of :command:`pixi run`.
Example:

.. code-block:: bash

    $ cd /ocean/$USER/Atlantis/SSAM_Runs/
    $ pixi run -m /ocean/$USER/Atlantis/AtlantisCmd salishsea run atlantis_highres_d0.yaml \
        /ocean/$USER/Atlantis/highres-d0_5b_2019-01-20_depth_PC/
