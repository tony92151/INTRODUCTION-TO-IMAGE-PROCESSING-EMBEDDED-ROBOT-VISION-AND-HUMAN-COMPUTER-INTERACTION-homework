# -*- coding: utf-8 -*-

import sys
from hw1_ui import Ui_MainWindow
import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication
import time


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.onBindingUI()

    # Write your code below
    # UI components are defined in hw1_ui.py, please take a look.
    # You can also open hw1.ui by qt-designer to check ui components.

    def onBindingUI(self):
        self.btn1_1.clicked.connect(self.on_btn1_1_click)
        self.btn1_2.clicked.connect(self.on_btn1_2_click)
        self.btn1_3.clicked.connect(self.on_btn1_3_click)
        self.btn1_4.clicked.connect(self.on_btn1_4_click)
        self.btn2_1.clicked.connect(self.on_btn2_1_click)
        self.btn3_1.clicked.connect(self.on_btn3_1_click)
        self.btn4_1.clicked.connect(self.on_btn4_1_click)
        self.btn4_2.clicked.connect(self.on_btn4_2_click)
        self.btn5_1.clicked.connect(self.on_btn5_1_click)
        self.btn5_2.clicked.connect(self.on_btn5_2_click)

    # button for problem 1.1
    def on_btn1_1_click(self):
        img = cv2.imread('dog.bmp')
        #a,b = img.cvSize
        print('Height = %d' % img.shape[0])
        print('Width = %d' % img.shape[1])
        #print(type(img))
        #print(img.shape[0])
        cv2.imshow('dog',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows('dog') 
        #print(type(img)
        
        
        

    def on_btn1_2_click(self):
        img = cv2.imread('color.png')
        print(type(img))
        
        

        img2 = img
        img2[:,:,[0,1,2]] = img2[:,:,[1,2,0]]

        cv2.imshow('color',img)
        cv2.imshow('color2',img2)
                 
    
        #cv2.destroyWindow('dog')

    def on_btn1_3_click(self):
        pass

    def on_btn1_4_click(self):
        pass

    def on_btn2_1_click(self):
        pass

    def on_btn3_1_click(self):
        pass

    def on_btn4_1_click(self):
        pass

    def on_btn4_2_click(self):
        pass

    def on_btn5_1_click(self):
        # edtAngle, edtScale. edtTx, edtTy to access to the ui object
        pass

    def on_btn5_2_click(self):
        pass
    ### ### ###


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
