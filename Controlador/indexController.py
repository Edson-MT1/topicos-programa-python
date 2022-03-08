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

class Holamundo(QMainWindow):
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
    
    def obtenerPalabras(self):
        pass
    
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

    def load_data(self):
        self.all_data = pd.read_csv(self.path)
        
        input_columns =  self.all_data[['Actores', 'Casting', 'Cortometraje', 'Cameo', 'Director', 'Cámara', 'Doblaje', 'Guión']]
        output_column = self.all_data[['Salida']]
        
        self.training_set_inputs = input_columns[:].values
        self.training_set_outputs = output_column.values
        
    def train(self):
        self.load_data()
        self.neural_network = NeuralNetwork()
    
        if not self.view.lineEditIterations.text():
            self.view.textBrowserInitialWeights.setText(np.array2string(self.neural_network.synaptic_weights))
            self.neural_network.train(self.training_set_inputs, self.training_set_outputs)
            self.view.textBrowserFinalWeights.setText(np.array2string(self.neural_network.synaptic_weights))
        else:
            iterations = int(self.view.lineEditIterations.text())
            self.view.textBrowserInitialWeights.setText(np.array2string(self.neural_network.synaptic_weights))
            self.neural_network.train(self.training_set_inputs, self.training_set_outputs, iterations)
            self.view.textBrowserFinalWeights.setText(np.array2string(self.neural_network.synaptic_weights))
            
        self.show_dialog()
        
    def show_dialog(self):
        dlg = QMessageBox(self.view)
        dlg.setWindowTitle("")
        dlg.setText("¡El entrenamiento ha finalizado!")
        button = dlg.exec()

        # if button == QMessageBox.Ok:
        #     print("OK!")
    
    def onStateChange(self, state):
        
        if state == QtCore.Qt.Checked:
            if self.view.sender() == self.view.checkboxActors_2:
                self.question[0] = 1
            elif self.view.sender() == self.view.checkboxCasting_2:
                self.question[1] = 1
            elif self.view.sender() == self.view.checkboxShortFilm_2:
                self.question[2] = 1
            elif self.view.sender() == self.view.checkboxCameo_2:
                self.question[3] = 1
            elif self.view.sender() == self.view.checkboxDirector_2:
                self.question[4] = 1
            elif self.view.sender() == self.view.checkboxCamera_2:
                self.question[5] = 1
            elif self.view.sender() == self.view.checkboxDubbing_2:
                self.question[6] = 1
            elif self.view.sender() == self.view.checkboxScript_2:
                self.question[7] = 1
        else:
            if self.view.sender() == self.view.checkboxActors_2:
                    self.question[0] = 0
            elif self.view.sender() == self.view.checkboxCasting_2:
                self.question[1] = 0
            elif self.view.sender() == self.view.checkboxShortFilm_2:
                self.question[2] = 0
            elif self.view.sender() == self.view.checkboxCameo_2:
                self.question[3] = 0
            elif self.view.sender() == self.view.checkboxDirector_2:
                self.question[4] = 0
            elif self.view.sender() == self.view.checkboxCamera_2:
                self.question[5] = 0
            elif self.view.sender() == self.view.checkboxDubbing_2:
                self.question[6] = 0
            elif self.view.sender() == self.view.checkboxScript_2:
                self.question[7] = 0
        print(self.question)
    
    def send(self):
        print ("Considering new situation [1, 0, 0, 1, 0, 1, 0, 1] -> ?: ")
        print (self.neural_network.think(np.array(self.question)))
        ans = np.array2string(self.neural_network.think(np.array(self.question)))
        self.view.lineEditAns.setText(ans)  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Holamundo()
    window.show()
    app.exec_()

