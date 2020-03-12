# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoClient.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(712, 483)
        font = QtGui.QFont()
        font.setPointSize(15)
        Dialog.setFont(font)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textEditMessages = QtWidgets.QTextEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.textEditMessages.setFont(font)
        self.textEditMessages.setObjectName("textEditMessages")
        self.gridLayout.addWidget(self.textEditMessages, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.lineEditMessage = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEditMessage.setFont(font)
        self.lineEditMessage.setObjectName("lineEditMessage")
        self.gridLayout.addWidget(self.lineEditMessage, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Client"))
        self.pushButton.setText(_translate("Dialog", "Send"))
