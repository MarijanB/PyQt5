import sys
from PyQt5.QtWidgets import *
from demoRadioGumb1 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButtonFirstClass.toggled.connect(self.dispFare)
        self.ui.radioButtonBusinessClass.toggled.connect(self.dispFare)
        self.ui.radioButtonEconomyClass.toggled.connect(self.dispFare)
        self.show()

    def dispFare(self):
        cijena = 0
        if self.ui.radioButtonFirstClass.isChecked() == True :
            cijena = 150
        if self.ui.radioButtonBusinessClass.isChecked() == True :
            cijena = 125

        if self.ui.radioButtonEconomyClass.isChecked() == True :
            cijena = 100

        self.ui.labelFare.setText("Air Fare is "+str(cijena))



if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
