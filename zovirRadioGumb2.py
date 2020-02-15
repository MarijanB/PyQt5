import sys
from PyQt5.QtWidgets import *
from demoRadioGumb2 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radioButton_M.toggled.connect(self.dispSelected)
        self.ui.radioButton_L.toggled.connect(self.dispSelected)
        self.ui.radioButton_XL.toggled.connect(self.dispSelected)
        self.ui.radioButton_XXL.toggled.connect(self.dispSelected)

        self.ui.radioButton_DebitCreditCard.toggled.connect(self.dispSelected)
        self.ui.radioButton_NetBanking.toggled.connect(self.dispSelected)
        self.ui.radioButton_CashOnDelivery.toggled.connect(self.dispSelected)

        self.show()

    def dispSelected(self):
        selected1 = ""
        selected2 = ""

        if self.ui.radioButton_M.isChecked() == True:
            selected1 = "Medium"

        if self.ui.radioButton_L.isChecked() == True:
            selected1 = "Large"

        if self.ui.radioButton_XL.isChecked() == True:
            selected1 = "Extra Large"

        if self.ui.radioButton_XXL.isChecked() == True:
            selected1 = "Extra Extra Large"

        if self.ui.radioButton_DebitCreditCard.isChecked() == True:
            selected2 = "Debit/CreditCard"

        if self.ui.radioButton_NetBanking.isChecked() == True:
            selected2 = "Net Banking"

        if self.ui.radioButton_CashOnDelivery.isChecked() == True:
            selected2 = "Cash On Delivery"

        self.ui.label_3.setText("Vi ste odabrali majicu veličine " + selected1 + "a metoda plačanja je " + selected2)






if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())