from PyQt5.QtWidgets import *
from demoListWidget1 import *
import sys

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.listWidgetDiagnosis.itemClicked.connect(self.dispSelectedTest)


        self.show()

    def dispSelectedTest(self):
        self.ui.labelTest.setText(f'Vi ste odabrali {self.ui.listWidgetDiagnosis.currentItem().text()}')


if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())