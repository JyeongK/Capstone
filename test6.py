import sys
import cv2
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtGui

from PIL import Image

form_class = uic.loadUiType("caps_gui.ui")[0]

global pic1_height
global qImg


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Fileopen.clicked.connect(self.loadImageFromFile)
        self.plus.clicked.connect(self.ImageZoomIn) 
        self.minus.clicked.connect(self.ImageZoomOut) 
        self.File_name.clear()
        self.setWindowTitle("RDS Program") # 프로그램 이름 정하기

        
        
    def ImageZoomIn(self) :
        global pic1_height
        pic1_height = pic1_height + 100

        print(pic1_height)
        global qImg
        pixmap = QtGui.QPixmap.fromImage(qImg)

        #if pic1_height > self.pic1.height() :
        #    QPixmap temp = pixmap.copy()
        pixmap = pixmap.scaledToWidth(pic1_height)
        print("pic1_width : ", self.pic1.width())
        print("pic1_height : ", self.pic1.height())
        #print("vertical : ", self.verticalLayout_6.)


        self.pic1.setPixmap(pixmap)
        
        
    def ImageZoomOut(self) :
        global pic1_height
        pic1_height = pic1_height - 100
        print(pic1_height)
        global qImg
        pixmap = QtGui.QPixmap.fromImage(qImg)
        pixmap = pixmap.scaledToWidth(pic1_height)
        print("pic1_width : ", self.pic1.width())
        print("pic1_height : ", self.pic1.height())


        self.pic1.setPixmap(pixmap)
        
        
    def loadImageFromFile(self):
        fname=QFileDialog.getOpenFileName(self,"File Load",'C:/vm-13/','All File(*);; Text File(*.txt);; Image file(*png *jpeg)', 'Image file(*png *jpeg)' )

        img = cv2.imread(fname[0], cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
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
