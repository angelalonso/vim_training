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
from PyQt4 import QtGui
import qt_windows
import yaml


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

    commnd = str(binary) + " -O ./LEVELS/TO_DO_list.txt ./LEVELS/Warmup.txt"
    proc = subprocess.Popen(commnd, shell=True)
    print "PID:", proc.pid
    # print "Return code:", proc.wait()
    timer_controller(timer)

    os.kill(proc.pid, signal.SIGTERM)


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

    #config_controller(modesMap)
    # both at the same time wont work
    # TODO: call it from the config one?
    process_controller(vim_binary, timer)


