# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'details.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Details(object):
    def setupUi(self, Details):
        Details.setObjectName("Details")
        Details.resize(459, 566)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../pyCode/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Details.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Details)
        self.widget.setGeometry(QtCore.QRect(52, 11, 345, 547))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.image = QtWidgets.QGraphicsView(self.widget)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.widget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.cid = QtWidgets.QLineEdit(self.widget)
        self.cid.setObjectName("cid")
        self.gridLayout.addWidget(self.cid, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.gender = QtWidgets.QLineEdit(self.widget)
        self.gender.setObjectName("gender")
        self.gridLayout.addWidget(self.gender, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.designation = QtWidgets.QLineEdit(self.widget)
        self.designation.setObjectName("designation")
        self.gridLayout.addWidget(self.designation, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.time_log = QtWidgets.QTextEdit(self.widget)
        self.time_log.setObjectName("time_log")
        self.gridLayout.addWidget(self.time_log, 5, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 1, 1, 1)

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
        self.label_5.setText(_translate("Details", "Time Log"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Details = QtWidgets.QDialog()
    ui = Ui_Details()
    ui.setupUi(Details)
    Details.show()
    sys.exit(app.exec_())

