# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoChekBox1.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(498, 333)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_RegularPizza = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.label_RegularPizza.setFont(font)
        self.label_RegularPizza.setObjectName("label_RegularPizza")
        self.gridLayout.addWidget(self.label_RegularPizza, 0, 0, 1, 1)
        self.label_selektiranjeDodataka = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.label_selektiranjeDodataka.setFont(font)
        self.label_selektiranjeDodataka.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_selektiranjeDodataka.setObjectName("label_selektiranjeDodataka")
        self.gridLayout.addWidget(self.label_selektiranjeDodataka, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_sir = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.checkBox_sir.setFont(font)
        self.checkBox_sir.setObjectName("checkBox_sir")
        self.verticalLayout.addWidget(self.checkBox_sir)
        self.checkBox_masline = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.checkBox_masline.setFont(font)
        self.checkBox_masline.setObjectName("checkBox_masline")
        self.verticalLayout.addWidget(self.checkBox_masline)
        self.checkBox_sos = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.checkBox_sos.setFont(font)
        self.checkBox_sos.setObjectName("checkBox_sos")
        self.verticalLayout.addWidget(self.checkBox_sos)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.label_izlaznacijena = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.label_izlaznacijena.setFont(font)
        self.label_izlaznacijena.setObjectName("label_izlaznacijena")
        self.gridLayout.addWidget(self.label_izlaznacijena, 2, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_RegularPizza.setText(_translate("Dialog", "Regular Pizza  $10"))
        self.label_selektiranjeDodataka.setText(_translate("Dialog", "Selektirajte ekstra dodatke"))
        self.checkBox_sir.setText(_translate("Dialog", "Ekstra sir      $1"))
        self.checkBox_masline.setText(_translate("Dialog", "Ekstra masline    $1"))
        self.checkBox_sos.setText(_translate("Dialog", "Ekstra sos  $2"))
        self.label_izlaznacijena.setText(_translate("Dialog", "TextLabel"))
