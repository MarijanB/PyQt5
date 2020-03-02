from PyQt5 import QtWidgets, QtCore
import sys,time

class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(1,21):
            self.sleep(3)
            self.mysignal.emit(f'i = {i}')

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel('Pritisni tipku za pokretanje procesa')
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.button = QtWidgets.QPushButton('Pokreni proces')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.mythread = MyThread()  #Objekt klase
        self.button.clicked.connect(self.onClicked)
        self.mythread.started.connect(self.onStarted)
        self.mythread.finished.connect(self.onFinished)
        self.mythread.mysignal.connect(self.onChange,QtCore.Qt.QueuedConnection)


    def onClicked(self):
        self.button.setDisabled(True)   #neaktivni gumb
        self.mythread.start()           #pokrećem proces

    def onStarted(self):
        self.label.setText('Pozivam metodu onStarted()')

    def onFinished(self):       # zovem pri završetku procesa
        self.label.setText('Zovem metodu onFinished()')
        self.button.setDisabled(False)  #Gumb postaje aktivan

    def onChange(self,s):
        self.label.setText(s)

if __name__ =='__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow()
    w.setWindowTitle('Upotreba klase QThread')
    w.resize(300,70)
    w.show()
    sys.exit(app.exec_())