import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *


class MyForm(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        Form, Base = uic.loadUiType('demoLineEdit.ui')
        self.ui = Form()
        self.ui.setupUi(self)
        self.ui.buttonClickMe.clicked.connect(self.dispmessage)

    def dispmessage(self):
        self.ui.label.setText("Hello " + self.ui.lineEditName.text())

if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())