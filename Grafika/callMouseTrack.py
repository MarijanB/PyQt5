import sys
from PyQt5.QtWidgets import *
from  demoMousetrack import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.setMouseTracking(True)
        self.ui.setupUi(self)

        self.show()

    def mouseMoveEvent(self,event):
        x = event.x()
        y = event.y()

        text = f"x: {x}, y: {y} "
        self.ui.label_2.setText(text)


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())