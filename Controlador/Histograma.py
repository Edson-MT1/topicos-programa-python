import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox
from stop_words import get_stop_words 
import os

class Histograma:
    df = ''
    texto = ''
    data = ''
    palabras_irrelevantes = []

    def leer_csv(self):
        archivo = QFileDialog.getOpenFileName(
            parent=self,
            caption="Seleccione su archivo para filtrar",
            directory = os.getcwd(),
            filter='csv files (*csv*);; All files *.*')
        global df
        
        df= pd.read_csv(archivo[0], index_col=0,encoding='latin-1')
        a = list(df['Texto']) 
        
        global texto
        texto = ' '.join(str(e) for e in a) 

    
    def filtradoPalabras(self):
        caracteres = ",;:.\n!\"'ÃÂðŸ€@¢âœïˆâïÃäº¾©*¡#£»´²³±¦"
        global texto

        #elimina caracteres y vuelve minusculas las palabras
        for caracter in caracteres:
            texto = texto.replace(caracter,"")  # Remplazarlo por "nada"; es decir, removerlo
        texto= texto.lower()
    
    def busquedaFrecuencia(self):
        global data
        global texto
        #buscar la frecuencia en x y y
        palabras = texto.split(" ")
        
        global palabras_irrelevantes
        palabras_irrelevantes = get_stop_words('spanish')
        stop_wordsunicos = ['Ã', 'Â', 'ð','ðŸ', 'Ÿ', '€','@', '¢' ,'https', 'âœ' 'âœˆï','ˆ','Ÿ','â','œ','ï', 'estÃ','dÃ','mÃ', 'ä', 'https://t.co/', 't', 'co', 'í', 'n']
        palabras_irrelevantes.extend(stop_wordsunicos)
        #palabras_irrelevantes.append("campeche")

        for i in range (len(palabras_irrelevantes)):
            try:
                while True:
                    palabras.remove(palabras_irrelevantes[i-1])
            except ValueError:
                pass
        diccionario_frecuencias = {}
        
        print(palabras)

        for palabra in palabras:
            if palabra in diccionario_frecuencias:
                diccionario_frecuencias[palabra] += 1
            else:
                diccionario_frecuencias[palabra] = 1

        for palabra in diccionario_frecuencias:
            frecuencia = diccionario_frecuencias[palabra]
            #print(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia}")
        data = palabras

    def showData(self):
        n, bins, patches = plt.hist(data)
        plt.xlabel("Palabras")
        plt.ylabel("Frecuencia")
        plt.title("Histograma")
        plt.show()


#print(texto) 