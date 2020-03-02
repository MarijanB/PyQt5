from PyQt5 import QtWidgets, QtCore
import sys,time

class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()

        self.running = False
        self.count = 0

    def run(self):
        self.running = True
        while self.running:
            self.count += 1
            self.mysignal.emit(f'count = {self.count}')
            self.sleep(1)


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel('Pritisni tipku za pokretanje procesa')
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.btnStart = QtWidgets.QPushButton('Pokreni proces')
        self.btnStop = QtWidgets.QPushButton('Zaustavi proces')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnStart)
        self.vbox.addWidget(self.btnStop)
        self.setLayout(self.vbox)
        self.mythread = MyThread()  #Objekt klase
        self.btnStart.clicked.connect(self.on_start)
        self.btnStop.clicked.connect(self.on_stop)

        self.mythread.mysignal.connect(self.on_change,QtCore.Qt.QueuedConnection)


    def on_start(self):
        if not self.mythread.isRunning():
            self.mythread.start()           #pokrećem proces

    def on_stop(self):
        self.mythread.running = False       #mijenjam flag izvršenja

    def on_change(self,s):
        self.label.setText(s)

    def closeEvent(self,event):             #Poziva se kod zatvorenog prozora
        self.hide()                         #Sakriva prozor
        self.mythread.running = False       #Mijenja flag izvršenja
        self.mythread.wait(5000)            #Daje vrijeme zatvaranja
        event.accept()                      #Zatvara prozor

if __name__ =='__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow()
    w.setWindowTitle('Pokretanje i zaustavljanje procesa')
    w.resize(300,70)
    w.show()
    sys.exit(app.exec_())