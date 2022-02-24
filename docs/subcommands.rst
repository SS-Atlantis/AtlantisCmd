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


.. _AtlantisCmdSubcommands:

*********************************
:command:`atlantis` Sub-Commands
*********************************

The command :kbd:`atlantis help` produces a list of the available :program:`atlantis` options and sub-commands:

.. code-block:: text

    usage: atlantis [--version] [-v | -q] [--log-file LOG_FILE] [-h] [--debug]

    Atlantis Ecosystem Model Command Processor

    optional arguments:
    --version            show program's version number and exit
    -v, --verbose        Increase verbosity of output. Can be repeated.
    -q, --quiet          Suppress output except warnings and errors.
    --log-file LOG_FILE  Specify a file to log output. Disabled by default.
    -h, --help           Show help message and exit.
    --debug              Show tracebacks on errors.

    Commands:
    complete       print bash completion command (cliff)
    help           print detailed help for another command (cliff)
    run            Prepare, execute, and gather results from a CSIRO Atlantis ecosystem model run.

For details of the arguments and options for a sub-command use
:command:`atlantis help <sub-command>`.
For example:

.. code-block:: bash

    $ atlantis help run

.. code-block:: text

    usage: atlantis run [-h] [--no-submit] [-q] DESC_FILE RESULTS_DIR

    Prepare, execute, and gather the results from an Atlantis run described in DESC_FILE.
    The results files from the run are gathered in RESULTS_DIR.
    If RESULTS_DIR does not exist it will be created.

    positional arguments:
    DESC_FILE    run description YAML file
    RESULTS_DIR  directory to store results into

    optional arguments:
    -h, --help   show this help message and exit
    --no-submit  Prepare the temporary run directory, and the bash script to
                execute the Atlantis run, but don't launch the run.
                This is useful during development runs when you want to hack on
                the bash script and/or use the same temporary run directory
                more than once.
    -q, --quiet  don't show the run directory path

You can check what version of :program:`atlantis` you have installed with:

.. code-block:: bash

    atlantis --version


.. _atlantis-run:

:kbd:`run` Sub-command
======================

The :command:`run` sub-command prepares,
executes,
and gathers the results from the CSIRO Atlantis ecosystem model run described in the specified run description file.
The results are gathered in the specified results directory.

.. code-block:: text


    usage: atlantis run [-h] [--no-submit] [-q] DESC_FILE RESULTS_DIR

    Prepare, execute, and gather the results from an Atlantis run described in DESC_FILE.
    The results files from the run are gathered in RESULTS_DIR.
    If RESULTS_DIR does not exist it will be created.

    positional arguments:
    DESC_FILE    run description YAML file
    RESULTS_DIR  directory to store results into

    optional arguments:
    -h, --help   show this help message and exit
    --no-submit  Prepare the temporary run directory, and the bash script to
                execute the Atlantis run, but don't launch the run.
                This is useful during development runs when you want to hack on
                the bash script and/or use the same temporary run directory
                more than once.
    -q, --quiet  don't show the run directory path

The path to the run directory,
and a message indicating that the run has been launched are printed upon completion of the command.

The :command:`run` sub-command does the following:

#. Uses a `cookiecutter`_ template in the AtlantisCmd package to set up a temporary run directory from which to execute the Atlantis run.

   .. _cookiecutter: https://cookiecutter.readthedocs.io/en/latest/

#. The `cookiecutter`_ processing generates an :file:`Atlantis.sh` job script in the run directory.
   The job script:

   * runs :program:`atlantisMerged`
   * executes the :ref:`atlantis-gather` to collect the run configuration and results files into the results directory

#. Launches job script as a background job.

See the :ref:`RunDescriptionFileStructure` section for details of the run description YAML file.

The :command:`run` sub-command concludes by printing the path to the run directory and a message indicating that the run has been launched.
Example:

.. code-block:: bash

    $ atlantis run atlantis.yaml /ocean/$USER/Atlantis/runs/my-run/

.. code-block:: text

    atlantis_cmd.run INFO: Created temporary run directory: /ocean/$USER/Atlantis/runs/SS-Atlantis_2021-08-18T153416.049642-0700
    atlantis_cmd.run INFO: launched SS-Atlantis run via /ocean/$USER/Atlantis/runs/SS-Atlantis_2021-08-18T153416.049642-0700/Atlantis.sh

If the :command:`run` sub-command prints an error message,
you can get a Python traceback containing more information about the error by re-running the command with the :kbd:`--debug` flag.

If there are uncommitted changes in any of the version control repositories included in the :ref:`VCS-Revisions` of the run description YAML file,
a warning message for each repository will appear.
Example:

.. code-block:: bash

    $ atlantis run atlantis.yaml /ocean/$USER/Atlantis/runs/my-run/

.. code-block:: text

    nemo_cmd.prepare WARNING: There are uncommitted changes in /ocean/$USER/Atlantis/salish-sea-atlantis-model
    nemo_cmd.prepare WARNING: There are uncommitted changes in /ocean/$USER/Atlantis/AtlantisCmd
    atlantis_cmd.run INFO: Created temporary run directory: /ocean/$USER/Atlantis/runs/SS-Atlantis_2021-08-18T153416.049642-0700
    atlantis_cmd.run INFO: launched SS-Atlantis run via /ocean/$USER/Atlantis/runs/SS-Atlantis_2021-08-18T153416.049642-0700/Atlantis.sh

The warning messages start with :kbd:`nemo_cmd.prepare` because the VCS recording feature is provided by the `NEMO-Cmd package`_.

.. _NEMO-Cmd package: https://nemo-cmd.readthedocs.io/en/latest/


.. _atlantis-gather:

:kbd:`gather` Sub-command
=========================

The :command:`gather` sub-command moves results from an Atlantis temporary run directory into a results directory.
It is provided by the `NEMO-Cmd package`_.
Please use:

.. code-block:: bash

    $ atlantis help gather

to see its usage,
and see :ref:`nemocmd:nemo-gather` for more details.

If the :command:`gather` sub-command prints an error message,
you can get a Python traceback containing more information about the error by re-running the command with the :kbd:`--debug` flag.
