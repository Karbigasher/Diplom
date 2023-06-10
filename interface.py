from PyQt5.QtWidgets import QApplication, QTabWidget, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QPlainTextEdit
from PyQt5 import uic
from Diplom.engine import engine
from Diplom.module import module
from Diplom.optimisation_bistr import optim_bistr
from Diplom.optimisation_mert import optim_mert
import sys


class UI(QTabWidget):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("Diplom.ui", self)
        # engine tab
        self.lineedit1 = self.findChild(QLineEdit, "lineEdit")
        self.lineedit2 = self.findChild(QLineEdit, "lineEdit_2")
        self.lineedit3 = self.findChild(QLineEdit, "lineEdit_3")
        self.tableWidget = self.findChild(QTableWidget, "tableWidget")

        self.button = self.findChild(QPushButton, "pushButton")

        # Optim_bistr tab
        self.lineedit4 = self.findChild(QLineEdit, "lineEdit_4")
        self.lineedit5 = self.findChild(QLineEdit, "lineEdit_5")
        self.plainTextEdit = self.findChild(QPlainTextEdit, "plainTextEdit")

        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button2.setEnabled(False)

        # Optim_mert tab
        self.lineedit6 = self.findChild(QLineEdit, "lineEdit_6")
        self.lineedit7 = self.findChild(QLineEdit, "lineEdit_7")
        self.plainTextEdit2 = self.findChild(QPlainTextEdit, "plainTextEdit_2")

        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button3.setEnabled(False)

        # bttn clicks
        self.button.clicked.connect(self.engine_bttn)
        self.button2.clicked.connect(self.optimBistr_bttn)
        self.button3.clicked.connect(self.optimMert_bttn)

        self.show()

    def engine_bttn(self):
        df, ggr, steps = engine(
            float(self.lineedit1.text()), float(self.lineedit2.text()))

        values = df.values
        for i in range(len(values)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(values[i])))

        self.lineedit3.setText(
            str(module(
                float(self.tableWidget.item(7, 0).text()),
                float(self.tableWidget.item(3, 0).text())
            ))
        )

        self.lineedit4.setText(str(steps)[:-2])
        self.lineedit5.setText(str(ggr)[:-2])
        self.lineedit7.setText(str(steps)[:-2])
        self.lineedit6.setText(str(ggr)[:-2])

        self.button2.setEnabled(True)
        self.button3.setEnabled(True)

    def optimBistr_bttn(self):
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText("Результаты оптимизации схемы:")
        ratioPerStep, bistr = optim_bistr(int(self.lineedit5.text()), float(
            self.lineedit3.text()), int(self.lineedit4.text()))
        for i in range(int(self.lineedit4.text())):
            self.plainTextEdit.appendPlainText(
                f"{i+1}-я ступень U = {ratioPerStep[i]}")
        self.plainTextEdit.appendPlainText(f"момент инерции механизма {bistr} кг*м2")

    def optimMert_bttn(self):
        self.plainTextEdit2.clear()
        self.plainTextEdit2.appendPlainText("Результаты оптимизации схемы:")
        ratioPerStep, mert = optim_mert(int(self.lineedit6.text()), float(
            self.lineedit3.text()), int(self.lineedit7.text()))
        for i in range(int(self.lineedit7.text())):
            self.plainTextEdit2.appendPlainText(
                f"{i+1}-я ступень U = {ratioPerStep[i]}")
        self.plainTextEdit2.appendPlainText(f"суммарный мёртвый ход {mert} угл. мин.")

    def closeEvent(self, event):
        QApplication.quit()


app = QApplication(sys.argv)
UIwin = UI()
app.exec_()
app.quit()
