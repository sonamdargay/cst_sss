# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uiCode/details.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Details(QtWidgets.QMainWindow):

    def setupUi(self, Details):
        Details.setObjectName("Details")
        Details.resize(430, 437)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../pyCode/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Details.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Details)
        self.gridLayout.setObjectName("gridLayout")
        self.image = QtWidgets.QGraphicsView(Details)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(Details)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 2, 1)
        self.name = QtWidgets.QLineEdit(Details)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 1, 1, 1)
        self.cid = QtWidgets.QLineEdit(Details)
        self.cid.setObjectName("cid")
        self.gridLayout.addWidget(self.cid, 2, 1, 2, 1)
        self.label_2 = QtWidgets.QLabel(Details)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Details)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.gender = QtWidgets.QLineEdit(Details)
        self.gender.setObjectName("gender")
        self.gridLayout.addWidget(self.gender, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Details)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.designation = QtWidgets.QLineEdit(Details)
        self.designation.setObjectName("designation")
        self.gridLayout.addWidget(self.designation, 5, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Details)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 1, 1, 1)
        '''
        scene = QtWidgets.QGraphicsScene() 
        pic = QtGui.QPixmap("suraj.jpg") 
        scene.addItem(QtWidgets.QGraphicsPixmapItem(pic)) 
        view = self.image
        view.setScene(scene) 
        view.setRenderHint(QtGui.QPainter.Antialiasing) 
        view.show() 
        '''
        self.retranslateUi(Details)
        self.buttonBox.accepted.connect(Details.accept)
        QtCore.QMetaObject.connectSlotsByName(Details)

    def retranslateUi(self, Details):
        _translate = QtCore.QCoreApplication.translate
        Details.setWindowTitle(_translate("Details", "Person Details"))
        self.label.setText(_translate("Details", "Name"))
        self.label_2.setText(_translate("Details", "CID"))
        self.label_3.setText(_translate("Details", "Gender"))
        self.label_4.setText(_translate("Details", "designation"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Details = QtWidgets.QDialog()
    ui = Ui_Details()
    ui.setupUi(Details)
    Details.show()
    sys.exit(app.exec_())

