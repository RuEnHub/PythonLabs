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
        MainWindow.resize(500, 250)
        MainWindow.setMinimumSize(QtCore.QSize(500, 250))
        MainWindow.setMaximumSize(QtCore.QSize(500, 250))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(290, 220, 61, 23))
        self.addBtn.setObjectName("addBtn")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(290, 10, 201, 197))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.code = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.code.setText("")
        self.code.setObjectName("code")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.code)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.body_type = QtWidgets.QComboBox(self.formLayoutWidget)
        self.body_type.setObjectName("body_type")
        self.body_type.addItem("")
        self.body_type.addItem("")
        self.body_type.addItem("")
        self.body_type.addItem("")
        self.body_type.addItem("")
        self.body_type.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.body_type)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.price = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.price.setMinimum(10000)
        self.price.setMaximum(10000000)
        self.price.setObjectName("price")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.price)
        self.radio = QtWidgets.QVBoxLayout()
        self.radio.setObjectName("radio")
        self.radioButton_2 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radio.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_3.setChecked(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radio.addWidget(self.radioButton_3)
        self.radioButton = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.radio.addWidget(self.radioButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.radio)
        self.year = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.year.setMinimum(1990)
        self.year.setMaximum(2021)
        self.year.setObjectName("year")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.year)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.model = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.model.setObjectName("model")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.model)
        self.delBtn = QtWidgets.QPushButton(self.centralwidget)
        self.delBtn.setGeometry(QtCore.QRect(360, 220, 61, 23))
        self.delBtn.setObjectName("delBtn")
        self.searchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.searchBtn.setGeometry(QtCore.QRect(430, 220, 61, 23))
        self.searchBtn.setObjectName("searchBtn")
        self.myList = QtWidgets.QListWidget(self.centralwidget)
        self.myList.setGeometry(QtCore.QRect(10, 10, 261, 231))
        self.myList.setObjectName("myList")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addBtn.setText(_translate("MainWindow", "Добавить"))
        self.label.setText(_translate("MainWindow", "Код"))
        self.label_2.setText(_translate("MainWindow", "Марка"))
        self.label_3.setText(_translate("MainWindow", "Год выпуска"))
        self.label_4.setText(_translate("MainWindow", "Тип кузова"))
        self.body_type.setItemText(0, _translate("MainWindow", "Седан"))
        self.body_type.setItemText(1, _translate("MainWindow", "Внедорожник"))
        self.body_type.setItemText(2, _translate("MainWindow", "Купе"))
        self.body_type.setItemText(3, _translate("MainWindow", "Универсал"))
        self.body_type.setItemText(4, _translate("MainWindow", "Кабриолет"))
        self.body_type.setItemText(5, _translate("MainWindow", "Лимузин"))
        self.label_5.setText(_translate("MainWindow", "Стоимость"))
        self.radioButton_2.setText(_translate("MainWindow", "BMW"))
        self.radioButton_3.setText(_translate("MainWindow", "Mercedes"))
        self.radioButton.setText(_translate("MainWindow", "Lada"))
        self.label_6.setText(_translate("MainWindow", "Модель"))
        self.delBtn.setText(_translate("MainWindow", "Удалить"))
        self.searchBtn.setText(_translate("MainWindow", "Поиск"))
