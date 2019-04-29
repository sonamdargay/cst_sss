# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uiCode/main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import cv2
import numpy as np
import os

import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_addNew import Ui_addNew
from ui_update import Ui_update
from ui_delete import Ui_remove
from ui_view import Ui_view

class Ui_MainWindow(QtWidgets.QMainWindow):
    def openAddNew(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_addNew()
        self.ui.setupUi(self.window)
        self.window.show()

    def openUpdate(self):
        self.updateDialog = QtWidgets.QDialog()
        self.ui = Ui_update()
        self.ui.setupUi(self.updateDialog)
        self.updateDialog.show()

    def openDelete(self):
        self.deleteDialog = QtWidgets.QDialog()
        self.ui = Ui_remove()
        self.ui.setupUi(self.deleteDialog)
        self.deleteDialog.show()

    def openView(self):
        self.viewDialog = QtWidgets.QDialog()
        self.ui = Ui_view()
        self.ui.setupUi(self.viewDialog)
        self.viewDialog.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(285, 384)
        MainWindow.setMinimumSize(QtCore.QSize(285, 384))
        MainWindow.setMaximumSize(QtCore.QSize(285, 384))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.btn_play = QtWidgets.QPushButton(self.centralwidget)
        self.btn_play.setObjectName("btn_play")
        self.verticalLayout_2.addWidget(self.btn_play)
        self.btn_play.clicked.connect(self.VideoPlayer)

        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout_2.addWidget(self.btn_add)
        self.btn_add.clicked.connect(self.openAddNew)

        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setObjectName("btn_delete")
        self.verticalLayout_2.addWidget(self.btn_delete)
        self.btn_delete.clicked.connect(self.openDelete)

        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setObjectName("btn_update")
        self.verticalLayout_2.addWidget(self.btn_update)
        self.btn_update.clicked.connect(self.openUpdate)

        self.btn_view = QtWidgets.QPushButton(self.centralwidget)
        self.btn_view.setObjectName("btn_view")
        self.verticalLayout_2.addWidget(self.btn_view)
        self.btn_view.clicked.connect(self.openView)

        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout_2.addWidget(self.btn_exit)
        self.btn_exit.clicked.connect(self.close_SSS)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 285, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smart Security Survellance"))
        self.btn_play.setText(_translate("MainWindow", "PLAY VIDEO"))
        self.btn_add.setText(_translate("MainWindow", "ADD NEW"))
        self.btn_delete.setText(_translate("MainWindow", "DELETE"))
        self.btn_update.setText(_translate("MainWindow", "UPDATE"))
        self.btn_view.setText(_translate("MainWindow", "VIEW"))
        self.btn_exit.setText(_translate("MainWindow", "EXIT"))


    def close_SSS(self):
        choice = QtWidgets.QMessageBox.question(self,"QuitApp","Are you sure that you want to quit the application?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass
    def VideoPlayer(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('../../trainer/trainer.yml')
        cascadePath = "../../cascades/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath);
        font = cv2.FONT_HERSHEY_SIMPLEX
        #iniciate id counter
        id = 0
        # names related to ids: example ==> Marcelo: id=1,  etc
        names = ['Taw', 'Sonam','Karma Samdrup','Paula', 'Ilza', 'Z', 'W','Suraj Mukhia','Rinchen','Ugyen'] 
        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video widht
        #cam.set(3, 820) #for rpi
        cam.set(4, 480) # set video height
        #cam.set(4, 740) #for rpi
        # Define min window size to be recognized as a face
        minW = 0.05*cam.get(3)
        minH = 0.05*cam.get(4)
        while True:
            ret, img =cam.read()
            #img = cv2.flip(img, -1) # Flip vertically
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            
            faces = faceCascade.detectMultiScale( 
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
               )
            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                # Check if confidence is less them 100 ==> "0" is perfect match for 'confidence = "  {0}%".format(round(100 - confidence))'
                # Confidence 
                if (confidence < 100):
                    id = names[id]
                    #confidence = "  {0}%".format(round(100 - confidence))
                    confidence = "  {0}%".format(round(confidence))
                else:
                    id = "unknown"
                    #confidence = "  {0}%".format(round(100 - confidence))
                    confidence = "  {0}%".format(round(100 - confidence))
                
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  

            cv2.imshow('SSS-CST',img) 

            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
        # Do a bit of cleanup
        cam.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

