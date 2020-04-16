# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(527, 288)
        self.gridLayout_3 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelFirstNumber = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.labelFirstNumber.setFont(font)
        self.labelFirstNumber.setObjectName("labelFirstNumber")
        self.gridLayout.addWidget(self.labelFirstNumber, 0, 0, 1, 1)
        self.lineEditFirstNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditFirstNumber.setObjectName("lineEditFirstNumber")
        self.gridLayout.addWidget(self.lineEditFirstNumber, 0, 1, 1, 1)
        self.labelSecondNumber = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.labelSecondNumber.setFont(font)
        self.labelSecondNumber.setObjectName("labelSecondNumber")
        self.gridLayout.addWidget(self.labelSecondNumber, 1, 0, 1, 1)
        self.lineEditSecondNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditSecondNumber.setObjectName("lineEditSecondNumber")
        self.gridLayout.addWidget(self.lineEditSecondNumber, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonPlus = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButtonPlus.setFont(font)
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.gridLayout_2.addWidget(self.pushButtonPlus, 0, 0, 1, 1)
        self.pushButtonSubtract = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButtonSubtract.setFont(font)
        self.pushButtonSubtract.setObjectName("pushButtonSubtract")
        self.gridLayout_2.addWidget(self.pushButtonSubtract, 0, 1, 1, 1)
        self.pushButtonMultiply = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButtonMultiply.setFont(font)
        self.pushButtonMultiply.setObjectName("pushButtonMultiply")
        self.gridLayout_2.addWidget(self.pushButtonMultiply, 0, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.labelResult = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.labelResult.setFont(font)
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.gridLayout_3.addWidget(self.labelResult, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "demoCalculator"))
        self.labelFirstNumber.setText(_translate("Dialog", "Unesi prvi broj"))
        self.labelSecondNumber.setText(_translate("Dialog", "Unesi drugi broj"))
        self.pushButtonPlus.setText(_translate("Dialog", "+"))
        self.pushButtonSubtract.setText(_translate("Dialog", "-"))
        self.pushButtonMultiply.setText(_translate("Dialog", "x"))
        self.pushButton_3.setText(_translate("Dialog", "/"))
