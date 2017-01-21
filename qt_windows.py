#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Manages the pyQt windows needed
"""


import sys
from PyQt4 import QtGui, QtCore


class CounterWindow(QtGui.QWidget):
    """
    window class for PyQt4 countdown timer
    Based on
    http://stackoverflow.com/questions/12661211/cant-seem-to-get-pyqt-countdown-timer-to-work#12661563
    """
    def __init__(self, timerinit, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.timer = QtCore.QTimer()
        text = "%d:%02d" % (timerinit / 60, timerinit % 60)

        self.timerlabel = QtGui.QLabel()
        self.timerlabel.move(20, 20)

        self.timerlabel.setText(text)
        self.timer.start(1000)

        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.addWidget(self.timerlabel, 1, 1, 1, 1)
        self.setLayout(self.gridLayout)

        self.startTimerDisplay(timerinit)
        self.timer.timeout.connect(self.updateTimerDisplay)

    def startTimerDisplay(self, timerinit):
        """ set the countdown value and start the timer """
        self.init = timerinit
        self.timer.start(1000)

    def updateTimerDisplay(self):
        """ count down one second, set the text,
        and check if the timer should stop """
        self.init -= 1
        text = "%d:%02d" % (self.init / 60, self.init % 60)
        self.timerlabel.setText(text)
        if self.init == 0:
            self.timer.stop()
            self.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainwin = CounterWindow(5)
    mainwin.show()
    sys.exit(app.exec_())
