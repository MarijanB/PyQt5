from PyQt5.QtGui import *
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
        self.getRadnici()
        self.displayFirstRecord()
        self.ui.btnNovi.clicked.connect(self.addRadnici)
        self.ui.listRadnika.itemClicked.connect(self.singleClick)


        self.show()

    def addRadnici(self):
        self.noviRadnik = DodajRadnike()
        self.close()

    def getRadnici(self):
        query = "SELECT id,Ime,prezime FROM radnici"
        radnici = cur.execute(query).fetchall()
        for radnik in radnici:
            self.ui.listRadnika.addItem(str(radnik[0]) + "-" + radnik[1] +" " + radnik[2])

    def displayFirstRecord(self):
        query = "SELECT * FROM radnici ORDER BY ROWid ASC LIMIT 1"
        radnik = cur.execute(query).fetchone()
        slika = QLabel()
        slika.setPixmap(QPixmap("bazaSlika/" + radnik[5]))
        Ime = QLabel(radnik[1])
        prezime = QLabel(radnik[2])
        telefon = QLabel(radnik[3])
        email = QLabel(radnik[4])
        adresa = QLabel(radnik[6])
        self.ui.leftLayout.setVerticalSpacing(20)
        self.ui.leftLayout.addRow(" ",slika)
        self.ui.leftLayout.addRow("Ime: ", Ime)
        self.ui.leftLayout.addRow("Prezime :", prezime)
        self.ui.leftLayout.addRow("telefon :", telefon)
        self.ui.leftLayout.addRow("Email :", email)
        self.ui.leftLayout.addRow("Adresa:", adresa)

    def singleClick(self):
        for i in reversed(range(self.ui.leftLayout.count())):
            widget = self.ui.leftLayout.takeAt(i).widget()

            if widget is not None:
                widget.deleteLater()

        radnik = self.ui.listRadnika.currentItem().text()
        id =radnik.split("-")[0]
        query =("SELECT * FROM radnici WHERE id=?")
        osoba = cur.execute(query,(id,)).fetchone()
        slika = QLabel()
        slika.setPixmap(QPixmap("bazaSlika/" + osoba[5]))
        Ime = QLabel(osoba[1])
        prezime = QLabel(osoba[2])
        telefon = QLabel(osoba[3])
        email = QLabel(osoba[4])
        adresa = QLabel(osoba[6])
        self.ui.leftLayout.setVerticalSpacing(20)
        self.ui.leftLayout.addRow(" ", slika)
        self.ui.leftLayout.addRow("Ime: ", Ime)
        self.ui.leftLayout.addRow("Prezime :", prezime)
        self.ui.leftLayout.addRow("telefon :", telefon)
        self.ui.leftLayout.addRow("Email :", email)
        self.ui.leftLayout.addRow("Adresa:", adresa)



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
            slika = Image.open(self.fileName)

            slika = slika.resize(size)
            slika.save("bazaSlika/{}".format(defaultImg))

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
