#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" PyCharm Commands
Usage: app_pycharm.py <cmd>

Options:
    --cmd=<cmd>           bookmark, favorites, etc

"""

import subprocess
from time import sleep, time
from apps.pycharm_commands import PYCHARM_COMMANDS
from apps.app import App

class PyCharm(App):
    app_name = 'PyCharm'
    cmds = PYCHARM_COMMANDS




if __name__ == "__main__":

    from docopt import docopt
    args = docopt(__doc__)

    app = PyCharm()
    app.command(args['<cmd>'])

