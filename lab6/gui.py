# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 180)
        MainWindow.setMinimumSize(QtCore.QSize(500, 180))
        MainWindow.setMaximumSize(QtCore.QSize(500, 180))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text1 = QtWidgets.QTextEdit(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(10, 10, 211, 161))
        self.text1.setObjectName("text1")
        self.text2 = QtWidgets.QTextEdit(self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(280, 10, 211, 161))
        self.text2.setObjectName("text2")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(230, 70, 41, 41))
        self.btn.setObjectName("btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.createMB = QtWidgets.QAction(MainWindow)
        self.createMB.setObjectName("createMB")
        self.openMB = QtWidgets.QAction(MainWindow)
        self.openMB.setObjectName("openMB")
        self.saveMB = QtWidgets.QAction(MainWindow)
        self.saveMB.setObjectName("saveMB")
        self.saveAsMB = QtWidgets.QAction(MainWindow)
        self.saveAsMB.setObjectName("saveAsMB")
        self.exitMB = QtWidgets.QAction(MainWindow)
        self.exitMB.setObjectName("exitMB")
        self.infoMB = QtWidgets.QAction(MainWindow)
        self.infoMB.setObjectName("infoMB")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn.setText(_translate("MainWindow", "->"))
        self.createMB.setText(_translate("MainWindow", "Создать"))
        self.openMB.setText(_translate("MainWindow", "Открыть"))
        self.saveMB.setText(_translate("MainWindow", "Сохранить"))
        self.saveAsMB.setText(_translate("MainWindow", "Сохранить как..."))
        self.exitMB.setText(_translate("MainWindow", "Выход"))
        self.infoMB.setText(_translate("MainWindow", "О разработчике"))