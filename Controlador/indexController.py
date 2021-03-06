from msilib.schema import Directory
from multiprocessing.sharedctypes import Value
from unittest import case
from matplotlib.pyplot import text
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from Controlador.redNeuronalController import NeuralNetwork
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox



from numpy import *
from Vista.ventana_ui import Ui_MainWindow
import pandas as pd
import numpy as np
import os

class palabrasFiltradas(QMainWindow):
    df = []
    archivo = ""
    palabras = []
    listaPalabras = ""
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()        
        self.ui.setupUi(self)
        #self.pushButtonAbrirArchivoCSV.clicked.connect(self.abrir_archivo)
        #self.pushButtonBuscar.clicked.connect(self.trabajarPalabras)
        #self.pushButtonGuardarArchivoFiltrado.clicked.connect(self.guardarArchivoFiltrado)
        self.pushButtonAbrirArchivo_DataSet.clicked.connect(self.abrir_archivo)

    def abrir_archivo(self):
        global archivo
        archivo = QFileDialog.getOpenFileName(
            parent=self,
            caption="Seleccione su archivo para filtrar",
            directory = os.getcwd(),
            filter='csv files (*csv*);; All files *.*')
        global df
        
        df= pd.read_csv(archivo[0], index_col=0,encoding='latin-1')
        return archivo
    
    def trabajarPalabras(self):
        global palabras
        palabras = self.ui.lineEditPalabrasClave.text().split()
        count = 0
        palabrasString = []

        for i in palabras:
            count = count + 1
            if count < len(palabras):
                palabrasString.append( i +"|")
            else:
                palabrasString.append(i)

        print(palabrasString)
        global listaPalabras
        listaPalabras = "".join(palabrasString)
        print(listaPalabras)
        self.ui.lineEditPalabrasClave.setText("")
        return listaPalabras 
        
    def guardarArchivoFiltrado(self):
        palabrasfiltradas = df[df['Texto'].str.contains(listaPalabras, case=False, na=False, regex=True)]
        #palabrasfiltradas.to_csv("C:/Users/USER/Downloads/palabrasfiltradas.csv")
        palabrasfiltradas.to_csv(os.path.abspath("palabrasfiltradas.csv"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = palabrasFiltradas()
    window.show()
    app.exec_()

