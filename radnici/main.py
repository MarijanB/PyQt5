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
        Main.resize(615, 791)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Main.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Main)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(9, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.listRadnika = QtWidgets.QListWidget(Main)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listRadnika.setFont(font)
        self.listRadnika.setObjectName("listRadnika")
        self.gridLayout.addWidget(self.listRadnika, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(308, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnNovi = QtWidgets.QPushButton(Main)
        self.btnNovi.setObjectName("btnNovi")
        self.horizontalLayout.addWidget(self.btnNovi)
        self.btnUcitaj = QtWidgets.QPushButton(Main)
        self.btnUcitaj.setObjectName("btnUcitaj")
        self.horizontalLayout.addWidget(self.btnUcitaj)
        self.btnIzbrisi = QtWidgets.QPushButton(Main)
        self.btnIzbrisi.setObjectName("btnIzbrisi")
        self.horizontalLayout.addWidget(self.btnIzbrisi)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 3)
        self.leftLayout = QtWidgets.QFormLayout()
        self.leftLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.leftLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.leftLayout.setLabelAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.leftLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.leftLayout.setObjectName("leftLayout")
        self.gridLayout.addLayout(self.leftLayout, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Moji radnici"))
        self.btnNovi.setText(_translate("Main", "Novi"))
        self.btnUcitaj.setText(_translate("Main", "Učitaj"))
        self.btnIzbrisi.setText(_translate("Main", "Izbriši"))
