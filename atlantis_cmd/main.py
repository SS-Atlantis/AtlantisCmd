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
"""AtlantisCmd application

Atlantis Ecosystem Model Command Processor

This module is connected to the `atlantis` command via a console_scripts
entry point in setup.py.
"""
import sys

import cliff.app
import cliff.commandmanager

import atlantis_cmd


class AtlantisCmdApp(cliff.app.App):
    CONSOLE_MESSAGE_FORMAT = "%(name)s %(levelname)s: %(message)s"

    def __init__(self):
        super().__init__(
            description="Atlantis Ecosystem Model Command Processor",
            version=atlantis_cmd.__version__,
            command_manager=cliff.commandmanager.CommandManager(
                "atlantis.app", convert_underscores=False
            ),
            stderr=sys.stdout,
        )


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    app = AtlantisCmdApp()
    return app.run(argv)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
