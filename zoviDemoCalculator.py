from PyQt5.QtWidgets import *
from demoCalculator import *
import sys
import math


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonPlus.clicked.connect(self.zbrajanje)
        self.ui.pushButtonSubtract.clicked.connect(self.oduzimanje)
        self.ui.pushButton_3.clicked.connect(self.dijeljenje)
        self.ui.pushButtonMultiply.clicked.connect(self.mnozenje)


        self.show()

    def zbrajanje(self):
        if len(self.ui.lineEditFirstNumber.text()) != 0 :
            a = float(self.ui.lineEditFirstNumber.text())
        else:
            a = 0

        if len(self.ui.lineEditSecondNumber.text()) != 0 :
            b = float(self.ui.lineEditSecondNumber.text())
        else:
            b = 0
        suma = a + b
        self.ui.labelResult.setText(f"Zbroj je {str(suma)}")

    def oduzimanje(self):
        if len(self.ui.lineEditFirstNumber.text()) != 0:
            a = float(self.ui.lineEditFirstNumber.text())
        else:
            a = 0

        if len(self.ui.lineEditSecondNumber.text()) != 0:
            b = float(self.ui.lineEditSecondNumber.text())
        else:
            b = 0
        razlika = a - b
        self.ui.labelResult.setText(f"Razlika je {str(razlika)}")

    def mnozenje(self):
        if len(self.ui.lineEditFirstNumber.text()) != 0:
            a = float(self.ui.lineEditFirstNumber.text())
        else:
            a = 0

        if len(self.ui.lineEditSecondNumber.text()) != 0:
            b = float(self.ui.lineEditSecondNumber.text())
        else:
            b = 0
        produkt = a * b
        self.ui.labelResult.setText(f"Produkt je {str(produkt)}")

    def dijeljenje(self):
        if len(self.ui.lineEditFirstNumber.text()) != 0:
            a = float(self.ui.lineEditFirstNumber.text())
        else:
            a = 0

        if len(self.ui.lineEditSecondNumber.text()) != 0:
            b = float(self.ui.lineEditSecondNumber.text())
        else:
            self.ui.labelResult.setText("Nemože se dijeliti s nulom")
        kvocijent =round(a/b,5)
        self.ui.labelResult.setText(f"Kvocijent je {str(kvocijent)}")






if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())