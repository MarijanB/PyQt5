import sys
from PyQt5.QtWidgets import *
from demoSpinner import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.spinBoxBookQty.editingFinished.connect(self.result1)
        self.ui.doubleSpinBox.editingFinished.connect(self.result2)

        self.show()

    def result1(self):
        if len(self.ui.lineEditBookPrice.text()) != 0:
            cijenaKnjige = int(self.ui.lineEditBookPrice.text())
        else:
            cijenaKnjige= 0

        ukupnaCijenaKnjige = self.ui.spinBoxBookQty.value() * cijenaKnjige

        self.ui.lineEditBookAmount.setText(str(ukupnaCijenaKnjige))

    def result2(self):
        if len(self.ui.lineEditSugarPrice.text()) != 0:
            cijenaSecera = float(self.ui.lineEditSugarPrice.text())
        else:
            cijenaSecera = 0

        ukupnaCijenaSecera = self.ui.doubleSpinBox.value() * cijenaSecera

        self.ui.lineEditSugarAmount.setText(str(round(ukupnaCijenaSecera,2)))

        ukupnaCijenaKnjige = int(self.ui.lineEditBookAmount.text())
        ukupnaCijena = ukupnaCijenaKnjige + ukupnaCijenaSecera
        self.ui.labelTotalAmount.setText(f"Ukupna cijena: {str(round(ukupnaCijena,2))}")





if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())