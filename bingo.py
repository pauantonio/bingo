# Filename: bingo.py

"""Bingo per al Centre d'Esplai Flor de Neu by Pau Antonio Soler"""

from pickle import FALSE
import sys
from tkinter import Y

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QWidget, QVBoxLayout, QLabel, QPushButton
)

from PyQt5 import QtCore

from PyQt5.QtGui import *

from PyQt5.uic import loadUi

from bingo_window import Ui_MainWindow

vectorNumeros = [False] * 90
ultims = []

class Bingo(QWidget) :
    def __init__(self):
        super().__init__()
        screen = QApplication.primaryScreen()
        self.setWindowTitle("Bingo Centre d'Esplai Flor de Neu")
        layout = QVBoxLayout()
        self.label = QLabel("")
        self.label.setStyleSheet("background-image : url(bingo.png); background-repeat: no-repeat; background-position: center;")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setStyleSheet("background-color: white")

        self.boto = QPushButton('Tancar', self)
        self.boto.setMinimumSize(QtCore.QSize(200, 50))
        self.boto.move(screen.size().width()-400, screen.size().height()-200)
        self.boto.clicked.connect(self.close)

        self.showMaximized()

class Linia(QWidget) :
    def __init__(self):
        super().__init__()
        screen = QApplication.primaryScreen()
        self.setWindowTitle("Bingo Centre d'Esplai Flor de Neu")
        layout = QVBoxLayout()
        self.label = QLabel("")
        self.label.setStyleSheet("background-image : url(linia.png); background-repeat: no-repeat; background-position: center;")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setStyleSheet("background-color: white")

        self.boto = QPushButton('Tancar', self)
        self.boto.setMinimumSize(QtCore.QSize(200, 50))
        self.boto.move(screen.size().width()-400, screen.size().height()-200)
        self.boto.clicked.connect(self.close)

        self.showMaximized()

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.setWindowTitle("Bingo Centre d'Esplai Flor de Neu")

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
            item.setBackground(QBrush(QColor(255, 0, 0, 255)))
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
        '''
        msg = QMessageBox()
        msg.setWindowTitle("LÍNIA!")
        msg.setText("Un afortunat/da ha fet línia!")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
'''
        self.linia = Linia()
        self.linia.show()

    def bingoClicat(self) :
        '''
        msg = QMessageBox()
        msg.setWindowTitle("BINGO!")
        msg.setText("Un afortunat/da ha fet bingo!")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
'''
        self.bingo = Bingo()
        self.bingo.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())