#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Controls all parts involved on the VIM Training
"""

import ConfigParser
import os
import signal
import subprocess
import sys
import time
import shutil
import psutil
from PyQt4 import QtGui
import yaml
import qt_windows


def timer_controller(timer):
    app = QtGui.QApplication(sys.argv)
    mainwin = qt_windows.CounterWindow(timer)
    mainwin.show()
    sys.exit(app.exec_())


def config_controller(modesMap):
    app = QtGui.QApplication(sys.argv)
    configwin = qt_windows.ConfigWindow(modesMap)
    configwin.show()
    sys.exit(app.exec_())


def process_controller(binary, timer):
    """
    Main function
    """

    # command = str(binary) + " -O ./LEVELS/TO_DO_list.txt ./LEVELS/Warmup.txt"
    shutil.copyfile('./LEVELS/TO_DO_list.orig.txt', './LEVELS/TO_DO_list.txt')
    command = '/usr/bin/terminator -m -e "/usr/bin/vim -O \
            ./LEVELS/TO_DO_list.txt \
            ./LEVELS/TO_DO_list.goal.txt \
            ./LEVELS/TO_DO_list.tips.txt"'
    proc = subprocess.Popen(command, shell=True)

    # TODO: when this is enabled, the program is unable to kill the vim process
    # (or do anything else at all)
    # timer_controller(timer)
    time.sleep(timer)

    # somehow os.kill does not...well, kill it
    for child in psutil.Process(proc.pid).children():
        os.kill(child.pid, signal.SIGKILL)

    os.kill(proc.pid, signal.SIGKILL)
    # TODO:
    # - Save current work before killing
    # - Diff work and goal
    # - remove any .swp leftovers
    os.remove('./LEVELS/.TO_DO_list.txt.swp')
    print ("Your time is over!")


def load_config(configfile):
    config = ConfigParser.RawConfigParser()
    config.read(configfile)
    return config


if __name__ == "__main__":
    cfg = load_config("./user.cfg")
    vim_binary = cfg.get('main', 'vim_path')
    timer = int(cfg.get('main', 'default_max_countdown'))
    f = open('./modes.yaml')
    # use safe_load instead load
    modesMap = yaml.safe_load(f)[0]
    f.close()

    # TODO:
    # If no configuration or parameter "-config":
    #   Show configuration main screen, take vars from there

    # config_controller(modesMap)
    # both at the same time wont work
    # TODO: call it from the config one?
    process_controller(vim_binary, timer)
