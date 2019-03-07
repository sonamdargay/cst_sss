# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sss.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
#import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_addNew import Ui_addNew
from ui_update import Ui_update
from ui_delete import Ui_remove
from ui_view import Ui_view

class Ui_mainWindow(QtWidgets.QMainWindow):
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
        #conn = sqlite3.connect('mySSS.db')
        #cur = conn.cursor() 
        #cids=self.ui.cid.text()
        #print(type(cids))
        #cids="qsdf"
        #print(cids)
        #cur.execute('''INSERT INTO sample(cid) VALUES(?)''',(cids,))
        #conn.commit()
        #conn.close()


    def openView(self):
        self.viewDialog = QtWidgets.QDialog()
        self.ui = Ui_view()
        self.ui.setupUi(self.viewDialog)
        self.viewDialog.show()

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(769, 472)
        mainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setObjectName("btn_add")
        self.btn_add.clicked.connect(self.openAddNew)

        self.verticalLayout.addWidget(self.btn_add)
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.clicked.connect(self.openDelete)

        self.verticalLayout.addWidget(self.btn_delete)
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setObjectName("btn_update")
        self.btn_update.clicked.connect(self.openUpdate)

        self.verticalLayout.addWidget(self.btn_update)
        self.btn_view = QtWidgets.QPushButton(self.centralwidget)
        self.btn_view.setObjectName("btn_view")
        self.btn_view.clicked.connect(self.openView)

        self.verticalLayout.addWidget(self.btn_view)
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setDefault(False)
        self.btn_exit.setFlat(False)
        self.btn_exit.setObjectName("btn_exit")
        #self.btn_exit.clicked.connect(QtWidgets.QApplication.instance().quit)
        self.btn_exit.clicked.connect(self.close_SSS)

        self.verticalLayout.addWidget(self.btn_exit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Smart Security Surveillance"))
        self.btn_add.setText(_translate("mainWindow", "ADD NEW"))
        self.btn_delete.setText(_translate("mainWindow", "DELETE"))
        self.btn_update.setText(_translate("mainWindow", "UPDATE"))
        self.btn_view.setText(_translate("mainWindow", "VIEW"))
        self.btn_exit.setText(_translate("mainWindow", "EXIT"))

    def close_SSS(self):
        choice = QtWidgets.QMessageBox.question(self,"QuitApp","Are you sure to quit?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

