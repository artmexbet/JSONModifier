# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\JSONModifier\design/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(244, 334)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.create_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.create_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_btn.setFont(font)
        self.create_btn.setObjectName("create_btn")
        self.gridLayout.addWidget(self.create_btn, 1, 0, 1, 1)
        self.open_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.open_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.open_btn.setFont(font)
        self.open_btn.setObjectName("open_btn")
        self.gridLayout.addWidget(self.open_btn, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.exit_btn.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")
        self.gridLayout.addWidget(self.exit_btn, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.create_btn.setText(_translate("MainWindow", "Создать"))
        self.open_btn.setText(_translate("MainWindow", "Открыть"))
        self.label.setText(_translate("MainWindow", "JSON"))
        self.exit_btn.setText(_translate("MainWindow", "Выйти"))