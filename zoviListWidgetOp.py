from PyQt5.QtWidgets import *
from demoListWidgetOp import *
import sys

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.listWidget.addItem('sladoled')
        self.ui.listWidget.addItem('soda')
        self.ui.listWidget.addItem('kava')
        self.ui.listWidget.addItem('čokolada')

        self.ui.psuhButtonAdd.clicked.connect(self.addlist)
        self.ui.pushButtonEdit.clicked.connect(self.editList)
        self.ui.pushButtonDelete.clicked.connect(self.delitem)
        self.ui.pushButton_4.clicked.connect(self.delAllItems)



        self.show()

    def addlist(self):
        self.ui.listWidget.addItem(self.ui.lineEdit.text())
        self.ui.lineEdit.setText('')
        self.ui.lineEdit.setFocus()

    def editList(self):
        row = self.ui.listWidget.currentRow()
        newtext, ok =QInputDialog.getText(self,"Enter new text","Enter new text")
        if ok and (len(newtext) !=0):
            self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
            self.ui.listWidget.insertItem(row,QListWidgetItem(newtext))

    def delitem(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

    def delAllItems(self):
        self.ui.listWidget.clear()



if __name__ =='__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())