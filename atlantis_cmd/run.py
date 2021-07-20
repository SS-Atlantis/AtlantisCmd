#  Copyright 2021, Salish Sea Atlantis project contributors, The University of British Columbia,
#  and CSIRO.
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
#
"""AtlantisCmd command plug-in for run sub-command.

Prepare for, execute, and gather the results of a run of the CSIRO Atlantis ecosystem model.
"""
import logging
from pathlib import Path

import cliff.command

logger = logging.getLogger(__name__)


class Run(cliff.command.Command):
    """Prepare, execute, and gather results from a CSIRO Atlantis ecosystem model run."""

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.description = """
            Prepare, execute, and gather the results from an Atlantis
            run described in DESC_FILE.
            The results files from the run are gathered in RESULTS_DIR.

            If RESULTS_DIR does not exist it will be created.
        """
        parser.add_argument(
            "desc_file",
            metavar="DESC_FILE",
            type=Path,
            help="run description YAML file",
        )
        parser.add_argument(
            "results_dir",
            metavar="RESULTS_DIR",
            type=Path,
            help="directory to store results into",
        )
        parser.add_argument(
            "--no-submit",
            dest="no_submit",
            action="store_true",
            help="""
            Prepare the temporary run directory, and the bash script to 
            execute the Atlantis run, but don't launch the run.
            This is useful during development runs when you want to hack on 
            the bash script and/or use the same temporary run directory 
            more than once.
            """,
        )
        parser.add_argument(
            "-q",
            "--quiet",
            action="store_true",
            help="don't show the run directory path",
        )
        return parser

    def take_action(self, parsed_args):
        """Execute the `atlantis run` sub-command.

        :param parsed_args: Arguments and options parsed from the command-line.
        :type parsed_args: :class:`argparse.Namespace` instance
        """
        pass
