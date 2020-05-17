# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rps_game.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(550, 500)
        Window.setMinimumSize(QtCore.QSize(55, 50))
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.scoreComputerText = QtWidgets.QLabel(self.centralwidget)
        self.scoreComputerText.setGeometry(QtCore.QRect(40, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scoreComputerText.setFont(font)
        self.scoreComputerText.setObjectName("scoreComputerText")
        self.scorePlayerText = QtWidgets.QLabel(self.centralwidget)
        self.scorePlayerText.setGeometry(QtCore.QRect(300, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.scorePlayerText.setFont(font)
        self.scorePlayerText.setObjectName("scorePlayerText")
        self.imageComputer = QtWidgets.QLabel(self.centralwidget)
        self.imageComputer.setGeometry(QtCore.QRect(60, 130, 121, 101))
        self.imageComputer.setText("")
        self.imageComputer.setPixmap(QtGui.QPixmap("slike/rock.png"))
        self.imageComputer.setObjectName("imageComputer")
        self.imagePlayer = QtWidgets.QLabel(self.centralwidget)
        self.imagePlayer.setGeometry(QtCore.QRect(350, 130, 121, 101))
        self.imagePlayer.setText("")
        self.imagePlayer.setPixmap(QtGui.QPixmap("slike/rock.png"))
        self.imagePlayer.setObjectName("imagePlayer")
        self.imageGame = QtWidgets.QLabel(self.centralwidget)
        self.imageGame.setGeometry(QtCore.QRect(220, 160, 71, 41))
        self.imageGame.setText("")
        self.imageGame.setPixmap(QtGui.QPixmap("slike/game.png"))
        self.imageGame.setAlignment(QtCore.Qt.AlignCenter)
        self.imageGame.setObjectName("imageGame")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(80, 280, 101, 41))
        self.btnStart.setObjectName("btnStart")
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setGeometry(QtCore.QRect(360, 280, 101, 41))
        self.btnStop.setObjectName("btnStop")
        Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Rock Paper Scrissors Game"))
        self.scoreComputerText.setText(_translate("Window", "Computer Score :"))
        self.scorePlayerText.setText(_translate("Window", "Your Score :"))
        self.btnStart.setText(_translate("Window", "Start"))
        self.btnStop.setText(_translate("Window", "Stop"))
