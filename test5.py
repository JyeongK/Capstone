#export QT_DEBUG_PLUGINS=1

import sys
import os
import cv2
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from pathlib import Path
from utils import *
from PyQt5 import QtGui
from PIL import Image



form_class = uic.loadUiType("caps_gui.ui")[0]
projDIR = Path('../').resolve()

global pic_name
global width
global pic1_height
global qImg
#test text
width = 400

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Start.clicked.connect(self.startPredict)
        self.Fileopen.clicked.connect(self.loadImageFromFile)  
        self.plus.clicked.connect(self.ImageZoomIn) 
        self.minus.clicked.connect(self.ImageZoomOut) 
        self.progressBar_2.reset()
        self.File_name.clear()
        self.setWindowTitle("RDS Program")

        
    def ImageZoomIn(self) :
        global pic1_height
        global qImg
        pic1_height = pic1_height + 100
        pixmap = QtGui.QPixmap.fromImage(qImg)
        pixmap = pixmap.scaledToWidth(pic1_height)

        self.pic1.setPixmap(pixmap)
    	
    def ImageZoomOut(self) :
        global pic1_height
        global qImg
        pic1_height = pic1_height - 100
        pixmap = QtGui.QPixmap.fromImage(qImg)
        pixmap = pixmap.scaledToWidth(pic1_height)
        self.pic1.setPixmap(pixmap)
        
    def startPredict(self):
        global pic_name
        os.system('sudo docker start rds_test')
        os.system('sudo docker attach rds_test')
        os.system('sudo docker exec rds_test sh -c "cd RDS;./RDS_nonRDS.sh"')
        img = pic_name.split('/')
        png_path = os.path.join(projDIR,"data","RDS",img[-1])
        self.qPixmapFileVar2 = QPixmap()
        self.qPixmapFileVar2.load(png_path)
        self.qPixmapFileVar2 = self.qPixmapFileVar2.scaledToWidth(400)
        self.pic2.setPixmap(self.qPixmapFileVar2)
        txt_path = os.path.join(projDIR,"output","pred.txt")
        data = showPredResult(txt_path)
        data = data.strip('[]')
        RDS = int(float(data)*100)
        self.progressBar_2.setValue(RDS)


    def loadImageFromFile(self):
        fname=QFileDialog.getOpenFileName(self,"File Load",'C:/vm-13/','All File(*);; Text File(*.txt);; Image file(*png *jpeg)', 'Image file(*png *jpeg)' )

        img = cv2.imread(fname[0], cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        image = Image.open(fname[0])
        h, w, c = img.shape
        global qImg
       
        qImg = QtGui.QImage(img.data, w, h, w*c, QtGui.QImage.Format_RGB888)
        #qImg = qimage2ndarray.array2qimage(img, normalize=True)
        
        pixmap = QtGui.QPixmap.fromImage(qImg)
        global pic1_height
        pic1_height = self.pic1.height()
        pixmap = pixmap.scaledToHeight(pic1_height)
        self.pic1.setPixmap(pixmap)

        if fname[0]:
            print("파일 선택됨 파일 경로는 아래와 같음")
            print(fname[0])

        else:
            print("파일 안 골랐음")
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = WindowClass() 
    mywindow.show()
    app.exec_()
