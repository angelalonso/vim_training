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


def timer_controller(timer):
    app = QtGui.QApplication(sys.argv)
    mainwin = qt_windows.CounterWindow(timer)
    mainwin.show()
    sys.exit(app.exec_())


def process_controller(binary, timer):
    """
    Main function
    """

    proc = subprocess.Popen(binary)
    print "PID:", proc.pid
    # print "Return code:", proc.wait()
    timer_controller(timer)

    os.kill(proc.pid, signal.SIGTERM)


def load_config(configfile):
    config = ConfigParser.RawConfigParser()
    config.read(configfile)
    return config


if __name__ == "__main__":
    cfg = load_config("./vim_training.cfg")
    vim_binary = cfg.get('main', 'vim_path')
    timer = cfg.get('main', 'default_max_countdown')
    print timer

    # TODO:
    # SOLVE ERROR: timer int or str
    # TODO:
    # If no configuration or parameter "-config":
    #   Show configuration main screen, take vars from there

    process_controller(vim_binary, timer)
