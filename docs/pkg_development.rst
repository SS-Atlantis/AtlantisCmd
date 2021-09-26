.. Copyright 2021, Salish Sea Atlantis project contributors, The University of British Columbia, and CSIRO
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


.. _AtlantisCmdPackagedDevelopment:

**************************************
:kbd:`AtlantisCmd` Package Development
**************************************


.. image:: https://img.shields.io/badge/license-Apache%202-cb2533.svg
    :target: https://www.apache.org/licenses/LICENSE-2.0
    :alt: Licensed under the Apache License, Version 2.0
.. image:: https://img.shields.io/badge/python-3.9-blue.svg
    :target: https://docs.python.org/3.9/
    :alt: Python Version
.. image:: https://img.shields.io/badge/version%20control-git-blue.svg?logo=github
    :target: https://github.com/SS-Atlantis/AtlantisCmd
    :alt: Git on GitHub
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://black.readthedocs.io/en/stable/
    :alt: The uncompromising Python code formatter
.. image:: https://readthedocs.org/projects/AtlantisCmd/badge/?version=latest
    :target: https://atlantiscmd.readthedocs.io/en/latest/
    :alt: Documentation Status
.. image:: https://github.com/SS-Atlantis/AtlantisCmd/workflows/CI/badge.svg
    :target: https://github.com/SS-Atlantis/AtlantisCmd/actions?query=workflow%3ACI
    :alt: pytest and test coverage analysis
.. image:: https://codecov.io/gh/SS-Atlantis/AtlantisCmd/branch/main/graph/badge.svg
    :target: https://app.codecov.io/gh/SS-Atlantis/AtlantisCmd
    :alt: Codecov Testing Coverage Report
.. image:: https://github.com/SS-Atlantis/AtlantisCmd/actions/workflows/codeql-analysis.yaml/badge.svg
      :target: https://github.com/SS-Atlantis/AtlantisCmd/actions?query=workflow:codeql-analysis
      :alt: CodeQL analysis
.. image:: https://img.shields.io/github/issues/SS-Atlantis/AtlantisCmd?logo=github
    :target: https://github.com/SS-Atlantis/AtlantisCmd/issues
    :alt: Issue Tracker

The AtlantisCmd package (:kbd:`atlantis_cmd`) is a command-line tool for doing various operations associated with the Salish Sea Atlantis project version of the CSIRO Atlantis ecosystem model. AtlantisCmd is based on, and provides Atlantis-specific extensions for https://github.com/SalishSeaCast/NEMO-Cmd.


.. _AtlantisCmdPythonVersions:

Python Versions
===============

.. image:: https://img.shields.io/badge/python-3.9-blue.svg
    :target: https://docs.python.org/3.9/
    :alt: Python Version

The :kbd:`atlantis_cmd` package is developed and tested using `Python`_ 3.9.
The package uses some Python language features that are not available in versions prior to 3.8,
in particular:

* `formatted string literals`_
  (aka *f-strings*)
  with :kbd:`=` specifiers

.. _Python: https://www.python.org/
.. _formatted string literals: https://docs.python.org/3/reference/lexical_analysis.html#f-strings


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

    .. _connecting to GitHub using SSH: https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh


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

.. _Conda: https://conda.io/en/latest/
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

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://black.readthedocs.io/en/stable/
    :alt: The uncompromising Python code formatter

The :kbd:`AtlantisCmd` package uses the `black`_ code formatting tool to maintain a coding style that is very close to `PEP 8`_.

.. _black: https://black.readthedocs.io/en/stable/
.. _PEP 8: https://www.python.org/dev/peps/pep-0008/

:command:`black` is installed as part of the :ref:`AtlantisCmdDevelopmentEnvironment` setup.

To run :command:`black` on the entire code-base use:

.. code-block:: bash

    $ cd AtlantisCmd
    $ conda activate atlantis_cmd
    (atlantis-cmd)$ black ./

in the repository root directory.
The output looks something like:

.. code-block:: text

    **add example black output**


.. _AtlantisCmdBuildingTheDocumentation:

Building the Documentation
==========================

.. image:: https://readthedocs.org/projects/atlantiscmd/badge/?version=latest
    :target: https://atlantiscmd.readthedocs.io/en/latest/
    :alt: Documentation Status

The documentation for the :kbd:`AtlantisCmd` package is written in `reStructuredText`_ and converted to HTML using `Sphinx`_.
Creating a :ref:`AtlantisCmdDevelopmentEnvironment` as described above includes the installation of Sphinx.
Building the documentation is driven by the :file:`docs/Makefile`.
With your :kbd:`salishsea-nowcast` development environment activated,
use:

.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _Sphinx: https://www.sphinx-doc.org/en/master/

.. code-block:: bash

    (atlantis-cmd)$ (cd docs && make clean html)

to do a clean build of the documentation.
The output looks something like:

.. code-block:: text

    Running Sphinx v4.1.1
    loading pickled environment... done
    building [mo]: targets for 0 po files that are out of date
    building [html]: targets for 1 source files that are out of date
    updating environment: 0 added, 1 changed, 0 removed
    reading sources... [100%] pkg_development
    looking for now-outdated files... none found
    pickling environment... done
    checking consistency... done
    preparing documents... done
    writing output... [ 50%] index
    writing output... [100%] pkg_development
    generating indices... genindex done
    writing additional pages... search done
    copying static files... done
    copying extra files... done
    dumping search index in English (code: en)... done
    dumping object inventory... done
    build succeeded.

    The HTML pages are in docs/_build.


The HTML rendering of the docs ends up in :file:`docs/_build/html/`.
You can open the :file:`index.html` file in that directory tree in your browser to preview the results of the build.

If you have write access to the `repository`_ on GitHub,
whenever you push changes to GitHub the documentation is automatically re-built and rendered at https://atlantiscmd.readthedocs.io/en/latest/.


.. _AtlantisCmdLinkCheckingTheDocumentation:

Link Checking the Documentation
-------------------------------

Sphinx also provides a link checker utility which can be run to find broken or redirected links in the docs.
With your :kbd:`atlantis-cmd)` environment activated,
use:

.. code-block:: bash

    (atlantis-cmd))$ cd AtlantisCmd/docs/
    (atlantis-cmd)) docs$ make linkcheck

The output looks something like:

.. code-block:: text

    Running Sphinx v4.1.1
    loading pickled environment... done
    building [mo]: targets for 0 po files that are out of date
    building [linkcheck]: targets for 2 source files that are out of date
    updating environment: 0 added, 1 changed, 0 removed
    reading sources... [100%] pkg_development

    looking for now-outdated files... none found
    pickling environment... done
    checking consistency... done
    preparing documents... done
    writing output... [ 50%] index
    writing output... [100%] pkg_development


    ( pkg_development: line  255) ok        https://coverage.readthedocs.io/en/latest/
    ( pkg_development: line   20) ok        https://black.readthedocs.io/en/stable/
    ( pkg_development: line  237) ok        https://docs.pytest.org/en/latest/
    ( pkg_development: line   20) ok        https://docs.python.org/3.9/
    ( pkg_development: line  101) ok        https://conda.io/en/latest/
    ( pkg_development: line  101) ok        https://docs.conda.io/en/latest/miniconda.html
    ( pkg_development: line  289) ok        https://git-scm.com/
    ( pkg_development: line   58) ok        https://docs.python.org/3/reference/lexical_analysis.html#f-strings
    ( pkg_development: line   89) ok        https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh
    ( pkg_development: line   20) ok        https://atlantiscmd.readthedocs.io/en/latest/
    ( pkg_development: line   20) ok        https://img.shields.io/badge/code%20style-black-000000.svg
    (           index: line   36) ok        https://img.shields.io/badge/license-Apache%202-cb2533.svg
    ( pkg_development: line   20) ok        https://img.shields.io/badge/python-3.9-blue.svg
    ( pkg_development: line   20) ok        https://img.shields.io/badge/version%20control-git-blue.svg?logo=github
    ( pkg_development: line   20) ok        https://github.com/SS-Atlantis/AtlantisCmd/issues
    ( pkg_development: line   20) ok        https://github.com/SS-Atlantis/AtlantisCmd
    ( pkg_development: line   42) ok        https://github.com/SalishSeaCast/NEMO-Cmd
    ( pkg_development: line   20) ok        https://img.shields.io/github/issues/SS-Atlantis/AtlantisCmd?logo=github
    ( pkg_development: line   89) ok        https://ubc-moad-docs.readthedocs.io/en/latest/ssh_access.html#secureremoteaccess
    ( pkg_development: line   54) ok        https://www.python.org/
    ( pkg_development: line   89) ok        https://ubc-moad-docs.readthedocs.io/en/latest/ssh_access.html#copyyourpublicsshkeytogithub
    ( pkg_development: line  135) ok        https://www.python.org/dev/peps/pep-0008/
    ( pkg_development: line  165) ok        https://www.sphinx-doc.org/en/master/
    ( pkg_development: line  165) ok        https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
    ( pkg_development: line   20) ok        https://readthedocs.org/projects/AtlantisCmd/badge/?version=latest
    ( pkg_development: line  159) ok        https://readthedocs.org/projects/atlantiscmd/badge/?version=latest
    (           index: line   36) ok        https://www.apache.org/licenses/LICENSE-2.0
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
    platform linux -- Python 3.9.6, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
    Using --randomly-seed=3861485000
    rootdir: /media/doug/warehouse/Atlantis/AtlantisCmd
    plugins: randomly-3.8.0, cov-2.12.1
    collected 1 item

    tests/test_run.py .                                                                                                                                                                                                                                                                                            [100%]

    ================================= 1 passed in 0.17s ==================================

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

.. image:: https://github.com/SS-Atlantis/AtlantisCmd/workflows/CI/badge.svg
    :target: https://github.com/SS-Atlantis/AtlantisCmd/actions?query=workflow%3ACI
    :alt: GitHub Workflow Status
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
are copyright 2021 by Salish Sea Atlantis project contributors, The University of British Columbia, and CSIRO.

They are licensed under the Apache License, Version 2.0.
https://www.apache.org/licenses/LICENSE-2.0
Please see the LICENSE file for details of the license.
