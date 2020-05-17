import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from rps_game import *
from random import randint

computerScore= 0
playerScore = 0

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Window()
        self.ui.setupUi(self)




        self.ui.btnStart.clicked.connect(self.start)
        self.ui.btnStop.clicked.connect(self.stop)
        self.timer=QTimer(self)
        self.timer.setInterval(100)

        self.timer.timeout.connect(self.playGame)



        self.show()

    def start(self):
        self.timer.start()

    def playGame(self):
        self.rndComputer = randint(1,3)
        self.rndPlayer = randint(1, 3)
        if self.rndComputer==1:
            self.ui.imageComputer.setPixmap(QPixmap('slike/rock.png'))

        elif self.rndComputer==2:
            self.ui.imageComputer.setPixmap(QPixmap('slike/paper.png'))

        else:
            self.ui.imageComputer.setPixmap(QPixmap('slike/scissors.png'))


        if self.rndPlayer == 1:
            self.ui.imagePlayer.setPixmap(QPixmap('slike/rock.png'))

        elif self.rndPlayer == 2:
            self.ui.imagePlayer.setPixmap(QPixmap('slike/paper.png'))

        else:
            self.ui.imagePlayer.setPixmap(QPixmap('slike/scissors.png'))


    def stop(self):
        global computerScore
        global playerScore
        self.timer.stop()

        if self.rndComputer ==1 and self.rndPlayer==1:
            mbox = QMessageBox.information(self,"Information","Draw Game")

        elif self.rndComputer ==1 and self.rndPlayer==2:
            mbox = QMessageBox.information(self,"Information","Vi ste pobijedili")
            playerScore +=1
            self.ui.scorePlayerText.setText(f"Your Score: {playerScore}")

        elif self.rndComputer ==1 and self.rndPlayer==3:
            mbox = QMessageBox.information(self,"Information","kompjurer je pobijedio")
            computerScore +=1
            self.ui.scoreComputerText.setText(f"Your Score: {computerScore}")

        elif self.rndComputer == 2 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, "Information", "kompjurer je pobijedio")
            computerScore += 1
            self.ui.scoreComputerText.setText(f"Your Score: {computerScore}")

        elif self.rndComputer ==2 and self.rndPlayer==2:
            mbox = QMessageBox.information(self,"Information","Draw Game")

        elif self.rndComputer == 2 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, "Information", "Vi ste pobijedili")
            playerScore += 1
            self.ui.scorePlayerText.setText(f"Your Score: {playerScore}")

        elif self.rndComputer == 3 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, "Information", "Vi ste pobijedili")
            computerScore += 1
            self.ui.scoreComputerText.setText(f"Your Score: {playerScore}")

        elif self.rndComputer == 3 and self.rndPlayer == 2:
            mbox = QMessageBox.information(self, "Information", "kompjurer je pobijedio")
            computerScore += 1
            self.ui.scoreComputerText.setText(f"Your Score: {computerScore}")

        elif self.rndComputer ==3 and self.rndPlayer==3:
            mbox = QMessageBox.information(self,"Information","Draw Game")

        if int(computerScore)==3 or int(playerScore)==3:
            mbox = QMessageBox.information(self,"Information","Game Over")
            sys.exit()

if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.start()
    w.show()
    sys.exit(app.exec_())