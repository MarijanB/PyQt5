import sys
from PyQt5.QtWidgets import *

from demoScrollBar import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.horizontalScrollBarSugarLevel.valueChanged.connect(self.scrollhorizontal)
        self.ui.verticalScrollBarPulseRate.valueChanged.connect(self.scrollvertical)
        self.ui.horizontalSliderBloodPressure.valueChanged.connect(self.sliderhorizontal)
        self.ui.verticalSliderCholestrolLevel.valueChanged.connect(self.slidervertical)

        self.show()

    def scrollhorizontal(self,value):
        self.ui.lineEdit.setText(f'Nivo šećera : {str(value)}')

    def scrollvertical(self,value):
        self.ui.lineEdit.setText(f'Broj otkucaja srca : {str(value)}')

    def sliderhorizontal(self,value):
        self.ui.lineEdit.setText(f'Krvni tlak : {str(value)}')

    def slidervertical(self, value):
        self.ui.lineEdit.setText(f'Nivo kolesterola : {str(value)}')




if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())