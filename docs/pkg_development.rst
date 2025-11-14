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


.. _AtlantisCmdPackagedDevelopment:

**************************************
:kbd:`AtlantisCmd` Package Development
**************************************

+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Continuous Integration** | .. image:: https://github.com/SS-Atlantis/AtlantisCmd/actions/workflows/pytest-with-coverage.yaml/badge.svg                                                                                          |
|                            |      :target: https://github.com/SS-Atlantis/AtlantisCmd/actions?query=workflow:pytest-with-coverage                                                                                                 |
|                            |      :alt: Pytest with Coverage Status                                                                                                                                                               |
|                            | .. image:: https://codecov.io/gh/SS-Atlantis/AtlantisCmd/branch/main/graph/badge.svg                                                                                                                 |
|                            |      :target: https://app.codecov.io/gh/SS-Atlantis/AtlantisCmd                                                                                                                                      |
|                            |      :alt: Codecov Testing Coverage Report                                                                                                                                                           |
|                            | .. image:: https://github.com/SS-Atlantis/AtlantisCmd/actions/workflows/codeql-analysis.yaml/badge.svg                                                                                               |
|                            |     :target: https://github.com/SS-Atlantis/AtlantisCmd/actions?query=workflow:CodeQL                                                                                                                |
|                            |     :alt: CodeQL analysis                                                                                                                                                                            |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Documentation**          | .. image:: https://readthedocs.org/projects/atlantiscmd/badge/?version=latest                                                                                                                        |
|                            |     :target: https://atlantiscmd.readthedocs.io/en/latest/                                                                                                                                           |
|                            |     :alt: Documentation Status                                                                                                                                                                       |
|                            | .. image:: https://github.com/SS-Atlantis/AtlantisCmd/actions/workflows/sphinx-linkcheck.yaml/badge.svg                                                                                              |
|                            |     :target: https://github.com/SS-Atlantis/AtlantisCmd/actions?query=workflow:sphinx-linkcheck                                                                                                      |
|                            |     :alt: Sphinx linkcheck                                                                                                                                                                           |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Package**                | .. image:: https://img.shields.io/github/v/release/SS-Atlantis/AtlantisCmd?logo=github                                                                                                               |
|                            |     :target: https://github.com/SS-Atlantis/AtlantisCmd/releases                                                                                                                                     |
|                            |     :alt: Releases                                                                                                                                                                                   |
|                            | .. image:: https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/SS-Atlantis/AtlantisCmd/main/pyproject.toml&logo=Python&logoColor=gold&label=Python    |
|                            |      :target: https://docs.python.org/3                                                                                                                                                              |
|                            |      :alt: Python Version from PEP 621 TOML                                                                                                                                                          |
|                            | .. image:: https://img.shields.io/github/issues/SS-Atlantis/AtlantisCmd?logo=github                                                                                                                  |
|                            |     :target: https://github.com/SS-Atlantis/AtlantisCmd/issues                                                                                                                                       |
|                            |     :alt: Issue Tracker                                                                                                                                                                              |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Meta**                   | .. image:: https://img.shields.io/badge/license-Apache%202-cb2533.svg                                                                                                                                |
|                            |     :target: https://www.apache.org/licenses/LICENSE-2.0                                                                                                                                             |
|                            |     :alt: Licensed under the Apache License, Version 2.0                                                                                                                                             |
|                            | .. image:: https://img.shields.io/badge/version%20control-git-blue.svg?logo=github                                                                                                                   |
|                            |     :target: https://github.com/SS-Atlantis/AtlantisCmd                                                                                                                                              |
|                            |     :alt: Git on GitHub                                                                                                                                                                              |
|                            +------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                            | .. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white                                                                                              |
|                            |     :target: https://pre-commit.com                                                                                                                                                                  |
|                            |     :alt: pre-commit                                                                                                                                                                                 |
|                            | .. image:: https://img.shields.io/badge/code%20style-black-000000.svg                                                                                                                                |
|                            |     :target: https://black.readthedocs.io/en/stable/                                                                                                                                                 |
|                            |     :alt: The uncompromising Python code formatter                                                                                                                                                   |
|                            | .. image:: https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg                                                                                                                                |
|                            |     :target: https://github.com/pypa/hatch                                                                                                                                                           |
|                            |     :alt: Hatch project                                                                                                                                                                              |
+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The AtlantisCmd package (:kbd:`atlantis_cmd`) is a command-line tool for doing various operations associated with the Salish Sea Atlantis project version of the CSIRO Atlantis ecosystem model. AtlantisCmd is based on, and provides Atlantis-specific extensions for https://github.com/SalishSeaCast/NEMO-Cmd.


.. _AtlantisCmdPythonVersions:

Python Versions
===============

.. image:: https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/SS-Atlantis/AtlantisCmd/main/pyproject.toml&logo=Python&logoColor=gold&label=Python
    :target: https://docs.python.org/3
    :alt: Python Version

The :kbd:`atlantis_cmd` package is developed and tested using `Python`_ 3.13.
The minimum supported Python version is 3.12.
The :ref:`AtlantisCmdContinuousIntegration` workflow on GitHub ensures that the package
is tested for all versions of Python>=3.12.

.. _Python: https://www.python.org/


.. _AtlantisCmdGettingTheCode:

Getting the Code
================

.. image:: https://img.shields.io/badge/version%20control-git-blue.svg?logo=github
    :target: https://github.com/SS-Atlantis/AtlantisCmd
    :alt: Git on GitHub

Clone the code and documentation `repository`_ from GitHub with:

.. _repository: https://github.com/SS-Atlantis/AtlantisCmd

.. code-block:: bash

    $ git clone git@github.com:SS-Atlantis/AtlantisCmd.git

or copy the URI
(the stuff after :kbd:`git clone` above)
from the :guilabel:`Code` button on the `repository`_ page.

.. note::

    The :kbd:`git clone` command above assumes that your are `connecting to GitHub using SSH`_.
    If it fails,
    please follow the instructions in our :ref:`moaddocs:SecureRemoteAccess` docs to set up your SSH keys and :ref:`moaddocs:CopyYourPublicSshKeyToGitHub`.

    .. _connecting to GitHub using SSH: https://docs.github.com/en/authentication/connecting-to-github-with-ssh


.. _AtlantisCmdDevelopmentEnvironment:

Development Environment
=======================

The :kbd:`AtlantisCmd` package depends on the `NEMO-Cmd package`_,
so you need to clone its repo,
`NEMO-Cmd`_,
beside your clone of AtlantisCmd `repository`_.

.. _NEMO-Cmd package: https://nemo-cmd.readthedocs.io/en/latest/
.. _NEMO-Cmd: https://github.com/SalishSeaCast/NEMO-Cmd

Setting up an isolated development environment using `Conda`_ is recommended.
Assuming that you have `Miniconda3`_ installed,
you can create and activate an environment called :kbd:`atlantis-cmd` that will have all of the Python packages necessary for development,
testing,
and building the documentation with the commands below.

.. _Conda: https://docs.conda.io/en/latest/
.. _Miniconda3: https://docs.conda.io/en/latest/miniconda.html

.. code-block:: bash

    $ cd AtlantisCmd
    $ conda env create -f env/environment-dev.yaml
    $ conda activate atlantis-cmd
    (atlantis-cmd)$ pip install --editable ../NEMO-Cmd
    (atlantis-cmd)$ pip install --editable .

The :kbd:`--editable` option in the :command:`pip install` commands above install the packages from the cloned repos via symlinks so that the installed packages will be automatically updated as their repos evolves.

To deactivate the environment use:

.. code-block:: bash

    (atlantis-cmd)$ conda deactivate


.. _AtlantisCmdCodingStyle:

Coding Style
============

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    :target: https://pre-commit.com
    :alt: pre-commit
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://black.readthedocs.io/en/stable/
    :alt: The uncompromising Python code formatter

The :kbd:`AtlantisCmd` package uses the Git pre-commit hooks managed by `pre-commit`_
to maintain consistent code style and and other aspects of code,
docs,
and repo QA.

.. _pre-commit: https://pre-commit.com/

To install the ``pre-commit`` hooks in a newly cloned repo,
activate the conda development environment,
and run :command:`pre-commit install`:

.. code-block:: bash

    $ cd AtlantisCmd
    $ conda activate atlantis_cmd
    (atlantis-cmd)$ pre-commit install

.. note::
    You only need to install the hooks once immediately after you make a new clone of the
    `AtlantisCmd repository`_ and build your :ref:`AtlantisCmdDevelopmentEnvironment`.

.. _AtlantisCmd repository: https://github.com/SS-Atlantis/AtlantisCmd


.. _AtlantisCmdBuildingTheDocumentation:

Building the Documentation
==========================

.. image:: https://readthedocs.org/projects/atlantiscmd/badge/?version=latest
    :target: https://atlantiscmd.readthedocs.io/en/latest/
    :alt: Documentation Status

The documentation for the :kbd:`AtlantisCmd` package is written in `reStructuredText`_ and converted to HTML using `Sphinx`_.
Creating a :ref:`AtlantisCmdDevelopmentEnvironment` as described above includes the installation of Sphinx.
Building the documentation is driven by the :file:`docs/Makefile`.
With your :kbd:`atlantis-cmd` development environment activated,
use:

.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _Sphinx: https://www.sphinx-doc.org/en/master/

.. code-block:: bash

    (atlantis-cmd)$ (cd docs && make clean html)

to do a clean build of the documentation.
The output looks something like:

.. code-block:: text

    Removing everything under '_build'...
    Running Sphinx v8.1.3
    loading translations [en]... done
    making output directory... done
    loading intersphinx inventory 'moaddocs' from https://ubc-moad-docs.readthedocs.io/en/latest/objects.inv ...
    loading intersphinx inventory 'nemocmd' from https://nemo-cmd.readthedocs.io/en/latest/objects.inv ...
    building [mo]: targets for 0 po files that are out of date
    writing output...
    building [html]: targets for 7 source files that are out of date
    updating environment: [new config] 7 added, 0 changed, 0 removed
    reading sources... [100%] subcommands
    looking for now-outdated files... none found
    pickling environment... done
    checking consistency... done
    preparing documents... done
    copying assets...
    copying static files...
    Writing evaluated template result to /media/doug/warehouse/Atlantis/AtlantisCmd/docs/_build/html/_static/language_data.js
    Writing evaluated template result to /media/doug/warehouse/Atlantis/AtlantisCmd/docs/_build/html/_static/basic.css
    Writing evaluated template result to /media/doug/warehouse/Atlantis/AtlantisCmd/docs/_build/html/_static/documentation_options.js
    Writing evaluated template result to /media/doug/warehouse/Atlantis/AtlantisCmd/docs/_build/html/_static/js/versions.js
    copying static files: done
    copying extra files...
    copying extra files: done
    copying assets: done
    writing output... [100%] subcommands
    generating indices... genindex done
    writing additional pages... search done
    dumping search index in English (code: en)... done
    dumping object inventory... done
    build succeeded.

    The HTML pages are in _build/html.

The HTML rendering of the docs ends up in :file:`docs/_build/html/`.
You can open the :file:`index.html` file in that directory tree in your browser to preview the results of the build.

If you have write access to the `repository`_ on GitHub,
whenever you push changes to GitHub the documentation is automatically re-built and rendered at https://atlantiscmd.readthedocs.io/en/latest/.


.. _AtlantisCmdLinkCheckingTheDocumentation:

Link Checking the Documentation
-------------------------------

.. image:: https://github.com/SS-Atlantis/AtlantisCmd/workflows/sphinx-linkcheck/badge.svg
    :target: https://github.com/SS-Atlantis/AtlantisCmd/actions?query=workflow%3Asphinx-linkcheck
    :alt: Sphinx linkcheck


Sphinx also provides a link checker utility which can be run to find broken or redirected links in the docs.
With your :kbd:`atlantis-cmd)` environment activated,
use:

.. code-block:: bash

    (atlantis-cmd))$ cd AtlantisCmd/docs/
    (atlantis-cmd)) docs$ make linkcheck

The output looks something like:

.. code-block:: text

    Removing everything under '_build'...
    Running Sphinx v8.1.3
    loading translations [en]... done
    making output directory... done
    loading intersphinx inventory 'moaddocs' from https://ubc-moad-docs.readthedocs.io/en/latest/objects.inv ...
    loading intersphinx inventory 'nemocmd' from https://nemo-cmd.readthedocs.io/en/latest/objects.inv ...
    building [mo]: targets for 0 po files that are out of date
    writing output...
    building [linkcheck]: targets for 7 source files that are out of date
    updating environment: [new config] 7 added, 0 changed, 0 removed
    reading sources... [100%] subcommands
    looking for now-outdated files... none found
    pickling environment... done
    checking consistency... done
    preparing documents... done
    copying assets...
    copying assets: done
    writing output... [100%] subcommands

    ( pkg_development: line   23) ok        https://black.readthedocs.io/en/stable/
    ( pkg_development: line   23) ok        https://atlantiscmd.readthedocs.io/en/latest/
    ( pkg_development: line   29) ok        https://codecov.io/gh/SS-Atlantis/AtlantisCmd/branch/main/graph/badge.svg
    ( pkg_development: line   23) ok        https://app.codecov.io/gh/SS-Atlantis/AtlantisCmd
    (     subcommands: line  119) ok        https://cookiecutter.readthedocs.io/en/latest/
    ( pkg_development: line  404) ok        https://coverage.readthedocs.io/en/latest/
    (installation/atlantis_cmd: line   70) ok        https://docs.conda.io/en/latest/
    ( pkg_development: line  453) ok        https://docs.github.com/en/actions
    (installation/atlantis_cmd: line   60) ok        https://docs.github.com/en/authentication/connecting-to-github-with-ssh
    (installation/atlantis_cmd: line   70) ok        https://docs.conda.io/en/latest/miniconda.html
    ( pkg_development: line  467) ok        https://git-scm.com/
    ( pkg_development: line  374) ok        https://docs.pytest.org/en/latest/
    (           index: line   30) ok        https://docs.openstack.org/cliff/latest/
    ( pkg_development: line   23) ok        https://docs.python.org/3
    (run_description_file/index: line   30) redirect  https://bitbucket.csiro.au/users/por07g/repos/salish-sea-atlantis-model/browse - with Found to https://bitbucket.csiro.au/login
    ( pkg_development: line   32) ok        https://github.com/SS-Atlantis/AtlantisCmd/actions/workflows/codeql-analysis.yaml/badge.svg
    (           index: line   23) ok        https://github.com/SS-Atlantis/AtlantisCmd
    ( pkg_development: line   26) ok        https://github.com/SS-Atlantis/AtlantisCmd/actions/workflows/pytest-with-coverage.yaml/badge.svg
    ( pkg_development: line   39) ok        https://github.com/SS-Atlantis/AtlantisCmd/actions/workflows/sphinx-linkcheck.yaml/badge.svg
    ( pkg_development: line  442) ok        https://github.com/SS-Atlantis/AtlantisCmd/actions
    ( pkg_development: line  433) ok        https://github.com/SS-Atlantis/AtlantisCmd/actions?query=workflow%3Apytest-with-coverage
    ( pkg_development: line  267) ok        https://github.com/SS-Atlantis/AtlantisCmd/actions?query=workflow%3Asphinx-linkcheck
    ( pkg_development: line   23) ok        https://github.com/SS-Atlantis/AtlantisCmd/actions?query=workflow:CodeQL
    ( pkg_development: line   23) ok        https://github.com/SS-Atlantis/AtlantisCmd/actions?query=workflow:pytest-with-coverage
    ( pkg_development: line   23) ok        https://github.com/SS-Atlantis/AtlantisCmd/issues
    ( pkg_development: line   23) ok        https://github.com/SS-Atlantis/AtlantisCmd/releases
    ( pkg_development: line  435) ok        https://github.com/SS-Atlantis/AtlantisCmd/workflows/pytest-with-coverage/badge.svg
    ( pkg_development: line  442) ok        https://github.com/SS-Atlantis/AtlantisCmd/commits/main
    ( pkg_development: line   23) ok        https://github.com/SS-Atlantis/AtlantisCmd/actions?query=workflow:sphinx-linkcheck
    ( pkg_development: line  269) ok        https://github.com/SS-Atlantis/AtlantisCmd/workflows/sphinx-linkcheck/badge.svg
    ( pkg_development: line   66) ok        https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg
    ( pkg_development: line   60) ok        https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    ( pkg_development: line   63) ok        https://img.shields.io/badge/code%20style-black-000000.svg
    (           index: line   58) ok        https://img.shields.io/badge/license-Apache%202-cb2533.svg
    ( pkg_development: line   56) ok        https://img.shields.io/badge/version%20control-git-blue.svg?logo=github
    ( pkg_development: line   49) ok        https://img.shields.io/github/issues/SS-Atlantis/AtlantisCmd?logo=github
    ( pkg_development: line   43) ok        https://img.shields.io/github/v/release/SS-Atlantis/AtlantisCmd?logo=github
    ( pkg_development: line   46) ok        https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/SS-Atlantis/AtlantisCmd/main/pyproject.toml&logo=Python&logoColor=gold&label=Python
    (installation/atlantis_cmd: line   46) ok        https://nemo-cmd.readthedocs.io/en/latest/
    ( pkg_development: line   23) ok        https://github.com/pypa/hatch
    (           index: line   30) ok        https://github.com/SalishSeaCast/NEMO-Cmd
    (     subcommands: line  181) ok        https://nemo-cmd.readthedocs.io/en/latest/subcommands.html#nemo-gather
    (run_description_file/index: line   25) ok        https://pyyaml.org/wiki/PyYAMLDocumentation
    ( pkg_development: line   23) ok        https://pre-commit.com
    ( pkg_development: line  404) ok        https://pytest-cov.readthedocs.io/en/latest/
    ( pkg_development: line  172) ok        https://pre-commit.com/
    (           index: line   56) ok        https://www.apache.org/licenses/LICENSE-2.0
    (installation/atlantis_cmd: line   60) ok        https://ubc-moad-docs.readthedocs.io/en/latest/ssh_access.html#copyyourpublicsshkeytogithub
    (installation/atlantis_cmd: line   60) ok        https://ubc-moad-docs.readthedocs.io/en/latest/ssh_access.html#secureremoteaccess
    ( pkg_development: line   83) ok        https://www.python.org/
    ( pkg_development: line  205) ok        https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
    ( pkg_development: line  205) ok        https://www.sphinx-doc.org/en/master/
    ( pkg_development: line   36) ok        https://readthedocs.org/projects/atlantiscmd/badge/?version=latest
    build succeeded.

    Look for any errors in the above output or in _build/linkcheck/output.txt

:command:`make linkcheck` is run monthly via a `scheduled GitHub Actions workflow`_

.. _scheduled GitHub Actions workflow: https://github.com/SS-Atlantis/AtlantisCmd/actions?query=workflow%3Asphinx-linkcheck


.. _AtlantisCmdRunningTheUnitTests:

Running the Unit Tests
======================

The test suite for the :kbd:`AtlantisCmd` package is in :file:`AtlantisCmd/tests/`.
The `pytest`_ tool is used for test parametrization and as the test runner for the suite.

.. _pytest: https://docs.pytest.org/en/latest/

With your :kbd:`atlantis-cmd` development environment activated,
use:

.. code-block:: bash

    (atlantis-cmd)$ cd AtlantisCmd/
    (atlantis-cmd)$ pytest

to run the test suite.
The output looks something like:

.. code-block:: text

    ================================ test session starts =================================
    platform linux -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
    Using --randomly-seed=990869215
    rootdir: /media/doug/warehouse/Atlantis/AtlantisCmd
    configfile: pyproject.toml
    plugins: anyio-4.8.0, randomly-3.15.0, cov-6.0.0
    collected 49 items

    tests/test_post_gen_project.py ........                                         [ 16%]
    tests/test_run.py .........................................                     [100%]

    ================================= 49 passed in 0.98s =================================

You can monitor what lines of code the test suite exercises using the `coverage.py`_ and `pytest-cov`_ tools with the command:

.. _coverage.py: https://coverage.readthedocs.io/en/latest/
.. _pytest-cov: https://pytest-cov.readthedocs.io/en/latest/

.. code-block:: bash

    (atlantis-cmd)$ cd AtlantisCmd/
    (atlantis-cmd)$ pytest --cov=./

and generate a test coverage report with:

.. code-block:: bash

    (atlantis-cmd)$ coverage report

to produce a plain text report,
or

.. code-block:: bash

    (atlantis-cmd)$ coverage html

to produce an HTML report that you can view in your browser by opening :file:`AtlantisCmd/htmlcov/index.html`.


.. _AtlantisCmdContinuousIntegration:

Continuous Integration
----------------------

.. image:: https://github.com/SS-Atlantis/AtlantisCmd/workflows/pytest-with-coverage/badge.svg
    :target: https://github.com/SS-Atlantis/AtlantisCmd/actions?query=workflow%3Apytest-with-coverage
    :alt: Pytest with Coverage Status
.. image:: https://codecov.io/gh/SS-Atlantis/AtlantisCmd/branch/main/graph/badge.svg
    :target: https://app.codecov.io/gh/SS-Atlantis/AtlantisCmd
    :alt: Codecov Testing Coverage Report

The :kbd:`AtlantisCmd` package unit test suite is run and a coverage report is generated whenever changes are pushed to GitHub.
The results are visible on the `repo actions page`_,
from the green checkmarks beside commits on the `repo commits page`_,
or from the green checkmark to the left of the "Latest commit" message on the `repo code overview page`_ .
The testing coverage report is uploaded to `codecov.io`_

.. _repo actions page: https://github.com/SS-Atlantis/AtlantisCmd/actions
.. _repo commits page: https://github.com/SS-Atlantis/AtlantisCmd/commits/main
.. _repo code overview page: https://github.com/SS-Atlantis/AtlantisCmd
.. _codecov.io: https://app.codecov.io/gh/SS-Atlantis/AtlantisCmd

The `GitHub Actions`_ workflow configuration that defines the continuous integration tasks is in the :file:`.github/workflows/pytest-coverage.yaml` file.

.. _GitHub Actions: https://docs.github.com/en/actions


.. _AtlantisCmdVersionControlRepository:

Version Control Repository
==========================

.. image:: https://img.shields.io/badge/version%20control-git-blue.svg?logo=github
    :target: https://github.com/SS-Atlantis/AtlantisCmd
    :alt: Git on GitHub

The :kbd:`AtlantisCmd` package code and documentation source files are available as a `Git`_ repository at https://github.com/SS-Atlantis/AtlantisCmd.

.. _Git: https://git-scm.com/


.. _AtlantisCmdIssueTracker:

Issue Tracker
=============

.. image:: https://img.shields.io/github/issues/SS-Atlantis/AtlantisCmd?logo=github
    :target: https://github.com/SS-Atlantis/AtlantisCmd/issues
    :alt: Issue Tracker

Development tasks,
bug reports,
and enhancement ideas are recorded and managed in the issue tracker at https://github.com/SS-Atlantis/AtlantisCmd/issues.


License
=======

.. image:: https://img.shields.io/badge/license-Apache%202-cb2533.svg
    :target: https://www.apache.org/licenses/LICENSE-2.0
    :alt: Licensed under the Apache License, Version 2.0

The code and documentation of the Atlantis Command Processor project
are copyright 2021 – present by the Salish Sea Atlantis project contributors,
The University of British Columbia, and CSIRO.

They are licensed under the Apache License, Version 2.0.
https://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file for details of the license.


Release Process
===============

.. image:: https://img.shields.io/github/v/release/SS-Atlantis/AtlantisCmd?logo=github
    :target: https://github.com/SS-Atlantis/AtlantisCmd/releases
    :alt: Releases
.. image:: https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg
    :target: https://github.com/pypa/hatch
    :alt: Hatch project

Releases are done at Doug's discretion when significant pieces of development work have been
completed.

The release process steps are:

#. Use :command:`hatch version release` to bump the version from ``.devn`` to the next release
   version identifier

#. Commit the version bump

#. Create and annotated tag for the release with :guilabel:`Git -> New Tag...` in PyCharm
   or :command:`git tag -e -a vyy.n`

#. Push the version bump commit and tag to GitHub

#. Use the GitHub web interface to create a release,
   editing the auto-generated release notes into sections:

   * Features
   * Bug Fixes
   * Documentation
   * Maintenance
   * Dependency Updates

#. Use the GitHub :guilabel:`Issues -> Milestones` web interface to edit the release
   milestone:

   * Change the :guilabel:`Due date` to the release date
   * Delete the "when it's ready" comment in the :guilabel:`Description`

#. Use the GitHub :guilabel:`Issues -> Milestones` web interface to create a milestone for
   the next release:

   * Set the :guilabel:`Title` to the next release version,
     prepended with a ``v``;
     e.g. ``v25.1``
   * Set the :guilabel:`Due date` to the end of the year of the next release
   * Set the :guilabel:`Description` to something like
     ``v25.1 release - when it's ready :-)``
   * Create the next release milestone

#. Review the open issues,
   especially any that are associated with the milestone for the just released version,
   and update their milestone.

#. Close the milestone for the just released version.

#. Use :command:`hatch version minor,dev` to bump the version for the next development cycle,
   or use :command:`hatch version major,minor,dev` for a year rollover version bump

#. Commit the version bump

#. Push the version bump commit to GitHub
