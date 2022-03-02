from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QLabel
import sys
import GUI
import datetime
from datetime import date

class Koledar:
    def __init__(self, _app):
        self.app = _app
        self.ui = GUI.Ui_KoledarWindow()
        self.uiWindow = QtWidgets.QMainWindow()
        self.uiWindow.setWindowIcon(QtGui.QIcon('icon.png'))

        self.ponPrazniki = [] #vsakoletni prazniki npr prvi april -> 1.4.XXXX
        self.Prazniki = [] #ne-vsakoletni prazniki npr. velika noč


    def setupUI(self):
        self.app.setStyle("Fusion")
        self.ui.setupUi(self.uiWindow)

        #event listeners
        self.ui.meseci.currentTextChanged.connect(self.updateKoledar)
        self.ui.leto.editingFinished.connect(self.updateKoledar)
        self.ui.datumLine.editingFinished.connect(self.parseDatumText)

        #prikazi koledar in okno
        self.ui.datumLine.setText(date.today().strftime("%d.%m.%Y")) #nastavi koledar na trenutni mesec in leto
        self.parseDatumText()
        self.updateKoledar()
        self.uiWindow.show()


    def getPrazniki(self,path):

        with open(path) as f:
            lines = f.read().splitlines()

        self.ponPrazniki = []
        self.Prazniki = []

        for line in lines:
            datum, oznaka = line.split(" ")
            if oznaka == "p":
                self.ponPrazniki.append(datum[:datum.rfind(".")]) #dodamo samo DD.MM , ker leto ni pomembno
            else:
                self.Prazniki.append(datum)
    
    def parseDatumText(self):
        try:
            _,mes,let = self.ui.datumLine.text().split(".")
        except:
            return 

        #preverimo da imamo številko za mesec in leto
        if not mes.isnumeric() or not let.isnumeric:
            return
        
        #nastavimo nove vrednosti
        self.ui.datumLine.setText("")
        self.ui.meseci.setCurrentIndex(int(mes)-1)
        self.ui.leto.setValue(int(let))

        self.updateKoledar()

    

    
    def updateKoledar(self):
        #pridobi datume praznikov iz datoteke
        self.getPrazniki("./prazniki.txt")

        mesec = self.ui.meseci.currentIndex() + 1
        leto = self.ui.leto.value()
        daysInMonth = self.getDaysInMonth(mesec,leto)


        offset = datetime.date(leto,mesec,1).weekday() #pove kateri dan v tednu je prvi dan meseca
        layout = self.ui.koledarLayout

        #zbrisi prejsni koledar
        for i in reversed(range(layout.count())): 
            layout.itemAt(i).widget().setParent(None)

        #dodaj dni v tednu
        teden = ["Pon","Tor","Sre","Čet","Pet","Sob","Ned"]
        for i in range(7):
            label = QLabel(teden[i])
            layout.addWidget(label,0,i)
            label.setAlignment(QtCore.Qt.AlignCenter)

        #spremenljivke za preverjanje praznika
        polniDatum = f".{mesec}.{leto}"
        polovicniDatum = f".{mesec}"

        #sestavi koledar
        for i in range(offset, daysInMonth+offset):
            stDneva = i - offset + 1
            label = QLabel(str(stDneva))
            label.setAlignment(QtCore.Qt.AlignCenter)

            #Če je praznik ga pobarvaj
            if f"{stDneva}{polniDatum}" in self.Prazniki or f"{stDneva}{polovicniDatum}" in self.ponPrazniki:
                label.setStyleSheet("background-color: red;border: 1px solid black; border-radius: 5px;")
            else:
                label.setStyleSheet("border: 1px solid black; border-radius: 5px;")

            r = i // 7 + 1
            c = i % 7
            layout.addWidget(label,r,c,1,1)

        self.uiWindow.show()
    

    def leapYear(self,year):
        if year % 400 == 0:
            return True

        if year % 100 == 0:
            return False

        if year % 4 == 0:
            return True

        return False

    def getDaysInMonth(self,month, year):
        if month in {1, 3, 5, 7, 8, 10, 12}:
            return 31

        if month == 2:
            return 29 if self.leapYear(year) else 28

        return 30

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    kol = Koledar(app)
    kol.setupUI()
    sys.exit(app.exec_())
    