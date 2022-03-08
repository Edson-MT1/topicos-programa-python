from msilib.schema import CheckBox
from select import select
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication,QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
import numpy as np

from Vista.ventana_ui import Ui_MainWindow
from Controlador.indexController import Holamundo
from Controlador.Histograma import Histograma
from Controlador.WordCloudController import Nube
from Controlador.redNeuronalController import NeuralNetwork

class MainWindow(QMainWindow):
    archivo = ""
    question = [0 for i in range(0, 8)]
    

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()    
        self.hola = Holamundo   
        self.histograma = Histograma
        self.nube = Nube
        self.ui.setupUi(self)  
        self.conexiones()
        self.chechboxChnged()
    
    def chechboxChnged(self):
        self.ui.pushButtonBuscar_DataSet.clicked.connect(self.send)
        self.ui.checkBoxSuicidio.stateChanged.connect(self.onStateChange)
        self.ui.checkBoxTristeza.stateChanged.connect(self.onStateChange)
        self.ui.checkBoxMascota.stateChanged.connect(self.onStateChange)
        self.ui.checkBoxUniversidad.stateChanged.connect(self.onStateChange)
        self.ui.checkBoxEscuela.stateChanged.connect(self.onStateChange)
        self.ui.checkBoxFamilia.stateChanged.connect(self.onStateChange)
        self.ui.checkBoxDepresion.stateChanged.connect(self.onStateChange)
        self.ui.checkBoxAnsiedad.stateChanged.connect(self.onStateChange)

    def conexiones(self):
        self.ui.itemCrearBd.triggered.connect(lambda: self.cambio_pag_2())
        self.ui.itemNube.triggered.connect(lambda: self.crear_wordcloud())
        self.ui.itemHistograma.triggered.connect(lambda: self.crear_histograma())
        self.ui.itemEntrenamiento.triggered.connect(lambda: self.abrirRedVista())
        self.ui.pushButtonAbrirArchivoCSV.clicked.connect(self.abrir_archivo)
        self.ui.pushButtonBuscar.clicked.connect(self.trabajarPalabras)
        self.ui.pushButtonGuardarArchivoFiltrado.clicked.connect(self.guardarArchivoFiltrado)
        self.ui.pushButtonAbrirArchivo_DataSet.clicked.connect(self.abrir_archivo)
        self.ui.pushButtonEntrenar.clicked.connect(self.train)
        

    def abrir_archivo(self):
        try:
            global archivo
            archivo = self.hola.abrir_archivo(self)
            self.ui.labelDireccionArchivo_2.setText(archivo[0])
            print(archivo[0])
        except:
            QMessageBox.about(self, "Error", "No se selecciono un archivoooooooo")
    def trabajarPalabras(self):
        self.hola.trabajarPalabras(self)

    def guardarArchivoFiltrado(self):
        self.hola.guardarArchivoFiltrado(self)

    def cambio_pag_2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.reduccion)

    def cambio_pag_1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.frecuencia)

    def abrirRedVista(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.neuronal)

    def crear_histograma(self):
        try:
            self.histograma.leer_csv(self)
            self.histograma.filtradoPalabras(self)
            self.histograma.busquedaFrecuencia(self)        
            self.histograma.showData(self)
        except:
            QMessageBox.about(self, "Error", "No se selecciono un archivo")

    def crear_wordcloud(self):
        try:
            self.nube.abrir_archivo(self)
            self.nube.generarWordCloud(self)
        except:
            QMessageBox.about(self, "Error", "No se selecciono un archivo")


    def load_data(self):
        global archivo
        all_data = pd.read_csv(archivo[0])
        print(all_data)
        input_columns =  all_data[['Tristeza', 'Ansiedad', 'Depresion', 'Suicidio', 'Universidad', 'Escuela', 'Familia', 'Mascota']]
        output_column = all_data[['Salida']]
        
        training_set_inputs = input_columns[:].values
        training_set_outputs = output_column.values
        
        print (training_set_inputs)
        print (training_set_outputs)

    def train(self):
        self.load_data()
        self.neural_network = NeuralNetwork()
    
        if not self.ui.lineEditIteraciones.text():

            self.ui.resultado_Entrenamiento.setText(np.array2string(self.neural_network.synaptic_weights))
            self.neural_network.train(self.training_set_inputs, self.training_set_outputs)
            self.ui.resultado_Entrenamiento.setText(np.array2string(self.neural_network.synaptic_weights))
        else:
            #agregar iteraciones desde interfaz
            iteraciones = int(self.ui.lineEditIteraciones.text())
            self.ui.resultado_Entrenamiento.setText(np.array2string(self.neural_network.synaptic_weights))
            self.neural_network.train(self.training_set_inputs, self.training_set_outputs, iteraciones)
            self.ui.resultado_Entrenamiento.setText(np.array2string(self.neural_network.synaptic_weights))
            
        self.show_dialog()
        
    def show_dialog(self):
        dlg = QMessageBox(self.ui)
        dlg.setWindowTitle("")
        dlg.setText("¡El entrenamiento ha finalizado!")
        button = dlg.exec()

        # if button == QMessageBox.Ok:
        #     print("OK!")
    
    def onStateChange(self, state):
        
        if state == QtCore.Qt.Checked:
            if self.hola.sender() == self.ui.checkBoxSuicidio:
                self.question[0] = 1
            elif self.hola.sender() == self.ui.checkBoxTristeza:
                self.question[1] = 1
            elif self.hola.sender() == self.ui.checkBoxMascota:
                self.question[2] = 1
            elif self.hola.sender() == self.ui.checkBoxUniversidad:
                self.question[3] = 1
            elif self.hola.sender() == self.ui.checkBoxEscuela:
                self.question[4] = 1
            elif self.hola.sender() == self.ui.checkBoxFamilia:
                self.question[5] = 1
            elif self.hola.sender() == self.ui.checkBoxDepresion:
                self.question[6] = 1
            elif self.hola.sender() == self.ui.checkBoxAnsiedad:
                self.question[7] = 1
        else:
            if self.hola.sender() == self.ui.checkBoxSuicidio:
                    self.question[0] = 0
            elif self.hola.sender() == self.ui.checkBoxTristeza:
                self.question[1] = 0
            elif self.hola.sender() == self.ui.checkBoxMascota:
                self.question[2] = 0
            elif self.hola.sender() == self.ui.checkBoxUniversidad:
                self.question[3] = 0
            elif self.hola.sender() == self.ui.checkBoxEscuela:
                self.question[4] = 0
            elif self.hola.sender() == self.ui.checkBoxFamilia:
                self.question[5] = 0
            elif self.hola.sender() == self.ui.checkBoxDepresion:
                self.question[6] = 0
            elif self.hola.sender() == self.ui.checkBoxAnsiedad:
                self.question[7] = 0
        print(self.question)
    
    def send(self):
        print ("Considering new situation [1, 0, 0, 1, 0, 1, 0, 1] -> ?: ")
        print (self.neural_network.think(np.array(self.question)))
        ans = np.array2string(self.neural_network.think(np.array(self.question)))
        self.ui.resultado_Entrenamiento.setText(ans)  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    