from PyQt5.QtWidgets import *
from main import *
from dodajRadnike import *
import sys, os
import sqlite3
from PIL import Image

con = sqlite3.connect("radnici.db")
cur = con.cursor()
defaultImg = "person-male.png"


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.ui.btnNovi.clicked.connect(self.addRadnici)

        self.show()

    def addRadnici(self):
        self.noviRadnik = DodajRadnike()
        self.close()


class DodajRadnike(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DodajRadnike()
        self.ui.setupUi(self)
        self.ui.btnPretraziSliku.clicked.connect(self.dodajSliku)
        self.ui.btnDodaj.clicked.connect(self.dodajRadnika)

        self.show()

    def dodajSliku(self):
        global defaultImg
        size = (128, 128)
        self.fileName, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image Files (*.jpg *.png)')
        if ok:
            defaultImg = os.path.basename(self.fileName)
            img = Image.open(self.fileName)

            img = img.resize(size)
            img.save("bazaSlika/{}".format(defaultImg))

    def dodajRadnika(self):
        global defaultImg
        Ime = self.ui.lineEditIme.text()
        prezime = self.ui.lineEditPrezime.text()
        telefon = self.ui.lineEditTelefon.text()
        email = self.ui.lineEditEmail.text()
        slika = defaultImg
        adresa = self.ui.textEditAdresa.toPlainText()
        if Ime and prezime and telefon != "":
            try:
                query = "INSERT INTO radnici (Ime,prezime,telefon,email,slika,adresa) VALUES(?,?,?,?,?,?)"
                cur.execute(query, (Ime, prezime, telefon, email, slika, adresa))
                con.commit()
                QMessageBox.information(self, "Success", "Osoba je dodana")
                self.close()
                self.main =MyWindow()
            except:
                QMessageBox(self, 'Warning', 'Osoba nije dodata u bazu podataka')

        else:
            QMessageBox.information(self, 'Warning', 'Polja nisu ispunjena')

    def closeEvent(self,event):
        self.main =MyWindow()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())
