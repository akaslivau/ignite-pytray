import os
import shutil
import subprocess
import time

import pygetwindow as gw
import pystray
from PIL import Image

image = Image.open("ignite.png")
ignite_home = os.path.normpath(os.environ.get('IGNITE_HOME'))
config = "base-config.xml"

dirs_to_remove = [
    os.path.join(ignite_home, "work", "db"),
    os.path.join(ignite_home, "work", "log"),
    os.path.join(ignite_home, "work", "opt"),
    os.path.join(ignite_home, "tempshit")
]

if __name__ == "__main__":
    def cmd_start_cluster():
        single_node()
        time.sleep(3)
        single_node()
        time.sleep(7)
        activate()


    def cmd_start_node():
        single_node()
        time.sleep(5)
        activate()


    def cmd_hard_reset():
        for dir_path in dirs_to_remove:
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path)


    def cmd_stop_all():
        windows = gw.getWindowsWithTitle("")
        for window in windows:
            if 'ignite.bat' in window.title:
                window.close()


    def single_node():
        ignite_cmd = ['start', 'cmd', '/k',
                      subprocess.list2cmdline([
                          os.path.join(ignite_home, "bin", "ignite.bat"),
                          os.path.join(ignite_home, "config", config)
                      ])]
        subprocess.Popen(ignite_cmd, shell=True)


    def control(args):
        control_cmd = ['start', 'cmd', '/k',
                       subprocess.list2cmdline([os.path.join(ignite_home, "bin", "control.bat"), *args])]
        subprocess.Popen(control_cmd, shell=True)


    def activate():
        control(['--set-state', 'ACTIVE'])


    def baseline():
        control(['--baseline'])


def exit_program(icon):
    icon.stop()
    os._exit(1)


icon = pystray.Icon(name='any_icon', icon=image)

icon.menu = (
    pystray.MenuItem("Baseline", baseline),
    pystray.MenuItem("Activate", activate),
    pystray.MenuItem("Start cluster", cmd_start_cluster),
    pystray.MenuItem("Start node", cmd_start_node),
    pystray.MenuItem("________", None),
    pystray.MenuItem("Stop all", cmd_stop_all),
    pystray.MenuItem("Hard reset", cmd_hard_reset),
    pystray.MenuItem("Exit", exit_program),
)
icon.run_detached()
