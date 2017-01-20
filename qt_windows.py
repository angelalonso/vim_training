#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
TO BE ADAPTED FOR THIS PROJECT!
"""

"""
First draft taken from:
 http://stackoverflow.com/questions/15561608/detecting-enter-on-a-qlineedit-or-qpushbutton#15567835
TODO:
    - Add equivalent actions form Vault CLI
"""

import subprocess
import sys
from PyQt4 import QtGui, QtCore


def get_passnames():
    """
    Gets a list of Secret 'titles' to choose from
    ATTENTION: not yet supported by Vault!
    """

    passlist = []
    # TODO: Change this dummy for a future equivalent Vault CLI command
    cmd = "./test.sh pass"
    process = subprocess.Popen(cmd, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    # wait for the process to terminate
    out, err = process.communicate()
    errcode = process.returncode
    # Print any error
    if errcode > 0:
        print str(errcode) + ": " + err
    for word in out.split(' '):
        passlist.append(word)
    return passlist


def get_pass(passname):
    """
    Gets the secret behind the chosen 'title'
    """
    password = passname + 'blah'
    # TODO: Test the following and change the previous dummy for this
    """
    cmd = "vault read " + passname + " | grep value | cut -d' ' -f2-"
    process = subprocess.Popen(cmd, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    password, err = process.communicate()
    errcode = process.returncode
    if errcode > 0:
        print str(errcode) + ": " + err
    """
    return password


class MyWindow(QtGui.QWidget):
    """
    Main window class for PyQt4
    """
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.setGeometry(412, 250, 600, 150)

        self.passnames = get_passnames()

        self.label = QtGui.QLabel()
        self.label.move(20, 20)
        self.label.setText("What are you looking for?")

        self.model = QtGui.QStringListModel()
        self.model.setStringList(self.passnames)

        self.completer = QtGui.QCompleter()
        self.completer.setModel(self.model)

        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.move(20, 40)
        self.lineEdit.setCompleter(self.completer)

        self.pushButtonSearch = QtGui.QPushButton(self)
        self.pushButtonSearch.setText("Search Pass")
        self.pushButtonSearch.clicked.connect(self.search)
        self.pushButtonSearch.setAutoDefault(True)

        self.lineEdit.returnPressed.connect(self.pushButtonSearch.click)

        self.pushButtonCopy = QtGui.QPushButton(self)
        self.pushButtonCopy.setText("Copy Pass")
        self.pushButtonCopy.clicked.connect(self.on_pushButtonCopy_clicked)
        self.pushButtonCopy.setEnabled(False)
        self.pushButtonCopy.setAutoDefault(True)

        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.gridLayout.addWidget(self.label, 1, 1, 1, 2)
        self.gridLayout.addWidget(self.pushButtonSearch, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.pushButtonCopy, 2, 2, 1, 1)
        self.setLayout(self.gridLayout)

        self.lineEdit.setFocus()

    @QtCore.pyqtSlot()
    def search(self):
        """
        Looks for the title entered by user
          and defines behaviour depending on whether it exists or not
        """
        passwdname_written = self.lineEdit.text()
        if passwdname_written in self.passnames:
            self.label.setText("Ready to Copy")
            self.pushButtonCopy.setEnabled(True)
        else:
            self.label.setText("Nothing found, try again")
            self.pushButtonCopy.setEnabled(False)

    def on_pushButtonCopy_clicked(self):
        """
        Defines behaviour when user clicks on 'Copy' button
        """
        passwd_received = get_pass(self.lineEdit.text())
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(passwd_received)
        self.label.setText("Password copied to Clipboard")


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('QtVault')

    mainwin = MyWindow()
    mainwin.show()

    sys.exit(app.exec_())
