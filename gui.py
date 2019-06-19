import sys,os
from os import path
import sqlite3
import datetime
import fnmatch
#import smtplib

import cv2
import numpy as np
sys.path.append('gui/')
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from ui_addNew import Ui_addNew
from ui_update import Ui_update
from ui_delete import Ui_remove
from ui_view import Ui_view

class RecordVideo(QtCore.QObject):
    image_data = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, camera_port=0, parent=None):
        super().__init__(parent)
        self.camera = cv2.VideoCapture(camera_port)
        self.timer = QtCore.QBasicTimer()

    def start_recording(self):
        self.timer.start(0, self)

    def timerEvent(self, event):
        if (event.timerId() != self.timer.timerId()):
            return
        read, data = self.camera.read()
        if read:
            self.image_data.emit(data)

class FaceDetectionWidget(QtWidgets.QWidget):
    def __init__(self, haar_cascade_filepath, parent=None):
        super().__init__(parent)
        self.classifier = cv2.CascadeClassifier(haar_cascade_filepath)
        self.image = QtGui.QImage()
        self._red = (0, 0, 255)
        self._width = 2
        self._min_size = (20, 20)
        
    def detect_faces(self, image: np.ndarray):
        # haarclassifiers work better in black and white
        value=[]
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.equalizeHist(gray_image)
        value.append(gray_image)
        faces = self.classifier.detectMultiScale(gray_image,
                                                 scaleFactor=1.3,
                                                 minNeighbors=4,
                                                 flags=cv2.CASCADE_SCALE_IMAGE,
                                                 minSize=self._min_size)
        value.append(faces)
        return value

    def image_data_slot(self, image_data):
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('trainer/trainer.yml')
        font = cv2.FONT_HERSHEY_SIMPLEX
        value1 = self.detect_faces(image_data)
        faces=value1[1]
        gray=value1[0]
        id=0
        names = [['unknown','12345678913'],['Suraj Mukhia','21309000371'],['Sonam Dargay','12345678912'],['Karma Samdrup','23456789123'],['Tawmo','34567891234'],['Tak Nath','45678912345']]
        

        for (x, y, w, h) in faces:
            img=cv2.rectangle(image_data,
                          (x, y),
                          (x+w, y+h),
                          self._red,
                          self._width)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            # Check if confidence is less them 100 ==> "0" is perfect match for 'confidence = "  {0}%".format(round(100 - confidence))'
            # Confidence 
            if (confidence < 100):
                ids=id
                id = names[id][0]
                #confidence = "  {0}%".format(round(100 - confidence))
                confidence = "  {0}%".format(round(confidence))

                #We are storing the time stamp of person whenever recognised.
                connection = sqlite3.connect('mySSS.db')
                cur = connection.cursor()

                time_stamp = datetime.datetime.now()
                id_number=names[ids][1]

                cur.execute("SELECT * FROM Time_Log ORDER BY count DESC LIMIT 1")
                result = cur.fetchone()
                if result[0] != str(id_number):
                    cur.execute('''INSERT INTO Time_Log(cid,time_stamp) VALUES(?,?)''',(id_number,time_stamp))
                    connection.commit()
                    connection.close()
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  

            else:
                id = "unknown"
                #confidence = "  {0}%".format(round(100 - confidence))
                #confidence = "  {0}%".format(round(confidence))

                time=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                cv2.imwrite('unknown/unknown'+"_"+str(time)+".jpg",gray[y:y+h,x:x+w])

                #We are storing the time stamp of person whenever recognised.
                connection = sqlite3.connect('mySSS.db')
                cur = connection.cursor()

                time_stamp = datetime.datetime.now()
                id_number=id
                cur.execute("SELECT * FROM Time_Log ORDER BY count DESC LIMIT 1")
                result = cur.fetchone()

                if result[0] != str(id_number):
                    cur.execute('''INSERT INTO Time_Log(cid,time_stamp) VALUES(?,?)''',(id_number,time_stamp))
                    connection.commit()
                    connection.close()

                #for mail alerting
                '''
                if id=="unknown":
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.login("cst.sss101@gmail.com", "Raspberrypi")
                    server.sendmail(
                    "cst.sss101@gmail.com", 
                    "0215538.cst@rub.edu.bt", 
                    "Unknown FOund!")
                    server.quit()
                '''
                
                #for sound
                #os.system("espeak 'Unknow Found'")

            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2) 
            #cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  #prints confidence both for known & unknown
        

        self.image = self.get_qimage(image_data)
        if self.image.size() != self.size():
            self.setFixedSize(self.image.size())
        self.update()

    def get_qimage(self, image: np.ndarray):
        height, width, colors = image.shape
        bytesPerLine = 3 * width
        QImage = QtGui.QImage

        image = QImage(image.data,
                       width,
                       height,
                       bytesPerLine,
                       QImage.Format_RGB888)
        image = image.rgbSwapped()
        return image

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)
        self.image = QtGui.QImage()

class MainWidget(QtWidgets.QWidget):

    def openAddNew(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_addNew()
        self.ui.setupUi(self.window)
        self.window.show()

    def openDelete(self):
        self.deleteDialog = QtWidgets.QDialog()
        self.ui = Ui_remove()
        self.ui.setupUi(self.deleteDialog)
        self.deleteDialog.show()

    def openUpdate(self):
        self.updateDialog = QtWidgets.QDialog()
        self.ui = Ui_update()
        self.ui.setupUi(self.updateDialog)
        self.updateDialog.show()

    def openView(self):
        self.viewDialog = QtWidgets.QDialog()
        self.ui = Ui_view()
        self.ui.setupUi(self.viewDialog)
        self.viewDialog.show()

    def __init__(self, haarcascade_filepath, parent=None):
        super().__init__(parent)

        fp = haarcascade_filepath
        self.face_detection_widget = FaceDetectionWidget(fp)

        # TODO: set video port
        self.record_video = RecordVideo()

        image_data_slot = self.face_detection_widget.image_data_slot
        self.record_video.image_data.connect(image_data_slot)

        layoutL = QtWidgets.QVBoxLayout()
        innerlayoutT = QtWidgets.QVBoxLayout()

        innerlayoutT.addWidget(self.face_detection_widget)
        self.record_video.start_recording()
        connection = sqlite3.connect('mySSS.db')
        cur = connection.cursor() 
        cur.execute("SELECT * FROM Person")
        result = cur.fetchall()
        knownP=len(result)
        unknownP=sum([len(files) for r, d, files in os.walk("unknown/")])
        totalP=knownP + unknownP
        innerlayoutB = QtWidgets.QHBoxLayout()
        self.known = QtWidgets.QLabel('Known : {}'.format(knownP))
        innerlayoutB.addWidget(self.known)
        self.unknown = QtWidgets.QLabel('Unknown : {}'.format(unknownP))
        innerlayoutB.addWidget(self.unknown)
        self.total = QtWidgets.QLabel('Total : {}'.format(totalP))
        innerlayoutB.addWidget(self.total)

        layoutL.addLayout(innerlayoutT)
        layoutL.addLayout(innerlayoutB)

        layoutR = QtWidgets.QVBoxLayout()

        #self.btn_add = QtWidgets.QPushButton("ADD NEW")
        #layoutR.addWidget(self.btn_add)
        #self.btn_add.clicked.connect(self.openAddNew)

        self.btn_delete = QtWidgets.QPushButton("DELETE")
        layoutR.addWidget(self.btn_delete)
        self.btn_delete.clicked.connect(self.openDelete)

        self.btn_update = QtWidgets.QPushButton("UPDATE")
        layoutR.addWidget(self.btn_update)
        self.btn_update.clicked.connect(self.openUpdate)

        self.btn_view = QtWidgets.QPushButton("VIEW")
        layoutR.addWidget(self.btn_view)
        self.btn_view.clicked.connect(self.openView)

        self.btn_quit = QtWidgets.QPushButton("QUIT")
        layoutR.addWidget(self.btn_quit)
        self.btn_quit.clicked.connect(self.close_SSS)

        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.addLayout(layoutL)
        mainLayout.addLayout(layoutR)
        
        self.setLayout(mainLayout)

    def close_SSS(self):
        choice = QtWidgets.QMessageBox.question(self,"QuitApp","Are you sure that you want to quit the application?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass


def main(haar_cascade_filepath):
    app = QtWidgets.QApplication(sys.argv)

    main_window = QtWidgets.QMainWindow()
    main_widget = MainWidget(haar_cascade_filepath)
    main_window.setCentralWidget(main_widget)
    main_window.setWindowTitle("Smart Surveillance Security")
    main_window.setWindowIcon(QtGui.QIcon('gui/logo.png'))
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    script_dir = path.dirname(path.realpath(__file__))
    cascade_filepath = path.join(script_dir,
                                 '.',
                                 'cascades',
                                 'haarcascade_frontalface_default.xml')

    cascade_filepath = path.abspath(cascade_filepath)
    main(cascade_filepath)