# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\JSONModifier\design/write.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(775, 598)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.value = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.value.setFont(font)
        self.value.setObjectName("value")
        self.gridLayout.addWidget(self.value, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.expression = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.expression.setFont(font)
        self.expression.setObjectName("expression")
        self.gridLayout.addWidget(self.expression, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 3)
        self.execute = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.execute.setFont(font)
        self.execute.setObjectName("execute")
        self.gridLayout.addWidget(self.execute, 1, 2, 1, 1)
        self.to_read_btn = QtWidgets.QPushButton(Dialog)
        self.to_read_btn.setObjectName("to_read_btn")
        self.gridLayout.addWidget(self.to_read_btn, 4, 0, 1, 3)
        self.output = QtWidgets.QTextEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output.setFont(font)
        self.output.setObjectName("output")
        self.gridLayout.addWidget(self.output, 3, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "????????????????:"))
        self.label.setText(_translate("Dialog", "???????????? ??????????????:"))
        self.execute.setText(_translate("Dialog", "??????????????????"))
        self.to_read_btn.setText(_translate("Dialog", "????????????"))
