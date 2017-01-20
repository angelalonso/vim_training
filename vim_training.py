#!/usr/bin/env python
"""
Controls all parts involved on the VIM Training
"""

import os
import signal
import subprocess
import time



def process_controller(binary, timer):
    """
    Main function
    """

    # TODO: Show timer on pyqt

    proc = subprocess.Popen(VIM_BIN)
    print "PID:", proc.pid
    # print "Return code:", proc.wait()
    time.sleep(timer)

    os.kill(proc.pid, signal.SIGTERM)

if __name__ == "__main__":
    VIM_BIN = "/usr/bin/vim"
    TIMER = 5

    # Show configuration main screen, take vars from there

    process_controller(VIM_BIN, TIMER)
