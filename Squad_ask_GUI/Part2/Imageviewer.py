from PyQt5.QtWidgets import QMainWindow ,QApplication ,QPushButton ,QFileDialog,QLabel,QComboBox 
from PyQt5 import uic 
from PyQt5.QtGui import QPixmap 
from PyQt5 import QtCore 
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        uic.loadUi("img.ui",self)
        #find widgets
        self.openfile_button = self.findChild(QPushButton,"openfile_button")
        self.RecentImages=self.findChild(QComboBox,"comboBox")
        self.label2=self.findChild(QLabel,"label_2")
        self.label=self.findChild(QLabel,"label")
        self.openfile_button.clicked.connect(self.clicker)
        self.label3=self.findChild(QLabel,"abokhalil")
        self.RecentImages.activated.connect(self.getFromRecent)


        self.show()
    def getFromRecent(self) :
        #get images from recent combo box 
        text =self.RecentImages.currentText()
        self.pixmap = QPixmap(text)
        self.label.setPixmap(self.pixmap.scaled(250,250, QtCore.Qt.KeepAspectRatio))
    def clicker(self,combobox) :
        #select images from my directory then show it 
        fname=QFileDialog.getOpenFileName(self,"Select an image",""," All Files (*) ;; PNG File (*.png) ;; JPG File (*.jpg) ;;")
        self.pixmap = QPixmap(fname[0])
        self.label.setPixmap(self.pixmap.scaled(250,250, QtCore.Qt.KeepAspectRatio))
        #add image to recent images in combo box
        self.RecentImages.addItem(fname[0])

app=QApplication(sys.argv)
UIWIN=UI()
app.exec_()
