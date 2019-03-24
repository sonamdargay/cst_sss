# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uiCode/delete.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 

class Ui_remove(QtWidgets.QMainWindow):
    def setupUi(self, remove):
        remove.setObjectName("remove")
        remove.resize(398, 277)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        remove.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(remove)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(remove)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cid = QtWidgets.QLineEdit(remove)
        self.cid.setObjectName("cid")
        self.gridLayout.addWidget(self.cid, 0, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(remove)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
            
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)
        self.retranslateUi(remove)
        self.buttonBox.accepted.connect(remove.accept)
        self.buttonBox.rejected.connect(remove.reject)
        QtCore.QMetaObject.connectSlotsByName(remove)

        self.buttonBox.accepted.connect(self.insertDelete)

    def retranslateUi(self, remove):
        _translate = QtCore.QCoreApplication.translate
        remove.setWindowTitle(_translate("remove", "Delete"))
        self.label.setText(_translate("remove", "Enter CID"))

    def insertDelete(self):
        status=1
        connection = sqlite3.connect('mySSS.db')
        cur = connection.cursor() 
        cid = self.cid.text()

        #Validating whether all the values are set or not. If set the person is added to database else not added
        if cid == "":
            status=0

        if status is 0:
            connection.close()
            QtWidgets.QMessageBox.warning(self,"Unsuccessfull","Sorry, Please enter the CID number of the person ",
                QtWidgets.QMessageBox.Ok)
        else:
            cur.execute('''DELETE FROM Person WHERE cid=?''',(cid,))
            check=cur.rowcount
            if check is 1:
                connection.commit()
                connection.close()
                QtWidgets.QMessageBox.information(self,"Successfull","You have successfully deleted a person with CID {}".format(cid),
                    QtWidgets.QMessageBox.Ok)
            else:
                connection.close()
                QtWidgets.QMessageBox.warning(self,"Unsuccessfull","Sorry, person with CID {} could not be deleted".format(cid),
                    QtWidgets.QMessageBox.Ok)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    remove = QtWidgets.QDialog()
    ui = Ui_remove()
    ui.setupUi(remove)
    remove.show()
    sys.exit(app.exec_())

