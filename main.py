from select import select
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication,QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import *

from Vista.ventana_ui import Ui_MainWindow
from Controlador.indexController import Holamundo
from Controlador.Histograma import Histograma
from Controlador.WordCloudController import Nube

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()    
        self.hola = Holamundo   
        self.histograma = Histograma
        self.nube = Nube
        self.ui.setupUi(self)  
        self.conexiones()

    def conexiones(self):
        self.ui.itemCrearBd.triggered.connect(lambda: self.cambio_pag_2())
        self.ui.itemNube.triggered.connect(lambda: self.crear_wordcloud())
        self.ui.itemHistograma.triggered.connect(lambda: self.crear_histograma())
        self.ui.itemEntrenamiento.triggered.connect(lambda: self.abrirRedVista())
        self.ui.pushButtonAbrirArchivoCSV.clicked.connect(self.abrir_archivo)
        self.ui.pushButtonBuscar.clicked.connect(self.trabajarPalabras)
        self.ui.pushButtonGuardarArchivoFiltrado.clicked.connect(self.guardarArchivoFiltrado)
        
        
    def abrir_archivo(self):
        try:
            archivo = self.hola.abrir_archivo(self)
            self.ui.labelDireccionArchivo.setText(archivo[0])
        except:
            QMessageBox.about(self, "Error", "No se selecciono un archivo")
       
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    