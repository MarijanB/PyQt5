import sys
from PyQt5.QtWidgets import *
from demoChekBox1 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.checkBox_sir.stateChanged.connect(self.ukupnaCijena)
        self.ui.checkBox_masline.stateChanged.connect(self.ukupnaCijena)
        self.ui.checkBox_sos.stateChanged.connect(self.ukupnaCijena)
        self.show()

    def ukupnaCijena(self):
        cijena = 10
        if self.ui.checkBox_sir.isChecked() == True:
            cijena = cijena + 1
        if self.ui.checkBox_masline.isChecked() == True:
            cijena = cijena + 1
        if self.ui.checkBox_sos.isChecked() == True:
            cijena = cijena + 2

        self.ui.label_izlaznacijena.setText(f"Cijena pizze iznosi {cijena} $")

if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())