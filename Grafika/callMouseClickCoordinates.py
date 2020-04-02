import sys
from PyQt5.QtWidgets import *
from  demoMouseClicks import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()

        self.ui.setupUi(self)

        self.show()

    def mousePressEvent(self, event):
        if event.buttons() and QtCore.Qt.LeftButton:
            x = event.x()
            y = event.y()
            text =f"x: {x}, y: {y}"
            self.ui.labelPress.setText('Mouse button pressed' + text)

    def mouseReleaseEvent(self, event):
        x = event.x()
        y = event.y()
        text =f"x: {x}, y: {y}"
        self.ui.label_3.setText('Mouse button released at' + text)
        self.update()



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())