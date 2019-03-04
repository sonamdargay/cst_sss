# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uiCode/update.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_update(object):
    def setupUi(self, update):
        update.setObjectName("update")
        update.resize(388, 256)
        self.formLayout = QtWidgets.QFormLayout(update)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(update)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(update)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.name = QtWidgets.QLineEdit(update)
        self.name.setObjectName("name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name)
        self.cid = QtWidgets.QLineEdit(update)
        self.cid.setObjectName("cid")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cid)
        self.male = QtWidgets.QRadioButton(update)
        self.male.setObjectName("male")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.male)
        self.female = QtWidgets.QRadioButton(update)
        self.female.setObjectName("female")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.female)
        self.label_3 = QtWidgets.QLabel(update)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(update)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.designation = QtWidgets.QLineEdit(update)
        self.designation.setObjectName("designation")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.designation)
        self.label_5 = QtWidgets.QLabel(update)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.buttonBox = QtWidgets.QDialogButtonBox(update)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(update)
        self.buttonBox.accepted.connect(update.accept)
        self.buttonBox.rejected.connect(update.reject)
        QtCore.QMetaObject.connectSlotsByName(update)

    def retranslateUi(self, update):
        _translate = QtCore.QCoreApplication.translate
        update.setWindowTitle(_translate("update", "Update"))
        self.label.setText(_translate("update", "Name"))
        self.label_2.setText(_translate("update", "CID"))
        self.male.setText(_translate("update", "Male"))
        self.female.setText(_translate("update", "Female"))
        self.label_3.setText(_translate("update", "Gender"))
        self.label_4.setText(_translate("update", "Designation"))
        self.label_5.setText(_translate("update", "Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update = QtWidgets.QDialog()
    ui = Ui_update()
    ui.setupUi(update)
    update.show()
    sys.exit(app.exec_())

