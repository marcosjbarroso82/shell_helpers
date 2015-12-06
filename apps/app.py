import subprocess


class App():
    def is_active(self):
        current_window_name = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"]).decode('utf-8').strip('\n')
        if self.app_name in current_window_name:
            return True
        return False

    def command(self, cmd):
        for app_cmd in self.cmds:
            if cmd in self.cmds[app_cmd]['aliases'] or ('miss_understood_aliases' in self.cmds[app_cmd] and cmd in self.cmds[app_cmd]['miss_understood_aliases']) :
                if self.cmds[app_cmd]['key_shortcut']:
                    subprocess.call( "xdotool key " + self.cmds[app_cmd]['key_shortcut'] , shell=True)
                else:
                    print("ERROR 244")
