# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCheckBox2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(429, 400)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_menu = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.label_menu.setFont(font)
        self.label_menu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_menu.setObjectName("label_menu")
        self.gridLayout.addWidget(self.label_menu, 0, 0, 1, 2)
        self.iceCramsCheckBox = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(13)
        self.iceCramsCheckBox.setFont(font)
        self.iceCramsCheckBox.setAcceptDrops(False)
        self.iceCramsCheckBox.setChecked(True)
        self.iceCramsCheckBox.setObjectName("iceCramsCheckBox")
        self.gridLayout.addWidget(self.iceCramsCheckBox, 1, 1, 1, 1)
        self.label_vrstaKreme = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.label_vrstaKreme.setFont(font)
        self.label_vrstaKreme.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_vrstaKreme.setObjectName("label_vrstaKreme")
        self.gridLayout.addWidget(self.label_vrstaKreme, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxChoclateChips = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.checkBoxChoclateChips.setFont(font)
        self.checkBoxChoclateChips.setObjectName("checkBoxChoclateChips")
        self.groupBoxIceCreams = QtWidgets.QButtonGroup(Dialog)
        self.groupBoxIceCreams.setObjectName("groupBoxIceCreams")
        self.groupBoxIceCreams.addButton(self.checkBoxChoclateChips)
        self.verticalLayout.addWidget(self.checkBoxChoclateChips)
        self.checkBoxCookieDough = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.checkBoxCookieDough.setFont(font)
        self.checkBoxCookieDough.setObjectName("checkBoxCookieDough")
        self.groupBoxIceCreams.addButton(self.checkBoxCookieDough)
        self.verticalLayout.addWidget(self.checkBoxCookieDough)
        self.checkBoxChoclateAlmond = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.checkBoxChoclateAlmond.setFont(font)
        self.checkBoxChoclateAlmond.setObjectName("checkBoxChoclateAlmond")
        self.groupBoxIceCreams.addButton(self.checkBoxChoclateAlmond)
        self.verticalLayout.addWidget(self.checkBoxChoclateAlmond)
        self.checkBoxRockyRoad = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.checkBoxRockyRoad.setFont(font)
        self.checkBoxRockyRoad.setObjectName("checkBoxRockyRoad")
        self.groupBoxIceCreams.addButton(self.checkBoxRockyRoad)
        self.verticalLayout.addWidget(self.checkBoxRockyRoad)
        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 1)
        self.drinksCheckBox = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(13)
        self.drinksCheckBox.setFont(font)
        self.drinksCheckBox.setChecked(True)
        self.drinksCheckBox.setObjectName("drinksCheckBox")
        self.gridLayout.addWidget(self.drinksCheckBox, 3, 1, 1, 1)
        self.label_pice = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.label_pice.setFont(font)
        self.label_pice.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_pice.setObjectName("label_pice")
        self.gridLayout.addWidget(self.label_pice, 4, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBoxCoffee = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.checkBoxCoffee.setFont(font)
        self.checkBoxCoffee.setObjectName("checkBoxCoffee")
        self.groupBoxDrinks = QtWidgets.QButtonGroup(Dialog)
        self.groupBoxDrinks.setObjectName("groupBoxDrinks")
        self.groupBoxDrinks.addButton(self.checkBoxCoffee)
        self.verticalLayout_2.addWidget(self.checkBoxCoffee)
        self.checkBoxSoda = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.checkBoxSoda.setFont(font)
        self.checkBoxSoda.setObjectName("checkBoxSoda")
        self.groupBoxDrinks.addButton(self.checkBoxSoda)
        self.verticalLayout_2.addWidget(self.checkBoxSoda)
        self.checkBoxTea = QtWidgets.QCheckBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.checkBoxTea.setFont(font)
        self.checkBoxTea.setObjectName("checkBoxTea")
        self.groupBoxDrinks.addButton(self.checkBoxTea)
        self.verticalLayout_2.addWidget(self.checkBoxTea)
        self.gridLayout.addLayout(self.verticalLayout_2, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_menu.setText(_translate("Dialog", "Menu"))
        self.iceCramsCheckBox.setText(_translate("Dialog", "Ice Creams"))
        self.label_vrstaKreme.setText(_translate("Dialog", "Odaberi vrstu kreme"))
        self.checkBoxChoclateChips.setText(_translate("Dialog", "Mint Choclate Chips $4"))
        self.checkBoxCookieDough.setText(_translate("Dialog", "Cookie Dough $2"))
        self.checkBoxChoclateAlmond.setText(_translate("Dialog", "Choclate Almond $3"))
        self.checkBoxRockyRoad.setText(_translate("Dialog", "Rocky Road $5"))
        self.drinksCheckBox.setText(_translate("Dialog", "Drinks"))
        self.label_pice.setText(_translate("Dialog", "Odaberi piće"))
        self.checkBoxCoffee.setText(_translate("Dialog", "Coffee $2"))
        self.checkBoxSoda.setText(_translate("Dialog", "Soda $3"))
        self.checkBoxTea.setText(_translate("Dialog", "Tea $1"))
