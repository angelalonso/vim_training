#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Controls all parts involved on the VIM Training
"""

import os
import signal
import subprocess
import sys
import time
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

if __name__ == "__main__":
    VIM_BIN = "/usr/bin/vim"
    TIMER = 6

    # TODO:
    # If no configuration or parameter "-config":
    #   Show configuration main screen, take vars from there

    process_controller(VIM_BIN, TIMER)
