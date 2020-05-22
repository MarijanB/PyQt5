# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(765, 608)
        self.gridLayout = QtWidgets.QGridLayout(Main)
        self.gridLayout.setObjectName("gridLayout")
        self.btnIzbrisi = QtWidgets.QPushButton(Main)
        self.btnIzbrisi.setObjectName("btnIzbrisi")
        self.gridLayout.addWidget(self.btnIzbrisi, 1, 2, 1, 1)
        self.btnUcitaj = QtWidgets.QPushButton(Main)
        self.btnUcitaj.setObjectName("btnUcitaj")
        self.gridLayout.addWidget(self.btnUcitaj, 1, 1, 1, 1)
        self.btnNovi = QtWidgets.QPushButton(Main)
        self.btnNovi.setObjectName("btnNovi")
        self.gridLayout.addWidget(self.btnNovi, 1, 0, 1, 1)
        self.listRadnika = QtWidgets.QListWidget(Main)
        self.listRadnika.setObjectName("listRadnika")
        self.gridLayout.addWidget(self.listRadnika, 0, 1, 1, 2)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Moji radnici"))
        self.btnIzbrisi.setText(_translate("Main", "Izbriši"))
        self.btnUcitaj.setText(_translate("Main", "Učitaj"))
        self.btnNovi.setText(_translate("Main", "Novi"))
