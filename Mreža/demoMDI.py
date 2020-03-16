# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoMDI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")
        self.subwindow = QtWidgets.QWidget()
        self.subwindow.setObjectName("subwindow")
        self.label = QtWidgets.QLabel(self.subwindow)
        self.label.setGeometry(QtCore.QRect(30, 30, 149, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.subwindow_2 = QtWidgets.QWidget()
        self.subwindow_2.setObjectName("subwindow_2")
        self.label_2 = QtWidgets.QLabel(self.subwindow_2)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 176, 23))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 21))
        self.menubar.setObjectName("menubar")
        self.menuSubWindow_Wiew = QtWidgets.QMenu(self.menubar)
        self.menuSubWindow_Wiew.setObjectName("menuSubWindow_Wiew")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTabbed_Wiew = QtWidgets.QAction(MainWindow)
        self.actionTabbed_Wiew.setObjectName("actionTabbed_Wiew")
        self.actionCascade_View = QtWidgets.QAction(MainWindow)
        self.actionCascade_View.setObjectName("actionCascade_View")
        self.actionTile_View = QtWidgets.QAction(MainWindow)
        self.actionTile_View.setObjectName("actionTile_View")
        self.actionSubWindow_View = QtWidgets.QAction(MainWindow)
        self.actionSubWindow_View.setObjectName("actionSubWindow_View")
        self.menuSubWindow_Wiew.addAction(self.actionSubWindow_View)
        self.menuSubWindow_Wiew.addAction(self.actionTabbed_Wiew)
        self.menuSubWindow_Wiew.addAction(self.actionCascade_View)
        self.menuSubWindow_Wiew.addAction(self.actionTile_View)
        self.menubar.addAction(self.menuSubWindow_Wiew.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.subwindow.setWindowTitle(_translate("MainWindow", "Subwindow"))
        self.label.setText(_translate("MainWindow", "First sub window"))
        self.subwindow_2.setWindowTitle(_translate("MainWindow", "Subwindow"))
        self.label_2.setText(_translate("MainWindow", "Second sub window"))
        self.menuSubWindow_Wiew.setTitle(_translate("MainWindow", "Windows"))
        self.actionTabbed_Wiew.setText(_translate("MainWindow", "Tabbed Wiew"))
        self.actionCascade_View.setText(_translate("MainWindow", "Cascade View"))
        self.actionTile_View.setText(_translate("MainWindow", "Tile View"))
        self.actionSubWindow_View.setText(_translate("MainWindow", "SubWindow View"))
