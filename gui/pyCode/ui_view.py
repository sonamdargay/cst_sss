# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uiCode/view.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui_details import Ui_Details
import sqlite3

class Ui_view(QtWidgets.QMainWindow):

    def openDetails(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Details()
        self.ui.setupUi(self.window)
        self.ui.name.setText(self.rows[0])
        self.ui.cid.setText(self.rows[1])
        self.ui.gender.setText(self.rows[3])
        self.ui.designation.setText(self.rows[2])
        img=self.rows[4]

        scene = QtWidgets.QGraphicsScene() 
        pic = QtGui.QPixmap(img) 
        scene.addItem(QtWidgets.QGraphicsPixmapItem(pic)) 
        view = self.ui.image
        view.setScene(scene) 
        view.setRenderHint(QtGui.QPainter.Antialiasing) 
        #view.show() 
        self.window.show()


    def setupUi(self, view):
        view.setObjectName("view")
        view.resize(398, 227)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        view.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(view)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(view)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cid = QtWidgets.QLineEdit(view)
        self.cid.setObjectName("CID")
        self.gridLayout.addWidget(self.cid, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(view)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.retranslateUi(view)
        self.buttonBox.accepted.connect(view.accept)
        self.buttonBox.rejected.connect(view.reject)
        QtCore.QMetaObject.connectSlotsByName(view)

        self.buttonBox.accepted.connect(self.viewUpdate)

        self.rows=None

    def retranslateUi(self, view):
        _translate = QtCore.QCoreApplication.translate
        view.setWindowTitle(_translate("view", "View Details"))
        self.label.setText(_translate("view", "Enter CID"))

    def viewUpdate(self):
            status=1
            connection = sqlite3.connect('mySSS.db')
            cur = connection.cursor() 
            cid = self.cid.text()
        
            #Validating whether all the values are set or not. If set the person is added to database else not added
            if cid == "":
                status=0

            if status is 0:
                connection.close()
                QtWidgets.QMessageBox.warning(self,"Unsuccessfull","Sorry, Please give CID number to view the information",
                    QtWidgets.QMessageBox.Ok)
            else:
                cur.execute('''SELECT * FROM Person WHERE cid=?''',(cid,))
                self.rows = cur.fetchone()
                if self.rows is None:
                    connection.close()
                    QtWidgets.QMessageBox.warning(self,"Unsuccessfull","Sorry, We don't have any information about {}".format(cid),
                        QtWidgets.QMessageBox.Ok)
                else:
                    connection.commit()
                    self.openDetails()
                    connection.close()
                    #QtWidgets.QMessageBox.information(self,"Successfull","This is the person information about {}".format(cid),
                    #    QtWidgets.QMessageBox.Ok)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view = QtWidgets.QDialog()
    ui = Ui_view()
    ui.setupUi(view)
    view.show()
    sys.exit(app.exec_())

