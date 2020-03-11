# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoBrowser.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(687, 589)
        font = QtGui.QFont()
        font.setPointSize(15)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditURL = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEditURL.setFont(font)
        self.lineEditURL.setObjectName("lineEditURL")
        self.horizontalLayout.addWidget(self.lineEditURL)
        self.pushButtonGo = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButtonGo.setFont(font)
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.horizontalLayout.addWidget(self.pushButtonGo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter URL"))
        self.pushButtonGo.setText(_translate("Dialog", "to Go"))
from PyQt5 import QtWebEngineWidgets
