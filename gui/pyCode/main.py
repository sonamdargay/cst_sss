# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uiCode/main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost

import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_addNew import Ui_addNew
from ui_update import Ui_update
from ui_delete import Ui_remove
from ui_view import Ui_view
from recogniser import *

class Ui_MainWindow(QtWidgets.QMainWindow):
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

    def openView(self):
        self.viewDialog = QtWidgets.QDialog()
        self.ui = Ui_view()
        self.ui.setupUi(self.viewDialog)
        self.viewDialog.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(285, 384)
        MainWindow.setMinimumSize(QtCore.QSize(285, 384))
        MainWindow.setMaximumSize(QtCore.QSize(285, 384))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.btn_play = QtWidgets.QPushButton(self.centralwidget)
        self.btn_play.setObjectName("btn_play")
        self.verticalLayout_2.addWidget(self.btn_play)
        self.btn_play.clicked.connect(VideoPlayer)

        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout_2.addWidget(self.btn_add)
        self.btn_add.clicked.connect(self.openAddNew)

        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setObjectName("btn_delete")
        self.verticalLayout_2.addWidget(self.btn_delete)
        self.btn_delete.clicked.connect(self.openDelete)

        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setObjectName("btn_update")
        self.verticalLayout_2.addWidget(self.btn_update)
        self.btn_update.clicked.connect(self.openUpdate)

        self.btn_view = QtWidgets.QPushButton(self.centralwidget)
        self.btn_view.setObjectName("btn_view")
        self.verticalLayout_2.addWidget(self.btn_view)
        self.btn_view.clicked.connect(self.openView)

        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout_2.addWidget(self.btn_exit)
        self.btn_exit.clicked.connect(self.close_SSS)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 285, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smart Security Survellance"))
        self.btn_play.setText(_translate("MainWindow", "PLAY VIDEO"))
        self.btn_add.setText(_translate("MainWindow", "ADD NEW"))
        self.btn_delete.setText(_translate("MainWindow", "DELETE"))
        self.btn_update.setText(_translate("MainWindow", "UPDATE"))
        self.btn_view.setText(_translate("MainWindow", "VIEW"))
        self.btn_exit.setText(_translate("MainWindow", "EXIT"))


    def close_SSS(self):
        choice = QtWidgets.QMessageBox.question(self,"QuitApp","Are you sure that you want to quit the application?",
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

