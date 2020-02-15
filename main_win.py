from PyQt5.QtWidgets import *
import  sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,300,500,300)
        self.menu = self.menuBar()
        self.file = self.menu.addMenu('&File')
        self.settings = self.menu.addMenu('&settings')
        self.exit = QAction('exit',self)
        self.settings_win = QAction('settings',self)
        self.file.addAction(self.exit)
        self.settings.addAction(self.settings_win)


if __name__ =='__main__':
    app = QApplication(sys.argv)
    myApp = MyWindow()
    myApp.show()
    sys.exit(app.exec_())
