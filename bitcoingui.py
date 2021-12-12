import sys
import requests
from PyQt5.QtWidgets import*
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer,QDateTime
import time

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Bitcoin Tracker"
        self.left = 200
        self.top = 300
        self.price = QLabel(self)
        self.main()
        self.label = QLabel(self)
        timer = QtCore.QTimer(self, timeout=self.main, interval=5 * 1000)
        timer.start()
        self.display()
        self.width = 180
        self.height = 60
        self.maximize()
        self.mw_attributes()
        self.show()
        
    def main(self):
            
        response = requests.get ('https://api.coindesk.com/v1/bpi/currentprice.json')

        #Run this in terminal to get data before hand
        response.json()

        data = response.json()

        usd = data["bpi"]["USD"]["rate"]

        a = usd

        b = a.split(",")
        c = "".join(b)

        d = float(c)
        print (d)
        MainWindow.e = round(d,2)
        self.price.setText (f"Bitcoin Price: $ {MainWindow.e}")         
            

    def mw_attributes(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
    def display(self):
        self.price.setGeometry (20, 25, 180, 10)
        self.price.setText (f"Bitcoin Price: $ {MainWindow.e}")
        
    def maximize(self):
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        
   



app = QApplication(sys.argv)
ex = MainWindow()
sys.exit (app.exec())