import sqlite3
import sys
from PyQt5.QtWidgets import *
from sqlite3 import Error
from demoCreateTable import *
tableDefinition = ""

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButtonCreateTable.clicked.connect(self.createTable)
        self.ui.pushButtonAddColumn.clicked.connect(self.addColumns)




        self.show()

    def addColumns(self):
        global tableDefinition
        if tableDefinition =="":
            tableDefinition = "CREATE TABLE IF NOT EXISTS " + \
                              self.ui.lineEditTableName.text() + " (" \
                              + self.ui.lineEditColumnName.text()+\
                                " " + self.ui.ComboBoxDataType.itemText(self.ui.ComboBoxDataType.currentIndex())

        else:
            tableDefinition += "," + self.ui.lineEditColumnName.text() + " " + self.ui.ComboBoxDataType.itemText(
                self.ui.ComboBoxDataType.currentIndex())
            self.ui.lineEditColumnName.setText("")
            self.ui.lineEditColumnName.setFocus()

    def createTable(self):
        global tableDefinition
        try:
            conn = sqlite3.connect(self.ui.lineEditDBName.text() + ".db")
            self.ui.labelResponse.setText("Database is connected")
            c = conn.cursor()
            tableDefinition += ") ;"
            c.execute(tableDefinition)
            self.ui.labelResponse.setText("Table is successfully created")

        except Error as e:
            self.ui.labelResponse.setText("Pogreška, tablica nije kreirana.")
        finally:
            conn.close()

if __name__ == '__main__':
    app =QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
