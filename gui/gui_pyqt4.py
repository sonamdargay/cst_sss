import sys
from PyQt4 import QtGui,QtCore
import numpy as np
import cv2

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class SSS(QtGui.QWidget):
    
    def __init__(self):
        super(SSS, self).__init__()

        #This is left side box of gui
        buttonLayout = QtGui.QHBoxLayout()
       
        buttonLayout.addWidget(rightPaneSSS())

        #This is right side box of gui where video will be displayed
        videoLayout = QtGui.QVBoxLayout()
        video_btn = QtGui.QPushButton('video',self)
        quit_btn = QtGui.QPushButton('Quit')
        quit_btn.clicked.connect(self.close_SSS)
        #videoLayout.addStretch(1)
        videoLayout.addWidget(video_btn)
        videoLayout.addWidget(quit_btn)

        #This is third layout in which right and left box are merged together
        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addLayout(videoLayout)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)


        self.setGeometry(0, 0, 800,400)
        self.setWindowTitle('Smart Security Survilleance')
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        self.show()

    #It quits the main application
    def close_SSS(self):
        choice = QtGui.QMessageBox.question(self,"QuitApp","Are you sure to quit?",
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
    
    #This will contain the main face recogintion system/logic
    def video_Show(self):
        cap = cv2.VideoCapture(0)
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                #frame = cv2.flip(frame,0)
                #write the flipped frame
                out.write(frame)

                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
        #Release everything if job is finished
        cap.release()
        out.release()
        cv2.destroyAllWindows()

#This contains the main tab creation for right side box 
class rightPaneSSS(QTabWidget):
    def __init__(self, parent = None):
      super(rightPaneSSS, self).__init__(parent)
      self.addNew_btn = QWidget()
      self.delete_btn = QWidget()
      self.update_btn = QWidget()
      self.view_btn = QWidget()
        
      self.addTab(self.addNew_btn,"Tab 1")
      self.addTab(self.delete_btn,"Tab 2")
      self.addTab(self.update_btn,"Tab 3")
      self.addTab(self.view_btn,"Tab 4")
      self.addNew()
      #self.delete()
      #self.update()
      #self.view()

    def addNew(self):
      layout = QFormLayout()
      layout.addRow("Name",QLineEdit())
      layout.addRow("Address",QLineEdit())
      self.setTabText(0,"ADD NEW")
      self.addNew_btn.setLayout(layout)

    #def delete(self):

    #def update(self):

    #def view(self):



        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = SSS()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()  
