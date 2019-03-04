# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uiCode/view.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_view(object):
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
        self.lineEdit = QtWidgets.QLineEdit(view)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(view)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.retranslateUi(view)
        self.buttonBox.accepted.connect(view.accept)
        self.buttonBox.rejected.connect(view.reject)
        QtCore.QMetaObject.connectSlotsByName(view)

    def retranslateUi(self, view):
        _translate = QtCore.QCoreApplication.translate
        view.setWindowTitle(_translate("view", "View Details"))
        self.label.setText(_translate("view", "Enter CID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view = QtWidgets.QDialog()
    ui = Ui_view()
    ui.setupUi(view)
    view.show()
    sys.exit(app.exec_())

