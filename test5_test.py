import sys
import os
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from pathlib import Path
from utils import *
from multiprocessing import Process

form_class = uic.loadUiType("caps_gui.ui")[0]
projDIR = Path('../').resolve()

global pic_name
global width
global mywindow
width = 400
# test                  
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
        #label1 = QLabel("pic1", self)
        #label1.setStyleSheet("background-color : #555555")
        
        
        #qPixmapVar.load("01395087_CR_ST001_SE001_IM00001.png")
        
        
        
    def ImageZoomIn(self) :
    	global width
    	width = width + 100
    	print(width)
    	self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(width)
    	self.pic1.setPixmap(self.qPixmapFileVar)
    	
    def ImageZoomOut(self) :
    	global width
    	width = width - 100
    	print(width)
    	self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(width)
    	self.pic1.setPixmap(self.qPixmapFileVar)
        
    def startPredict(self):
        global pic_name
        cmd = 'cp '+str(pic_name)+' '+str(projDIR)+'/input'
        os.system(str(cmd))
        docker_start = Thread1(self)
        docker_start.start()
        rds_predict = Thread2(self)
        rds_predict.start()
        #rds_predict.wait()
                        




    def loadImageFromFile(self):
        global pic_name
        fname=QFileDialog.getOpenFileName(self,"File Load",'C:home/','All File(*);; Text File(*.txt);; Image file(*png *jpeg)', 'Image file(*png *jpeg)' )
        if fname[0] != '':
            pic_name = fname[0]
            cmd = 'rm '+str(projDIR)+'/input/*'  
            os.system(cmd)
            self.progressBar_2.reset()
            self.qPixmapFileVar = QPixmap()
            self.qPixmapFileVar.load(fname[0])
            self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(400)
            self.pic1.setPixmap(self.qPixmapFileVar)
            self.File_name.setText(fname[0])
            self.pic2.clear()
            scene = QGraphicsScene()

class Thread1(QThread):
    #parent = MainWidget을 상속 받음.
    def __init__(self, parent):
        super().__init__(parent)
    def run(self):
        os.system('sudo docker start rds_test')
        os.system('sudo docker attach rds_test')
        
class Thread2(QThread):
    #parent = MainWidget을 상속 받음.
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    def run(self):
        os.system('sudo docker exec rds_test sh -c "cd RDS;./RDS_nonRDS.sh"')
        img = pic_name.split('/')
        png_path = os.path.join(projDIR,"data","RDS",img[-1])
        self.parent.qPixmapFileVar2 = QPixmap()
        self.parent.qPixmapFileVar2.load(png_path)
        self.parent.qPixmapFileVar2 = mywindow.qPixmapFileVar2.scaledToWidth(400)
        self.parent.pic2.setPixmap(self.parent.qPixmapFileVar2)
        txt_path = os.path.join(projDIR,"output","pred.txt")
        data = showPredResult(txt_path)
        data = data.strip('[]')
        RDS = int(float(data)*100)
        mywindow.progressBar_2.setValue(RDS)   
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = WindowClass() 
    mywindow.show()
    app.exec_()
