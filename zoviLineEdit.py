from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

class MyForm(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('demoLineEdit.ui',self)
        self.buttonClickMe.clicked.connect(self.dispmessage)

    def dispmessage(self):
        self.label.setText("Hello " + self.lineEditName.text())

if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())