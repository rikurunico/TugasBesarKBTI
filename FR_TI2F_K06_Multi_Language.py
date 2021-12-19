import sys
import os
import random
from deep_translator import GoogleTranslator
import gtts
from playsound import playsound

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer


class Translator(QWidget):
    def __init__(self):
        super(Translator, self).__init__()
        self.init_ui()


    def init_ui(self):
        vb = QVBoxLayout()
        self.setLayout(vb)
        
        font = QFont("Serif", 10)
        self.setStyleSheet("background-color: rgb(242, 175, 175);")
        
        self.label = QLabel("MULTI LANGUAGE")
        self.label.setFont(QFont("Times", 15))
        self.label.setStyleSheet("background-color: rgb(233, 124, 124);")
        self.label.setAlignment(Qt.AlignCenter)
        vb.addWidget(self.label)
        
        self.insert_text = QTextEdit()
        self.insert_text.setFont(font)
        self.insert_text.setStyleSheet("background-color: rgb(231, 206, 206);")
        vb.addWidget(self.insert_text)
        

        self.show_translation = QTextEdit()
        self.show_translation.setFont(font)
        self.show_translation.setStyleSheet("background-color: rgb(231, 206, 206);")
        vb.addWidget(self.show_translation)

        self.translatebtn = QPushButton("Terjemahkan")
        self.translatebtn.setFont(font)
        self.translatebtn.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.translatebtn.setFont(font)
        vb.addWidget(self.translatebtn)
        

       
        self.combo = QComboBox()
        self.combo.setFont(font)
        bahasa =["Arabic","Amharic", "Afrikaans", "Bulgarian", "English", "Indonesian", "Italian", "Spanish", "Kannada", 
                 "Korean", "Malay", "Mongolian", "German", "Portuguese", "Russian", "Romanian", "Sundanese", 
                 "Javanese", "Japanese", "French", "Thai"]
        self.combo.addItems(bahasa)
        self.combo.setEditable(True)
        self.combo.lineEdit().setAlignment(Qt.AlignCenter)
        vb.addWidget(self.combo)
        self.targer ={"Arabic" : "ar", "Amharic" : "am", "Afrikaans" : "af", "Bulgarian" : "bg", "English" : "en", "Indonesian" : "id", 
                      "Italian" : "it", "Spanish" : "es", "Kannada" : "kn", "Korean" : "ko", "Malay" : "ms", "Mongolian" : "mn", 
                      "German" : "de", "Portuguese" : "pt", "Russian" : "ru", "Romanian" : "ro", "Sundanese" : "su", 
                      "Javanese" : "jv", "Japanese" : "ja", "French" : "fr", "Thai" : "th"}
        
        self.player = QMediaPlayer()

        self.translatebtn.clicked.connect(self.translate_text)
       

    def translate_text(self):
        global mp3
        mp3 = random.randint(10000, 1000000)
        target = self.targer[self.combo.currentText()]
        text = self.insert_text.toPlainText()
        translated = GoogleTranslator(
            source="auto", target=target).translate(text)
        self.show_translation.clear()
        self.show_translation.setText(translated)
        tts = gtts.gTTS(translated, lang=target)
        os.remove('sample.mp3')
        tts.save('sample.mp3')
        #Ganti Sesuai Directory Sample MP3 Kalian Masing Masing
        playsound('C:/Users/IQRIMA/KBTItubes/sample.mp3')
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Translator()
    gui.setGeometry(100, 100, 800, 500)
    gui.setWindowTitle("Multi-Language 2021")
    gui.show()
    sys.exit(app.exec_())
