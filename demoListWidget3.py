# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidget3.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(837, 414)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditFoodItem = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.lineEditFoodItem.setFont(font)
        self.lineEditFoodItem.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEditFoodItem.setObjectName("lineEditFoodItem")
        self.horizontalLayout.addWidget(self.lineEditFoodItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.pushButtonAdd.setFont(font)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.horizontalLayout_2.addWidget(self.pushButtonAdd)
        spacerItem1 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.listWidgetSelectedItems = QtWidgets.QListWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(15)
        self.listWidgetSelectedItems.setFont(font)
        self.listWidgetSelectedItems.setObjectName("listWidgetSelectedItems")
        self.gridLayout.addWidget(self.listWidgetSelectedItems, 0, 1, 2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Demo list widget 3"))
        self.label.setText(_translate("Dialog", "Vaša omiljena hrana je:"))
        self.pushButtonAdd.setText(_translate("Dialog", "Dodaj listi"))
