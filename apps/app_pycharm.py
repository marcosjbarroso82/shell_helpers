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

class PyCharm():
    app_name = 'PyCharm'
    cmds = PYCHARM_COMMANDS

    def is_active(self):
        current_window_name = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"]).decode('utf-8').strip('\n')
        if self.app_name in current_window_name:
            return True
        return False

    def favorites(self):
        subprocess.call( "xdotool key alt+2" , shell=True)

    def pin_tab(self):
        subprocess.call( "xdotool key alt+p" , shell=True)

    def command(self, cmd):
        print("PyCharm Command: " + cmd)
        for app_cmd in self.cmds:
            if cmd in self.cmds[app_cmd]['aliases'] or ('miss_understood_aliases' in self.cmds[app_cmd] and cmd in self.cmds[app_cmd]['miss_understood_aliases']) :
                if self.cmds[app_cmd]['key_shortcut']:
                    print(self.cmds[app_cmd]['key_shortcut'])
                    subprocess.call( "xdotool key " + self.cmds[app_cmd]['key_shortcut'] , shell=True)
                else:
                    print("ERROR 244")



if __name__ == "__main__":

    from docopt import docopt
    args = docopt(__doc__)

    app = PyCharm()
    app.command(args['<cmd>'])

