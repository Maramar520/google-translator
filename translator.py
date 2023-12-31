import GUI
import sys
import googletrans
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox

class Main(QtWidgets.QMainWindow, GUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.setupUi(self)
        self.plainTextEdit.clear()
        self.tambah_bahasa()

        self.pushButton.clicked.connect(self.terjemah)
        self.pushButton_2.clicked.connect(self.hapus)

    def tambah_bahasa(self):
        for x in googletrans.LANGUAGES.values():
            self.comboBox.addItem(x.capitalize())

            self.comboBox_2.addItem(x.capitalize())



    def terjemah(self):
        try:
            text_1 = self.plainTextEdit.toPlainText()
            lang_1 = self.comboBox.currentText()
            lang_2 = self.comboBox_2.currentText()

            penerjemah = googletrans.Translator()
            terjemah = penerjemah.translate(text_1, src=lang_1, dest=lang_2)
            self.textEdit_2.setText(terjemah.text)

        except Exception as e:
            self.error_message(e)

    def error_message(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle('Error')
        msg.setText(str(text))
        msg.exec_()

    def hapus(self):
        self.plainTextEdit.clear()
        self.textEdit_2.clear()


if __name__ == "__main__":
    a = QtWidgets.QApplication(sys.argv)
    app = Main()
    app.show()
    a.exec_()

