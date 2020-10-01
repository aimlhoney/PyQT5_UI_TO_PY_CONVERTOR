# -*- coding: utf-8 -*-
import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog

from convertor_ui import Ui_MainWindow


class Convertor(QMainWindow):
    def __init__(self):
        super(Convertor, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialize()

    def initialize(self):
        pass
        self.setWindowTitle("UI to PYConvertor")
        self.centralWidget()
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton.clicked.connect(self.tapSelectFolder)
        self.ui.pushButton_2.clicked.connect(self.convertFile)
        self.ui.lineEdit.setEnabled(False)

    def tapSelectFolder(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.lineEdit.setText(file)
        self.ui.pushButton_2.setEnabled(True)

    def convertFile(self):
        os.chdir(self.ui.lineEdit.text())
        files = self.getFileName()
        for file in files:
            name = file.split('.')
            if len(name) == 2 and name[1] == 'ui':
                self.ui.textEdit.append(str(self.runcommand('pyuic5 -o ' + name[0] + '.py ' + file)))


    def runcommand(self, cmd):
        try:
            output = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
            out, err = output.communicate()
            if out is None:
                return err
            if err is None:
                return "File is converted."
        except:
            return "Success"

    def getFileName(self):
        return os.listdir()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Convertor()
    window.show()
    sys.exit(app.exec_())
