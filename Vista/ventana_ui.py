# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(666, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 661, 471))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.stackedWidget.addWidget(self.home)
        self.reduccion = QtWidgets.QWidget()
        self.reduccion.setObjectName("reduccion")
        self.layoutWidget = QtWidgets.QWidget(self.reduccion)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 651, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonAbrirArchivoCSV = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonAbrirArchivoCSV.setObjectName("pushButtonAbrirArchivoCSV")
        self.gridLayout.addWidget(self.pushButtonAbrirArchivoCSV, 2, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 1, 1, 1)
        self.pushButtonBuscar = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonBuscar.setObjectName("pushButtonBuscar")
        self.gridLayout.addWidget(self.pushButtonBuscar, 6, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.lineEditPalabrasClave = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditPalabrasClave.setObjectName("lineEditPalabrasClave")
        self.gridLayout.addWidget(self.lineEditPalabrasClave, 6, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.labelDireccionArchivo = QtWidgets.QLabel(self.layoutWidget)
        self.labelDireccionArchivo.setText("")
        self.labelDireccionArchivo.setObjectName("labelDireccionArchivo")
        self.gridLayout.addWidget(self.labelDireccionArchivo, 2, 1, 1, 1)
        self.pushButtonGuardarArchivoFiltrado = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonGuardarArchivoFiltrado.setObjectName("pushButtonGuardarArchivoFiltrado")
        self.gridLayout.addWidget(self.pushButtonGuardarArchivoFiltrado, 8, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.stackedWidget.addWidget(self.reduccion)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 26))
        self.menubar.setObjectName("menubar")
        self.menuBD = QtWidgets.QMenu(self.menubar)
        self.menuBD.setObjectName("menuBD")
        self.menuFrecuencia = QtWidgets.QMenu(self.menubar)
        self.menuFrecuencia.setObjectName("menuFrecuencia")
        MainWindow.setMenuBar(self.menubar)
        self.itemCrearBd = QtWidgets.QAction(MainWindow)
        self.itemCrearBd.setObjectName("itemCrearBd")
        self.actionsadsad = QtWidgets.QAction(MainWindow)
        self.actionsadsad.setObjectName("actionsadsad")
        self.itemNube = QtWidgets.QAction(MainWindow)
        self.itemNube.setObjectName("itemNube")
        self.itemHistograma = QtWidgets.QAction(MainWindow)
        self.itemHistograma.setObjectName("itemHistograma")
        self.menuBD.addAction(self.itemCrearBd)
        self.menuFrecuencia.addAction(self.itemNube)
        self.menuFrecuencia.addAction(self.itemHistograma)
        self.menubar.addAction(self.menuBD.menuAction())
        self.menubar.addAction(self.menuFrecuencia.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Analizador"))
        self.pushButtonAbrirArchivoCSV.setText(_translate("MainWindow", "Seleccionar"))
        self.pushButtonBuscar.setText(_translate("MainWindow", "Buscar"))
        self.label_5.setText(_translate("MainWindow", "Ingrese las palabras claves a filtrar, usando espacios entre cada palabra"))
        self.label.setText(_translate("MainWindow", "Seleccione su archivo CSV"))
        self.label_6.setText(_translate("MainWindow", "Palabras clave:"))
        self.pushButtonGuardarArchivoFiltrado.setText(_translate("MainWindow", "Guardar CSV Reducido"))
        self.label_9.setText(_translate("MainWindow", "Crear Base De Datos Reducido"))
        self.label_3.setText(_translate("MainWindow", "Direccion del Archivo:"))
        self.menuBD.setTitle(_translate("MainWindow", "BD reducida"))
        self.menuFrecuencia.setTitle(_translate("MainWindow", "Frecuencia de palabras"))
        self.itemCrearBd.setText(_translate("MainWindow", "Crear BD Reducida"))
        self.actionsadsad.setText(_translate("MainWindow", "Nube de palabras"))
        self.itemNube.setText(_translate("MainWindow", "Nube de palabras"))
        self.itemHistograma.setText(_translate("MainWindow", "Histograma"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

