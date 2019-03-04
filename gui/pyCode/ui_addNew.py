# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uiCode/addNew.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addNew(object):
    def setupUi(self, addNew):
        addNew.setObjectName("addNew")
        addNew.resize(455, 301)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        addNew.setWindowIcon(icon)
        self.formLayout = QtWidgets.QFormLayout(addNew)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(addNew)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(addNew)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.female = QtWidgets.QRadioButton(addNew)
        self.female.setObjectName("female")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.female)
        self.label_5 = QtWidgets.QLabel(addNew)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_4 = QtWidgets.QLabel(addNew)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(addNew)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
        self.name = QtWidgets.QLineEdit(addNew)
        self.name.setObjectName("name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name)
        self.cid = QtWidgets.QLineEdit(addNew)
        self.cid.setObjectName("cid")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cid)
        self.label_3 = QtWidgets.QLabel(addNew)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.male = QtWidgets.QRadioButton(addNew)
        self.male.setObjectName("male")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.male)
        self.designation = QtWidgets.QLineEdit(addNew)
        self.designation.setObjectName("designation")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.designation)

        self.retranslateUi(addNew)
        self.buttonBox.accepted.connect(addNew.accept)
        self.buttonBox.rejected.connect(addNew.reject)
        QtCore.QMetaObject.connectSlotsByName(addNew)

    def retranslateUi(self, addNew):
        _translate = QtCore.QCoreApplication.translate
        addNew.setWindowTitle(_translate("addNew", "Add New"))
        self.label.setText(_translate("addNew", "Name"))
        self.label_2.setText(_translate("addNew", "Gender"))
        self.female.setText(_translate("addNew", "Female"))
        self.label_5.setText(_translate("addNew", "Designation"))
        self.label_4.setText(_translate("addNew", "Image"))
        self.label_3.setText(_translate("addNew", "CID"))
        self.male.setText(_translate("addNew", "Male"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addNew = QtWidgets.QDialog()
    ui = Ui_addNew()
    ui.setupUi(addNew)
    addNew.show()
    sys.exit(app.exec_())

