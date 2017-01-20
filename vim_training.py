#!/usr/bin/env python
"""
Controls all parts involved on the VIM Training
"""

import os
import signal
import subprocess
import time

VIM_BIN = "/usr/bin/vim"
TIMER = 15


def main():
    """
    Main function
    """

    proc = subprocess.Popen(VIM_BIN)
    print "PID:", proc.pid
    #print "Return code:", proc.wait()
    time.sleep(TIMER)

    os.kill(proc.pid, signal.SIGTERM)

if __name__ == "__main__":
    main()
