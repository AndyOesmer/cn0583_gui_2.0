# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cn0583_design.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1003, 679)
        self.main = QWidget(MainWindow)
        self.main.setObjectName(u"main")
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main_frame = QFrame(self.main)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"background-color: rgb(250, 250, 250);\n"
"border-color: rgb(250, 250, 250);")
        self.main_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gui_title = QFrame(self.main_frame)
        self.gui_title.setObjectName(u"gui_title")
        self.gui_title.setMaximumSize(QSize(16777215, 60))
        self.gui_title.setStyleSheet(u"background-color: rgb(0, 103, 185);\n"
"border-color: rgb(0, 103, 185);")
        self.gui_title.setFrameShape(QFrame.Shape.StyledPanel)
        self.gui_title.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.gui_title)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.gui_title)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.GUI_Name = QLabel(self.frame)
        self.GUI_Name.setObjectName(u"GUI_Name")
        font = QFont()
        font.setFamilies([u"Barlow"])
        font.setPointSize(19)
        font.setBold(True)
        self.GUI_Name.setFont(font)
        self.GUI_Name.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.GUI_Name)


        self.horizontalLayout.addWidget(self.frame)

        self.space = QFrame(self.gui_title)
        self.space.setObjectName(u"space")
        self.space.setFrameShape(QFrame.Shape.StyledPanel)
        self.space.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.space)

        self.frame_3 = QFrame(self.gui_title)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(50, 16777215))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.for_ADI_logo = QLabel(self.frame_3)
        self.for_ADI_logo.setObjectName(u"for_ADI_logo")
        self.for_ADI_logo.setMaximumSize(QSize(25, 30))
        self.for_ADI_logo.setPixmap(QPixmap(u"../../Users/aoesmer/Downloads/Analog-devices.jpg"))
        self.for_ADI_logo.setScaledContents(True)
        self.for_ADI_logo.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.for_ADI_logo)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.gui_title)

        self.body = QFrame(self.main_frame)
        self.body.setObjectName(u"body")
        self.body.setFrameShape(QFrame.Shape.StyledPanel)
        self.body.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.body)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.controls_frame = QFrame(self.body)
        self.controls_frame.setObjectName(u"controls_frame")
        self.controls_frame.setMaximumSize(QSize(250, 16777215))
        self.controls_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.controls_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.controls_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.controls_title = QFrame(self.controls_frame)
        self.controls_title.setObjectName(u"controls_title")
        self.controls_title.setMaximumSize(QSize(16777215, 40))
        self.controls_title.setStyleSheet(u"background-color: rgb(0, 103, 185);")
        self.controls_title.setFrameShape(QFrame.Shape.StyledPanel)
        self.controls_title.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.controls_title)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.controls_title)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Barlow"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_5.addWidget(self.controls_title)

        self.connect_cn0583 = QFrame(self.controls_frame)
        self.connect_cn0583.setObjectName(u"connect_cn0583")
        self.connect_cn0583.setMaximumSize(QSize(16777215, 100))
        self.connect_cn0583.setStyleSheet(u"background-color: rgb(237, 237, 237);")
        self.connect_cn0583.setFrameShape(QFrame.Shape.StyledPanel)
        self.connect_cn0583.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.connect_cn0583)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_8 = QFrame(self.connect_cn0583)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 90))
        self.frame_8.setStyleSheet(u"background-color: rgb(237, 237, 237);\n"
"background-color: rgb(217, 217, 217);")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setFamilies([u"Barlow"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.label_5.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.connect = QPushButton(self.frame_8)
        self.connect.setObjectName(u"connect")
        self.connect.setMinimumSize(QSize(0, 50))
        self.connect.setMaximumSize(QSize(70, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Barlow"])
        font3.setBold(False)
        self.connect.setFont(font3)
        self.connect.setStyleSheet(u"border-color: rgb(194, 194, 194);\n"
"background-color: rgb(255, 255, 255);")
        self.connect.setFlat(False)

        self.horizontalLayout_8.addWidget(self.connect)


        self.verticalLayout_6.addWidget(self.frame_8)


        self.verticalLayout_5.addWidget(self.connect_cn0583)

        self.stream_buttons = QFrame(self.controls_frame)
        self.stream_buttons.setObjectName(u"stream_buttons")
        self.stream_buttons.setMaximumSize(QSize(16777215, 200))
        self.stream_buttons.setStyleSheet(u"background-color: rgb(237, 237, 237);")
        self.stream_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.stream_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.stream_buttons)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_10 = QFrame(self.stream_buttons)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 50))
        self.frame_10.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.start_button = QPushButton(self.frame_10)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(0, 0))
        self.start_button.setMaximumSize(QSize(250, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Barlow"])
        font4.setPointSize(14)
        font4.setBold(False)
        self.start_button.setFont(font4)
        self.start_button.setStyleSheet(u"border-color: rgb(194, 194, 194);\n"
"background-color: rgb(255, 255, 255);")
        self.start_button.setFlat(False)

        self.horizontalLayout_7.addWidget(self.start_button)


        self.verticalLayout_7.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.stream_buttons)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 50))
        self.frame_11.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.stop_button = QPushButton(self.frame_11)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMinimumSize(QSize(0, 0))
        self.stop_button.setMaximumSize(QSize(250, 16777215))
        self.stop_button.setFont(font4)
        self.stop_button.setStyleSheet(u"border-color: rgb(194, 194, 194);\n"
"background-color: rgb(255, 255, 255);")
        self.stop_button.setFlat(False)

        self.horizontalLayout_11.addWidget(self.stop_button)


        self.verticalLayout_7.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.stream_buttons)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 50))
        self.frame_12.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.clear_button = QPushButton(self.frame_12)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setMinimumSize(QSize(0, 0))
        self.clear_button.setMaximumSize(QSize(250, 16777215))
        self.clear_button.setFont(font4)
        self.clear_button.setStyleSheet(u"border-color: rgb(194, 194, 194);\n"
"background-color: rgb(255, 255, 255);")
        self.clear_button.setFlat(False)

        self.horizontalLayout_12.addWidget(self.clear_button)


        self.verticalLayout_7.addWidget(self.frame_12)


        self.verticalLayout_5.addWidget(self.stream_buttons)

        self.sapce = QFrame(self.controls_frame)
        self.sapce.setObjectName(u"sapce")
        self.sapce.setMaximumSize(QSize(16777215, 40))
        self.sapce.setStyleSheet(u"background-color: rgb(0, 103, 185);")
        self.sapce.setFrameShape(QFrame.Shape.StyledPanel)
        self.sapce.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.sapce)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_4 = QLabel(self.sapce)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.label_4)


        self.verticalLayout_5.addWidget(self.sapce)

        self.temperature = QFrame(self.controls_frame)
        self.temperature.setObjectName(u"temperature")
        self.temperature.setMaximumSize(QSize(16777215, 70))
        self.temperature.setStyleSheet(u"background-color: rgb(237, 237, 237);")
        self.temperature.setFrameShape(QFrame.Shape.StyledPanel)
        self.temperature.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.temperature)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_13 = QFrame(self.temperature)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.temp = QVBoxLayout()
        self.temp.setSpacing(2)
        self.temp.setObjectName(u"temp")

        self.horizontalLayout_9.addLayout(self.temp)


        self.horizontalLayout_16.addWidget(self.frame_13)


        self.verticalLayout_5.addWidget(self.temperature)

        self.frame_9 = QFrame(self.controls_frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.frame_9)


        self.horizontalLayout_3.addWidget(self.controls_frame)

        self.data_frame = QFrame(self.body)
        self.data_frame.setObjectName(u"data_frame")
        self.data_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.data_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.data_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.data_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 103, 185);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.label_2)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.data_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 400))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.bluegraph = QVBoxLayout()
        self.bluegraph.setObjectName(u"bluegraph")

        self.verticalLayout_9.addLayout(self.bluegraph)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.data_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 40))
        self.frame_5.setStyleSheet(u"background-color: rgb(0, 103, 185);")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.data_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 400))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.irgraph = QVBoxLayout()
        self.irgraph.setObjectName(u"irgraph")

        self.verticalLayout_10.addLayout(self.irgraph)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.data_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 80))
        self.frame_7.setStyleSheet(u"background-color: rgb(0, 103, 185);")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_14 = QFrame(self.frame_7)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(150, 16777215))
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_6 = QLabel(self.frame_14)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(250, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Barlow"])
        font5.setPointSize(15)
        font5.setBold(True)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.label_6)


        self.horizontalLayout_13.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_7)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.alarm_box = QVBoxLayout()
        self.alarm_box.setObjectName(u"alarm_box")

        self.horizontalLayout_15.addLayout(self.alarm_box)


        self.horizontalLayout_13.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_7)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(400, 16777215))
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_13.addWidget(self.frame_16)


        self.verticalLayout_4.addWidget(self.frame_7)


        self.horizontalLayout_3.addWidget(self.data_frame)


        self.verticalLayout_2.addWidget(self.body)


        self.verticalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.main)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.connect.setDefault(False)
        self.start_button.setDefault(False)
        self.stop_button.setDefault(False)
        self.clear_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.GUI_Name.setText(QCoreApplication.translate("MainWindow", u"CN0583 SMOKE DETECTION SYSTEM", None))
        self.for_ADI_logo.setText("")
        self.controls_frame.setStyleSheet(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CN0583 CONTROLS", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CN0583\n"
"Connection", None))
        self.connect.setText(QCoreApplication.translate("MainWindow", u"CONNECT", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"START STREAM", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CURRENT TEMPERATURE", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"BLUE LIGHT INTENSITY", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"IR LIGHT INTENSITY", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ALARM \n"
"STATUS", None))
    # retranslateUi

