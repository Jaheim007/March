# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'March.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1531, 997)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-30, 0, 1561, 1031))
        self.stackedWidget.setStyleSheet(u"background-color:#F7E7CE;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.Logo = QLabel(self.page)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(100, 20, 91, 81))
        self.Logo.setPixmap(QPixmap(u":/Images/Static/codebreaker.png"))
        self.Logo.setScaledContents(True)
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 40, 113, 41))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton.setFlat(True)
        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 40, 113, 41))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_2.setFlat(True)
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 150, 441, 351))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u":/Images/Static/AdobeStock_241083104-1400x934.webp"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 520, 151, 51))
        self.label_2.setStyleSheet(u"QLabel{\n"
"font: 25 16pt \"Avenir\";\n"
"}")
        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(120, 590, 351, 61))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(7, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(False)
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(830, 90, 471, 121))
        self.label_3.setStyleSheet(u"QLabel{\n"
"font: 25 25pt \"Avenir\";\n"
"}")
        self.pushButton_7 = QPushButton(self.page)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(120, 700, 351, 61))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"color: rgb(0,0,0)\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(7, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_7.setFlat(False)
        self.pushButton_8 = QPushButton(self.page)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(120, 800, 351, 61))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"color: rgb(0,0,0)\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(7, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_8.setFlat(False)
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(830, 220, 151, 51))
        self.label_4.setStyleSheet(u"QLabel{\n"
"font: 25 16pt \"Avenir\";\n"
"}")
        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(830, 270, 501, 41))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit.setClearButtonEnabled(True)
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(830, 320, 151, 51))
        self.label_5.setStyleSheet(u"QLabel{\n"
"font: 25 16pt \"Avenir\";\n"
"}")
        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(830, 370, 501, 41))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.stackedWidget_2 = QStackedWidget(self.page)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(810, 530, 611, 401))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.pushButton_4 = QPushButton(self.page_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(60, 30, 191, 141))
        self.pushButton_4.setMinimumSize(QSize(191, 141))
        self.pushButton_4.setStyleSheet(u"")
        self.pushButton_6 = QPushButton(self.page_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(60, 220, 191, 141))
        self.pushButton_9 = QPushButton(self.page_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(370, 220, 191, 141))
        self.pushButton_10 = QPushButton(self.page_3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(360, 30, 191, 141))
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget_2.addWidget(self.page_4)
        self.pushButton_11 = QPushButton(self.page)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(830, 480, 151, 51))
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"background-color: #1E90FF;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.pushButton_11.setAutoDefault(True)
        self.pushButton_11.setFlat(False)
        self.pushButton_12 = QPushButton(self.page)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(1360, 30, 151, 51))
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"background-color: #1E90FF;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.pushButton_12.setAutoDefault(True)
        self.pushButton_12.setFlat(False)
        self.pushButton_23 = QPushButton(self.page)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(820, 420, 171, 41))
        self.pushButton_23.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_23.setFlat(True)
        self.line = QFrame(self.page)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(100, 660, 391, 20))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)
        self.line_4 = QFrame(self.page)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(90, 780, 391, 3))
        self.line_4.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_5 = QFrame(self.page)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(90, 890, 391, 3))
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_6 = QFrame(self.page)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(97, 570, 391, 20))
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setFrameShape(QFrame.HLine)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.Logo_2 = QLabel(self.page_2)
        self.Logo_2.setObjectName(u"Logo_2")
        self.Logo_2.setGeometry(QRect(90, 20, 91, 81))
        self.Logo_2.setPixmap(QPixmap(u":/Images/Static/Logo.png"))
        self.Logo_2.setScaledContents(True)
        self.pushButton_13 = QPushButton(self.page_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(210, 40, 113, 41))
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_13.setFlat(True)
        self.pushButton_14 = QPushButton(self.page_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(350, 40, 113, 41))
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_14.setFlat(True)
        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(540, 140, 471, 91))
        self.label_7.setStyleSheet(u"QLabel{\n"
"font: 25 25pt \"Avenir\";\n"
"}")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(540, 440, 151, 51))
        self.label_8.setStyleSheet(u"QLabel{\n"
"font: 25 16pt \"Avenir\";\n"
"}")
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(540, 540, 151, 51))
        self.label_9.setStyleSheet(u"QLabel{\n"
"font: 25 16pt \"Avenir\";\n"
"}")
        self.lineEdit_4 = QLineEdit(self.page_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(540, 380, 501, 41))
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_5 = QLineEdit(self.page_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(540, 600, 501, 41))
        self.lineEdit_5.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_5.setEchoMode(QLineEdit.Password)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(1110, 40, 251, 51))
        self.label_10.setStyleSheet(u"QLabel{\n"
"font: 25 18pt \"Avenir\";\n"
"}")
        self.pushButton_15 = QPushButton(self.page_2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(1370, 40, 151, 51))
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"background-color:#1E90FF;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.pushButton_15.setAutoDefault(True)
        self.pushButton_15.setFlat(False)
        self.pushButton_16 = QPushButton(self.page_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(720, 690, 151, 51))
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"background-color:#1E90FF;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.pushButton_16.setAutoDefault(True)
        self.pushButton_16.setFlat(False)
        self.label_14 = QLabel(self.page_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(540, 330, 151, 51))
        self.label_14.setStyleSheet(u"QLabel{\n"
"font: 25 16pt \"Avenir\";\n"
"}")
        self.label_15 = QLabel(self.page_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(540, 220, 151, 51))
        self.label_15.setStyleSheet(u"QLabel{\n"
"font: 25 16pt \"Avenir\";\n"
"}")
        self.lineEdit_6 = QLineEdit(self.page_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(540, 490, 501, 41))
        self.lineEdit_6.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_6.setEchoMode(QLineEdit.Password)
        self.lineEdit_6.setClearButtonEnabled(True)
        self.lineEdit_7 = QLineEdit(self.page_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(540, 270, 501, 41))
        self.lineEdit_7.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.lineEdit_7.setEchoMode(QLineEdit.Password)
        self.lineEdit_7.setClearButtonEnabled(True)
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.Logo_5 = QLabel(self.page_5)
        self.Logo_5.setObjectName(u"Logo_5")
        self.Logo_5.setGeometry(QRect(50, 30, 91, 81))
        self.Logo_5.setPixmap(QPixmap(u":/Images/Static/Logo.png"))
        self.Logo_5.setScaledContents(True)
        self.pushButton_18 = QPushButton(self.page_5)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(180, 50, 113, 41))
        self.pushButton_18.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_18.setFlat(True)
        self.pushButton_19 = QPushButton(self.page_5)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(330, 50, 113, 41))
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_19.setFlat(True)
        self.stackedWidget_3 = QStackedWidget(self.page_5)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setGeometry(QRect(400, 140, 1051, 841))
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.pushButton_20 = QPushButton(self.page_6)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(80, 130, 113, 32))
        self.pushButton_21 = QPushButton(self.page_6)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(380, 110, 301, 321))
        self.pushButton_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_21.setFlat(True)
        self.pushButton_22 = QPushButton(self.page_6)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(110, 440, 113, 32))
        self.label_13 = QLabel(self.page_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(40, 20, 291, 61))
        self.label_13.setStyleSheet(u"QLabel{\n"
"font: 87 20pt \"Avenir\";\n"
"}")
        self.stackedWidget_3.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.stackedWidget_3.addWidget(self.page_7)
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(50, 170, 291, 61))
        self.label_11.setStyleSheet(u"QLabel{\n"
"font: 25 30pt \"Avenir\";\n"
"}")
        self.pushButton_24 = QPushButton(self.page_5)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(30, 250, 141, 41))
        self.pushButton_24.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_24.setIconSize(QSize(100, 100))
        self.pushButton_24.setFlat(True)
        self.pushButton_25 = QPushButton(self.page_5)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setGeometry(QRect(30, 450, 113, 41))
        self.pushButton_25.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_25.setFlat(True)
        self.pushButton_26 = QPushButton(self.page_5)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(30, 300, 113, 41))
        self.pushButton_26.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_26.setFlat(True)
        self.pushButton_27 = QPushButton(self.page_5)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setGeometry(QRect(40, 350, 113, 41))
        self.pushButton_27.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_27.setFlat(True)
        self.pushButton_28 = QPushButton(self.page_5)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setGeometry(QRect(20, 400, 113, 41))
        self.pushButton_28.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_28.setFlat(True)
        self.label_12 = QLabel(self.page_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 530, 291, 61))
        self.label_12.setStyleSheet(u"QLabel{\n"
"font: 25 30pt \"Avenir\";\n"
"}")
        self.pushButton_29 = QPushButton(self.page_5)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(20, 680, 241, 41))
        self.pushButton_29.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_29.setIconSize(QSize(100, 100))
        self.pushButton_29.setFlat(True)
        self.pushButton_30 = QPushButton(self.page_5)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(20, 740, 201, 41))
        self.pushButton_30.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_30.setFlat(True)
        self.pushButton_33 = QPushButton(self.page_5)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setGeometry(QRect(20, 800, 201, 41))
        self.pushButton_33.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_33.setFlat(True)
        self.pushButton_34 = QPushButton(self.page_5)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setGeometry(QRect(20, 620, 201, 41))
        self.pushButton_34.setStyleSheet(u"QPushButton{\n"
"font: 25 16pt \"Avenir\";\n"
"}\n"
"QPushButton::hover{\n"
"color: rgb(7, 0, 255);\n"
"}")
        self.pushButton_34.setFlat(True)
        self.stackedWidget.addWidget(self.page_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_3.setDefault(True)
        self.pushButton_7.setDefault(True)
        self.pushButton_8.setDefault(True)
        self.pushButton_11.setDefault(True)
        self.pushButton_12.setDefault(True)
        self.pushButton_15.setDefault(True)
        self.pushButton_16.setDefault(True)
        self.pushButton_21.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Logo.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Catalogue", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Resources", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Quel est ton but?</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Construisez votre carri\u00e8re", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Entrez gratuitement dans le monde de la </p><p>programmation avec Code Breaker</p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Apprendre un langage de programmation", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Acqu\u00e9rir une comp\u00e9tence", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton_4.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"iugduyggf", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Mot de passe oubli\u00e9?", None))
        self.Logo_2.setText("")
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Catalogue", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Resources", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Connectez-vous \u00e0 Code Breaker</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Email</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Vous n'avez pas de compte ?</p></body></html>", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Prenom</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Nom</span></p></body></html>", None))
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.Logo_5.setText("")
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Catalogue", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Resources", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_21.setText("")
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Le plus populaire</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Langue</span></p></body></html>", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u" \u2022 HTML & CSS", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u" \u2022 Flutter", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u" \u2022 Python", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u" \u2022 JavaScript", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u" \u2022 PHP", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Carri\u00e8re</span></p></body></html>", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u" \u2022 Scientifique des donn\u00e9es", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u" \u2022 Front-End Ing\u00e9nieur", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u" \u2022 Full-Stack Ing\u00e9nieur", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u" \u2022 Computer science", None))
    # retranslateUi

