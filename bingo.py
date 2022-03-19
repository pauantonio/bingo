# Filename: bingo.py

"""Bingo per al Centre d'Esplai Flor de Neu by Pau Antonio Soler"""

from pickle import FALSE
import sys
sys.path.insert(0, './temp')
from tkinter import Y

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QWidget, QVBoxLayout, QLabel, QPushButton
)

from PyQt5 import QtCore

from PyQt5.QtGui import *

from bingo_window import Ui_MainWindow
from popup_bingo_window import Ui_MainWindow as popup_bingo
from popup_linia_window import Ui_MainWindow as popup_linia

vectorNumeros = [False] * 90
ultims = []

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.onlyInt = QIntValidator()
        self.lectorNumero.setValidator(self.onlyInt)
        self.taulaNumeros.resizeColumnsToContents()

        self.taulaNumeros.clicked.connect(self.numeroClicat)
        self.botoNumero.clicked.connect(self.botoClicat)
        self.lectorNumero.returnPressed.connect(self.botoClicat)
        self.reset.clicked.connect(self.resetClicat)
        self.linia.clicked.connect(self.liniaClicat)
        self.bingo.clicked.connect(self.bingoClicat)

    def botoClicat(self) :
        num = self.lectorNumero.text()
        self.lectorNumero.clear()
        if (num != '' and int(num) > 0 and int(num) < 91) : 
            self.canviarNumero(int(num))
        else :
            self.errorLecturaNumeros()

    def errorLecturaNumeros(self) :
        msg = QMessageBox()
        msg.setWindowTitle("VIGILA!")
        msg.setText("Introdueix un número vàlid, entre el 01 i el 90.")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def numeroClicat(self, selected) :
        numero = selected.column()+selected.row()*15+1
        self.taulaNumeros.clearSelection()
        self.canviarNumero(int(numero))
        
    def canviarNumero(self, num) :
        item = self.taulaNumeros.item(int((num-1)/15), (num-1)%15)
        if (not vectorNumeros[num-1]) :
            vectorNumeros[num-1] = True
            #item.setBackground(QBrush(QColor(255, 0, 0, 255)))
            item.setBackground(QBrush(QColor(106, 44, 112, 255)))
            item.setForeground(QBrush(QColor(255, 255, 255, 255)))
            ultims.insert(0, num)
            self.escriureUltims()
        else :
            okey = self.esborrarNumero(num)
            if okey :
                vectorNumeros[num-1] = False
                item.setBackground(QBrush(QColor(255, 255, 255, 255)))
                item.setForeground(QBrush(QColor(0, 0, 0, 255)))
                for n in ultims :
                    if (n == num) : 
                        ultims.remove(num)
                        self.escriureUltims()
                        break

    def esborrarNumero(self, num) :
        msg = QMessageBox()
        msg.setWindowTitle("VIGILA!")
        msg.setText("El número " + str(num) + " ja ha estat introduït.\nEstàs segur que vols esborrar-lo?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        botoSI = msg.button(QMessageBox.Yes)
        botoSI.setText('&Sí')
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()
        return msg.clickedButton() == botoSI

    def resetClicat(self) :
        okey = self.confirmarReset()
        if okey :
            vectorNumeros[:] = [False] * 90
            for column in range(15) :
                for row in range(6) :
                    item = self.taulaNumeros.item(row, column)
                    item.setBackground(QBrush(QColor(255, 255, 255, 255)))
                    item.setForeground(QBrush(QColor(0, 0, 0, 255)))
            ultims.clear()
            self.escriureUltims()

    def confirmarReset(self) :
        msg = QMessageBox()
        msg.setWindowTitle("VIGILA!")
        msg.setText("Estàs segur que vols reiniciar la partida?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        botoSI = msg.button(QMessageBox.Yes)
        botoSI.setText('&Sí')
        msg.setDefaultButton(QMessageBox.Yes)
        msg.exec_()
        return msg.clickedButton() == botoSI

    def escriureUltims(self) :
        for i in range(5) :
            posicio = ''
            if i == 0 : posicio = self.ultim1
            if i == 1 : posicio = self.ultim2
            if i == 2 : posicio = self.ultim3
            if i == 3 : posicio = self.ultim4
            if i == 4 : posicio = self.ultim5

            if i < len(ultims) : 
                posicio.setText(str(ultims[i]))
            else :
                posicio.setText('-')

    def liniaClicat(self) :
        self.win2 = Window()
        self.win2.showMaximized()
        popup_linia().setupUi(self.win2)

    def bingoClicat(self) :
        self.win2 = Window()
        self.win2.showMaximized()
        popup_bingo().setupUi(self.win2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.showMaximized()
    sys.exit(app.exec())