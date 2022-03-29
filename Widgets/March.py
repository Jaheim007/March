# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/March.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1531, 997)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-30, 0, 1561, 1031))
        self.stackedWidget.setStyleSheet("background-color:#F7E7CE;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.Logo = QtWidgets.QLabel(self.page)
        self.Logo.setGeometry(QtCore.QRect(100, 20, 91, 81))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap(":/Images/Static/Logo.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setObjectName("Logo")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(220, 40, 113, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.page)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 40, 113, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(110, 150, 441, 351))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Images/Static/AdobeStock_241083104-1400x934.webp"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(110, 520, 151, 51))
        self.label_2.setStyleSheet("QLabel{\n"
"font: 25 16pt \"Avenir\";\n"
"}")
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.page)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 590, 351, 61))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(7, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(830, 90, 471, 121))
        self.label_3.setStyleSheet("QLabel{\n"
"font: 25 25pt \"Avenir\";\n"
"}")
        self.label_3.setObjectName("label_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.page)
        self.pushButton_7.setGeometry(QtCore.QRect(120, 700, 351, 61))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"color: rgb(0,0,0)\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(7, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.page)
        self.pushButton_8.setGeometry(QtCore.QRect(120, 800, 351, 61))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"color: rgb(0,0,0)\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(7, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(830, 220, 151, 51))
        self.label_4.setStyleSheet("QLabel{\n"
"font: 25 16pt \"Avenir\";\n"
"}")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(830, 270, 501, 41))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(830, 320, 151, 51))
        self.label_5.setStyleSheet("QLabel{\n"
"font: 25 16pt \"Avenir\";\n"
"}")
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page)
        self.lineEdit_2.setGeometry(QtCore.QRect(830, 370, 501, 41))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page)
        self.stackedWidget_2.setGeometry(QtCore.QRect(810, 530, 611, 401))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 30, 191, 141))
        self.pushButton_4.setMinimumSize(QtCore.QSize(191, 141))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 220, 191, 141))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_9.setGeometry(QtCore.QRect(370, 220, 191, 141))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_10.setGeometry(QtCore.QRect(360, 30, 191, 141))
        self.pushButton_10.setObjectName("pushButton_10")
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget_2.addWidget(self.page_4)
        self.pushButton_11 = QtWidgets.QPushButton(self.page)
        self.pushButton_11.setGeometry(QtCore.QRect(830, 480, 151, 51))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"background-color: #1E90FF;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.pushButton_11.setAutoDefault(True)
        self.pushButton_11.setDefault(True)
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.page)
        self.pushButton_12.setGeometry(QtCore.QRect(1360, 30, 151, 51))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"background-color: #1E90FF;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.pushButton_12.setAutoDefault(True)
        self.pushButton_12.setDefault(True)
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_23 = QtWidgets.QPushButton(self.page)
        self.pushButton_23.setGeometry(QtCore.QRect(820, 420, 171, 41))
        self.pushButton_23.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_23.setFlat(True)
        self.pushButton_23.setObjectName("pushButton_23")
        self.line = QtWidgets.QFrame(self.page)
        self.line.setGeometry(QtCore.QRect(100, 660, 391, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.line_4 = QtWidgets.QFrame(self.page)
        self.line_4.setGeometry(QtCore.QRect(90, 780, 391, 3))
        self.line_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.page)
        self.line_5.setGeometry(QtCore.QRect(90, 890, 391, 3))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.page)
        self.line_6.setGeometry(QtCore.QRect(97, 570, 391, 20))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.Logo_2 = QtWidgets.QLabel(self.page_2)
        self.Logo_2.setGeometry(QtCore.QRect(90, 20, 91, 81))
        self.Logo_2.setText("")
        self.Logo_2.setPixmap(QtGui.QPixmap(":/Images/Static/Logo.png"))
        self.Logo_2.setScaledContents(True)
        self.Logo_2.setObjectName("Logo_2")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_13.setGeometry(QtCore.QRect(210, 40, 113, 41))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_13.setFlat(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_14.setGeometry(QtCore.QRect(350, 40, 113, 41))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_14.setFlat(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_7 = QtWidgets.QLabel(self.page_2)
        self.label_7.setGeometry(QtCore.QRect(540, 140, 471, 91))
        self.label_7.setStyleSheet("QLabel{\n"
"font: 25 25pt \"Avenir\";\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(540, 440, 151, 51))
        self.label_8.setStyleSheet("QLabel{\n"
"font: 25 16pt \"Avenir\";\n"
"}")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.page_2)
        self.label_9.setGeometry(QtCore.QRect(540, 540, 151, 51))
        self.label_9.setStyleSheet("QLabel{\n"
"font: 25 16pt \"Avenir\";\n"
"}")
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(540, 380, 501, 41))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(540, 600, 501, 41))
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_10 = QtWidgets.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(1110, 40, 251, 51))
        self.label_10.setStyleSheet("QLabel{\n"
"font: 25 18pt \"Avenir\";\n"
"}")
        self.label_10.setObjectName("label_10")
        self.pushButton_15 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_15.setGeometry(QtCore.QRect(1370, 40, 151, 51))
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"background-color:#1E90FF;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.pushButton_15.setAutoDefault(True)
        self.pushButton_15.setDefault(True)
        self.pushButton_15.setFlat(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_16.setGeometry(QtCore.QRect(720, 690, 151, 51))
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"background-color:#1E90FF;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.pushButton_16.setAutoDefault(True)
        self.pushButton_16.setDefault(True)
        self.pushButton_16.setFlat(False)
        self.pushButton_16.setObjectName("pushButton_16")
        self.label_14 = QtWidgets.QLabel(self.page_2)
        self.label_14.setGeometry(QtCore.QRect(540, 330, 151, 51))
        self.label_14.setStyleSheet("QLabel{\n"
"font: 25 16pt \"Avenir\";\n"
"}")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.page_2)
        self.label_15.setGeometry(QtCore.QRect(540, 220, 151, 51))
        self.label_15.setStyleSheet("QLabel{\n"
"font: 25 16pt \"Avenir\";\n"
"}")
        self.label_15.setObjectName("label_15")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(540, 490, 501, 41))
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setClearButtonEnabled(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.page_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(540, 270, 501, 41))
        self.lineEdit_7.setStyleSheet("QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_7.setClearButtonEnabled(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.Logo_5 = QtWidgets.QLabel(self.page_5)
        self.Logo_5.setGeometry(QtCore.QRect(50, 30, 91, 81))
        self.Logo_5.setText("")
        self.Logo_5.setPixmap(QtGui.QPixmap(":/Images/Static/Logo.png"))
        self.Logo_5.setScaledContents(True)
        self.Logo_5.setObjectName("Logo_5")
        self.pushButton_18 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_18.setGeometry(QtCore.QRect(180, 50, 113, 41))
        self.pushButton_18.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_18.setFlat(True)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_19.setGeometry(QtCore.QRect(330, 50, 113, 41))
        self.pushButton_19.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_19.setFlat(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.page_5)
        self.stackedWidget_3.setGeometry(QtCore.QRect(400, 140, 1051, 841))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.pushButton_20 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_20.setGeometry(QtCore.QRect(80, 130, 113, 32))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_21.setGeometry(QtCore.QRect(380, 110, 301, 321))
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setText("")
        self.pushButton_21.setDefault(True)
        self.pushButton_21.setFlat(True)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.page_6)
        self.pushButton_22.setGeometry(QtCore.QRect(110, 440, 113, 32))
        self.pushButton_22.setObjectName("pushButton_22")
        self.label_13 = QtWidgets.QLabel(self.page_6)
        self.label_13.setGeometry(QtCore.QRect(40, 20, 291, 61))
        self.label_13.setStyleSheet("QLabel{\n"
"font: 87 20pt \"Avenir\";\n"
"}")
        self.label_13.setObjectName("label_13")
        self.stackedWidget_3.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.stackedWidget_3.addWidget(self.page_7)
        self.label_11 = QtWidgets.QLabel(self.page_5)
        self.label_11.setGeometry(QtCore.QRect(50, 170, 291, 61))
        self.label_11.setStyleSheet("QLabel{\n"
"font: 25 30pt \"Avenir\";\n"
"}")
        self.label_11.setObjectName("label_11")
        self.pushButton_24 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_24.setGeometry(QtCore.QRect(30, 250, 141, 41))
        self.pushButton_24.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_24.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_24.setFlat(True)
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_25.setGeometry(QtCore.QRect(30, 450, 113, 41))
        self.pushButton_25.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_25.setFlat(True)
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_26.setGeometry(QtCore.QRect(30, 300, 113, 41))
        self.pushButton_26.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_26.setFlat(True)
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_27.setGeometry(QtCore.QRect(40, 350, 113, 41))
        self.pushButton_27.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_27.setFlat(True)
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_28.setGeometry(QtCore.QRect(20, 400, 113, 41))
        self.pushButton_28.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_28.setFlat(True)
        self.pushButton_28.setObjectName("pushButton_28")
        self.label_12 = QtWidgets.QLabel(self.page_5)
        self.label_12.setGeometry(QtCore.QRect(50, 530, 291, 61))
        self.label_12.setStyleSheet("QLabel{\n"
"font: 25 30pt \"Avenir\";\n"
"}")
        self.label_12.setObjectName("label_12")
        self.pushButton_29 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_29.setGeometry(QtCore.QRect(20, 680, 241, 41))
        self.pushButton_29.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_29.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_29.setFlat(True)
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_30.setGeometry(QtCore.QRect(20, 740, 201, 41))
        self.pushButton_30.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_30.setFlat(True)
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_33 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_33.setGeometry(QtCore.QRect(20, 800, 201, 41))
        self.pushButton_33.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_33.setFlat(True)
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.page_5)
        self.pushButton_34.setGeometry(QtCore.QRect(20, 620, 201, 41))
        self.pushButton_34.setStyleSheet("QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_34.setFlat(True)
        self.pushButton_34.setObjectName("pushButton_34")
        self.stackedWidget.addWidget(self.page_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Catalogue"))
        self.pushButton_2.setText(_translate("MainWindow", "Resources"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Quel est ton but?</span></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "Construisez votre carrière"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Entrez gratuitement dans le monde de la </p><p>programmation avec Code Breaker</p></body></html>"))
        self.pushButton_7.setText(_translate("MainWindow", "Apprendre un langage de programmation"))
        self.pushButton_8.setText(_translate("MainWindow", "Acquérir une compétence"))
        self.label_4.setText(_translate("MainWindow", "Email"))
        self.label_5.setText(_translate("MainWindow", "Password"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_10.setText(_translate("MainWindow", "iugduyggf"))
        self.pushButton_11.setText(_translate("MainWindow", "Log In"))
        self.pushButton_12.setText(_translate("MainWindow", "Sign Up"))
        self.pushButton_23.setText(_translate("MainWindow", "Mot de passe oublié?"))
        self.pushButton_13.setText(_translate("MainWindow", "Catalogue"))
        self.pushButton_14.setText(_translate("MainWindow", "Resources"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Connectez-vous à Code Breaker</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Email</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "Password"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>Vous n\'avez pas de compte ?</p></body></html>"))
        self.pushButton_15.setText(_translate("MainWindow", "Log In"))
        self.pushButton_16.setText(_translate("MainWindow", "Sign Up"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Prenom</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Nom</span></p></body></html>"))
        self.pushButton_18.setText(_translate("MainWindow", "Catalogue"))
        self.pushButton_19.setText(_translate("MainWindow", "Resources"))
        self.pushButton_20.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_22.setText(_translate("MainWindow", "PushButton"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p>Le plus populaire</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Langue</span></p></body></html>"))
        self.pushButton_24.setText(_translate("MainWindow", " • HTML & CSS"))
        self.pushButton_25.setText(_translate("MainWindow", " • Flutter"))
        self.pushButton_26.setText(_translate("MainWindow", " • Python"))
        self.pushButton_27.setText(_translate("MainWindow", " • JavaScript"))
        self.pushButton_28.setText(_translate("MainWindow", " • PHP"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" text-decoration: underline;\">Carrière</span></p></body></html>"))
        self.pushButton_29.setText(_translate("MainWindow", " • Scientifique des données"))
        self.pushButton_30.setText(_translate("MainWindow", " • Front-End Ingénieur"))
        self.pushButton_33.setText(_translate("MainWindow", " • Full-Stack Ingénieur"))
        self.pushButton_34.setText(_translate("MainWindow", " • Computer science"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
