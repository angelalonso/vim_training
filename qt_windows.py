#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Manages the pyQt windows needed
TO BE ADAPTED FOR THIS PROJECT!
"""


import sys
from PyQt4 import QtGui, QtCore


class CounterWindow(QtGui.QWidget):
    """
    window class for PyQt4 countdown timer
    """
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.inicio = 5

        self.timer = QtCore.QTimer()
        text = "%d:%02d" % (self.inicio / 60, self.inicio % 60)

        self.timerlabel = QtGui.QLabel()
        self.timerlabel.move(20, 20)

        self.timerlabel.setText(text)
        self.timer.start(1000)

        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.addWidget(self.timerlabel, 1, 1, 1, 1)
        self.setLayout(self.gridLayout)

        self.startTimerDisplay()
        self.timer.timeout.connect(self.updateTimerDisplay)

    def startTimerDisplay(self):
        """ set the countdown value and start the timer """
        self.inicio = 5
        self.timer.start(1000)

    def updateTimerDisplay(self):
        """ count down one second, set the text,
        and check if the timer should stop """
        self.inicio -= 1
        text = "%d:%02d" % (self.inicio/60, self.inicio % 60)
        self.timerlabel.setText(text)
        if self.inicio == 0:
            self.timer.stop()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mainwin = CounterWindow()
    #mainwin.updateTimerDisplay()
    mainwin.show()
    sys.exit(app.exec_())
