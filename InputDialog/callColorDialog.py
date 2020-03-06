import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from demoColorDialog import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        col = QColor(0,0,0)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.frameColor.setStyleSheet("QWidget {background-color: % s}" % col.name())
        self.ui.pushButtonColor.clicked.connect(self.dispColor)


        self.show()

    def dispColor(self):
        col =QColorDialog.getColor()
        if col.isValid():
            self.ui.frameColor.setStyleSheet("QWidget {background-color: % s}" % col.name())
            self.ui.label.setText("You have selected the color with code: " + str(col.name()))

if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())