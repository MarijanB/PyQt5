import sys

from PyQt5.QtWidgets import *
from demoCheckBox2 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.checkBoxChoclateAlmond.stateChanged.connect(self.ukupnaCijena)
        self.ui.checkBoxChoclateChips.stateChanged.connect(self.ukupnaCijena)
        self.ui.checkBoxCookieDough.stateChanged.connect(self.ukupnaCijena)
        self.ui.checkBoxRockyRoad.stateChanged.connect(self.ukupnaCijena)
        self.ui.checkBoxCoffee.stateChanged.connect(self.ukupnaCijena)
        self.ui.checkBoxSoda.stateChanged.connect(self.ukupnaCijena)
        self.ui.checkBoxTea.stateChanged.connect(self.ukupnaCijena)

        self.show()

    def ukupnaCijena(self):
        cijena = 0
        if self.ui.checkBoxChoclateAlmond.isChecked()==True:
            cijena = cijena + 3
        if self.ui.checkBoxChoclateChips.isChecked()==True:
            cijena = cijena + 4
        if self.ui.checkBoxCookieDough.isChecked()==True:
            cijena = cijena + 2
        if self.ui.checkBoxRockyRoad.isChecked()==True:
            cijena = cijena + 5

        if self.ui.checkBoxCoffee.isChecked()==True:
            cijena = cijena + 2
        if self.ui.checkBoxSoda.isChecked()==True:
            cijena = cijena + 3
        if self.ui.checkBoxTea.isChecked()==True:
            cijena = cijena + 1

        self.ui.label_4.setText(f"Ukupna cijena je {cijena} $")


if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())