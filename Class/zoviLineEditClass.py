import sys

from LineEditClass import *
from PyQt5.QtWidgets import *

class Student:
    ime = ""
    def __init__(self,ime):
        self.ime = ime
    def printIme(self):
        return self.ime


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ButtonClickMe.clicked.connect(self.poruka)


        self.show()

    def poruka(self):
        studentObj = Student(self.ui.lineEditName.text())
        self.ui.abelResponse.setText(f'Pozdrav {studentObj.printIme()}')


if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())