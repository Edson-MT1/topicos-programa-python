from tkinter import filedialog
from wordcloud import WordCloud
import matplotlib.pyplot as plt 
import nltk
from nltk.corpus import stopwords
from PyQt5.QtWidgets import QFileDialog,QMessageBox
import pandas as pd
import os

class Nube:
    df = []
    archivo = ""

    def abrir_archivo(self):
        global archivo
        
        archivo = QFileDialog.getOpenFileName(
            parent=self,
            caption="Seleccione su archivo para filtrar",
            directory = os.getcwd(),
            filter='csv files (*csv*);; All files *.*')

        #self.labelDireccion.setText(archivo)
        print(archivo[0])
        global df
        df= pd.read_csv(archivo[0], index_col=0,encoding='latin-1')


    def generarWordCloud(self):
        info = ""
        frases = df["Texto"]
        frasesArreglo = []

        for i in frases:
            frasesArreglo.append(i)
        info = "".join(frasesArreglo)
        #print(info)

        #generar stopwords
        stop_wordsunicos = ['Ã', 'Â', 'ð','ðŸ', 'Ÿ', '€','@', '¢' ,'https', 'âœ' 'âœˆï','ˆ','Ÿ','â','œ','ï', 'estÃ','dÃ','mÃ', 'ä', 'https://t.co/', 't', 'co', 'í', 'n' ]
        stop_words = stopwords.words('spanish')
        stop_words.extend(stop_wordsunicos)
        #gererar nube
        wordCloud = WordCloud(stopwords = stop_words, max_words=10000).generate(info)
        wordCloud.to_file(os.path.abspath("palabrasfiltradas.png"))
        QMessageBox.about(self, "WordCloud", "El WordCloud fue creado con exito")

        plt.imshow(wordCloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

        

