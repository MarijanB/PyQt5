# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoInputDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(761, 114)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditCountry = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.lineEditCountry.setFont(font)
        self.lineEditCountry.setObjectName("lineEditCountry")
        self.horizontalLayout.addWidget(self.lineEditCountry)
        self.pushButtonCountry = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(15)
        self.pushButtonCountry.setFont(font)
        self.pushButtonCountry.setObjectName("pushButtonCountry")
        self.horizontalLayout.addWidget(self.pushButtonCountry)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your Country"))
        self.pushButtonCountry.setText(_translate("Dialog", "Choose Country"))
