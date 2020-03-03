import sys

from demoStudentClass import *
from PyQt5.QtWidgets import *

class Student:
    name = ""
    code = ""
    def __init__(self,code,name):
        self.code = code
        self.name = name
    def getCode(self):
        return self.code

    def getName(self):
        return self.name


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ButtonClickMe.clicked.connect(self.poruka)


        self.show()

    def poruka(self):
        studentObj = Student(self.ui.lineEditCode.text(),self.ui.lineEditName.text())
        self.ui.abelResponse.setText(f'Code: {studentObj.getCode()}, Name: {studentObj.getName()}')


if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())