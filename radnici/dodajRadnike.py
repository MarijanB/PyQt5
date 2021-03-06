# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dodajRadnike.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DodajRadnike(object):
    def setupUi(self, DodajRadnike):
        DodajRadnike.setObjectName("DodajRadnike")
        DodajRadnike.resize(367, 618)
        self.verticalLayout = QtWidgets.QVBoxLayout(DodajRadnike)
        self.verticalLayout.setObjectName("verticalLayout")
        self.naziv = QtWidgets.QLabel(DodajRadnike)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(24)
        self.naziv.setFont(font)
        self.naziv.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.naziv.setAlignment(QtCore.Qt.AlignCenter)
        self.naziv.setObjectName("naziv")
        self.verticalLayout.addWidget(self.naziv)
        self.dodajSliku = QtWidgets.QLabel(DodajRadnike)
        self.dodajSliku.setText("")
        self.dodajSliku.setPixmap(QtGui.QPixmap("slike/person-male.png"))
        self.dodajSliku.setAlignment(QtCore.Qt.AlignCenter)
        self.dodajSliku.setObjectName("dodajSliku")
        self.verticalLayout.addWidget(self.dodajSliku)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.imeLabel = QtWidgets.QLabel(DodajRadnike)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.imeLabel.setFont(font)
        self.imeLabel.setObjectName("imeLabel")
        self.gridLayout.addWidget(self.imeLabel, 0, 0, 1, 1)
        self.lineEditIme = QtWidgets.QLineEdit(DodajRadnike)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEditIme.setFont(font)
        self.lineEditIme.setObjectName("lineEditIme")
        self.gridLayout.addWidget(self.lineEditIme, 0, 1, 1, 1)
        self.prezimeLabel = QtWidgets.QLabel(DodajRadnike)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.prezimeLabel.setFont(font)
        self.prezimeLabel.setObjectName("prezimeLabel")
        self.gridLayout.addWidget(self.prezimeLabel, 1, 0, 1, 1)
        self.lineEditPrezime = QtWidgets.QLineEdit(DodajRadnike)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEditPrezime.setFont(font)
        self.lineEditPrezime.setObjectName("lineEditPrezime")
        self.gridLayout.addWidget(self.lineEditPrezime, 1, 1, 1, 1)
        self.telefonLabel = QtWidgets.QLabel(DodajRadnike)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.telefonLabel.setFont(font)
        self.telefonLabel.setObjectName("telefonLabel")
        self.gridLayout.addWidget(self.telefonLabel, 2, 0, 1, 1)
        self.lineEditTelefon = QtWidgets.QLineEdit(DodajRadnike)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEditTelefon.setFont(font)
        self.lineEditTelefon.setObjectName("lineEditTelefon")
        self.gridLayout.addWidget(self.lineEditTelefon, 2, 1, 1, 1)
        self.emailLabel = QtWidgets.QLabel(DodajRadnike)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName("emailLabel")
        self.gridLayout.addWidget(self.emailLabel, 3, 0, 1, 1)
        self.lineEditEmail = QtWidgets.QLineEdit(DodajRadnike)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEditEmail.setFont(font)
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.gridLayout.addWidget(self.lineEditEmail, 3, 1, 1, 1)
        self.slikaLabel = QtWidgets.QLabel(DodajRadnike)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.slikaLabel.setFont(font)
        self.slikaLabel.setObjectName("slikaLabel")
        self.gridLayout.addWidget(self.slikaLabel, 4, 0, 1, 1)
        self.btnPretraziSliku = QtWidgets.QPushButton(DodajRadnike)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnPretraziSliku.setFont(font)
        self.btnPretraziSliku.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.btnPretraziSliku.setObjectName("btnPretraziSliku")
        self.gridLayout.addWidget(self.btnPretraziSliku, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.formLayout.setObjectName("formLayout")
        self.adresaLabel = QtWidgets.QLabel(DodajRadnike)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.adresaLabel.setFont(font)
        self.adresaLabel.setObjectName("adresaLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.adresaLabel)
        self.textEditAdresa = QtWidgets.QTextEdit(DodajRadnike)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textEditAdresa.setFont(font)
        self.textEditAdresa.setObjectName("textEditAdresa")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEditAdresa)
        self.btnDodaj = QtWidgets.QPushButton(DodajRadnike)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btnDodaj.setFont(font)
        self.btnDodaj.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.btnDodaj.setObjectName("btnDodaj")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btnDodaj)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(DodajRadnike)
        QtCore.QMetaObject.connectSlotsByName(DodajRadnike)

    def retranslateUi(self, DodajRadnike):
        _translate = QtCore.QCoreApplication.translate
        DodajRadnike.setWindowTitle(_translate("DodajRadnike", "Dodaj radnike"))
        self.naziv.setText(_translate("DodajRadnike", "Dodaj radnika"))
        self.imeLabel.setText(_translate("DodajRadnike", "Ime :"))
        self.lineEditIme.setPlaceholderText(_translate("DodajRadnike", "Unesi ime radnika"))
        self.prezimeLabel.setText(_translate("DodajRadnike", "Prezime:"))
        self.lineEditPrezime.setPlaceholderText(_translate("DodajRadnike", "Unesi prezime radnika"))
        self.telefonLabel.setText(_translate("DodajRadnike", "Telefon :"))
        self.lineEditTelefon.setPlaceholderText(_translate("DodajRadnike", "Unesi broj telefona radnika"))
        self.emailLabel.setText(_translate("DodajRadnike", "Email:"))
        self.lineEditEmail.setPlaceholderText(_translate("DodajRadnike", "Unesi email radnika"))
        self.slikaLabel.setText(_translate("DodajRadnike", "Slika :"))
        self.btnPretraziSliku.setText(_translate("DodajRadnike", "Pretraži"))
        self.adresaLabel.setText(_translate("DodajRadnike", "Adresa :"))
        self.btnDodaj.setText(_translate("DodajRadnike", "Dodaj"))
