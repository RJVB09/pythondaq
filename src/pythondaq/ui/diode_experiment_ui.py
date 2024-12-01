# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'experiment.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
import pythondaq.ui.diode_experiment_ui_resources 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(953, 547)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.range_buttons = QHBoxLayout()
        self.range_buttons.setObjectName(u"range_buttons")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.start_label = QLabel(self.centralwidget)
        self.start_label.setObjectName(u"start_label")
        self.start_label.setStyleSheet(u"font: bold 15px;\n"
"font-family: Comic Sans MS;")

        self.verticalLayout_2.addWidget(self.start_label)

        self.startSpinBox = QSpinBox(self.centralwidget)
        self.startSpinBox.setObjectName(u"startSpinBox")
        self.startSpinBox.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 207, 226, 255), stop:1 rgba(167, 124, 255, 255));\n"
"font-family: Comic Sans MS;\n"
"font: bold 12px;")
        self.startSpinBox.setMaximum(1023)

        self.verticalLayout_2.addWidget(self.startSpinBox)


        self.range_buttons.addLayout(self.verticalLayout_2)

        self.startLayout = QVBoxLayout()
        self.startLayout.setObjectName(u"startLayout")
        self.stop_label = QLabel(self.centralwidget)
        self.stop_label.setObjectName(u"stop_label")
        self.stop_label.setStyleSheet(u"font: bold 15px;\n"
"font-family: Comic Sans MS;")

        self.startLayout.addWidget(self.stop_label)

        self.stopSpinBox = QSpinBox(self.centralwidget)
        self.stopSpinBox.setObjectName(u"stopSpinBox")
        self.stopSpinBox.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 207, 226, 255), stop:1 rgba(167, 124, 255, 255));\n"
"font-family: Comic Sans MS;\n"
"font: bold 12px;")
        self.stopSpinBox.setMaximum(1023)
        self.stopSpinBox.setValue(1023)

        self.startLayout.addWidget(self.stopSpinBox)


        self.range_buttons.addLayout(self.startLayout)


        self.verticalLayout.addLayout(self.range_buttons)

        self.iterationsLayout = QVBoxLayout()
        self.iterationsLayout.setObjectName(u"iterationsLayout")
        self.iterations_label = QLabel(self.centralwidget)
        self.iterations_label.setObjectName(u"iterations_label")
        self.iterations_label.setStyleSheet(u"font: bold 15px;\n"
"font-family: Comic Sans MS;")

        self.iterationsLayout.addWidget(self.iterations_label)

        self.iterationsSpinBox = QSpinBox(self.centralwidget)
        self.iterationsSpinBox.setObjectName(u"iterationsSpinBox")
        self.iterationsSpinBox.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 207, 226, 255), stop:1 rgba(167, 124, 255, 255));\n"
"font-family: Comic Sans MS;\n"
"font: bold 12px;")
        self.iterationsSpinBox.setMaximum(50)
        self.iterationsSpinBox.setValue(2)

        self.iterationsLayout.addWidget(self.iterationsSpinBox)


        self.verticalLayout.addLayout(self.iterationsLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.deviceLayout = QVBoxLayout()
        self.deviceLayout.setObjectName(u"deviceLayout")
        self.device_label = QLabel(self.centralwidget)
        self.device_label.setObjectName(u"device_label")
        self.device_label.setStyleSheet(u"font: bold 15px;\n"
"font-family: Comic Sans MS;")

        self.deviceLayout.addWidget(self.device_label)

        self.updateDevicesButton = QPushButton(self.centralwidget)
        self.updateDevicesButton.setObjectName(u"updateDevicesButton")
        self.updateDevicesButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(226, 0, 174, 255), stop:1 rgba(255, 219, 124, 255));\n"
"font-family: Comic Sans MS")

        self.deviceLayout.addWidget(self.updateDevicesButton)

        self.deviceComboBox = QComboBox(self.centralwidget)
        self.deviceComboBox.setObjectName(u"deviceComboBox")
        self.deviceComboBox.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 207, 226, 255), stop:1 rgba(167, 124, 255, 255));\n"
"font-family: Comic Sans MS")

        self.deviceLayout.addWidget(self.deviceComboBox)


        self.verticalLayout.addLayout(self.deviceLayout)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setStyleSheet(u"background-image: url(:/images/scrumpy.jpg);\n"
"background-color: #cccccc; /* Used if the image is unavailable */\n"
"height: 100px; /* You must set a specified height */\n"
"background-position: center; /* Center the image */\n"
"background-repeat: no-repeat; /* Do not repeat the image */\n"
"background-size: cover; /* Resize the background image to cover the entire container */")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(57, 173, 0, 255), stop:1 rgba(212, 255, 124, 255));\n"
"font-family: Comic Sans MS")

        self.verticalLayout.addWidget(self.startButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.saveLineEdit = QLineEdit(self.centralwidget)
        self.saveLineEdit.setObjectName(u"saveLineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.saveLineEdit.sizePolicy().hasHeightForWidth())
        self.saveLineEdit.setSizePolicy(sizePolicy1)
        self.saveLineEdit.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 207, 226, 255), stop:1 rgba(167, 124, 255, 255));\n"
"font-family: Comic Sans MS;\n"
"font: bold 11px;")

        self.verticalLayout.addWidget(self.saveLineEdit)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(226, 0, 174, 255), stop:1 rgba(255, 219, 124, 255));\n"
"font-family: Comic Sans MS")

        self.verticalLayout.addWidget(self.saveButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.plot_widget = PlotWidget(self.centralwidget)
        self.plot_widget.setObjectName(u"plot_widget")
        self.plot_widget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(65, 111, 120, 255));")

        self.verticalLayout_4.addWidget(self.plot_widget)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"font: 700 11pt \"Comic Sans MS\";")
        self.progressBar.setValue(24)

        self.verticalLayout_4.addWidget(self.progressBar)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 953, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pythondaq - Diode experiment", None))
        self.start_label.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_label.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.iterations_label.setText(QCoreApplication.translate("MainWindow", u"Iterations", None))
        self.device_label.setText(QCoreApplication.translate("MainWindow", u"Device", None))
        self.updateDevicesButton.setText(QCoreApplication.translate("MainWindow", u"Update devices list...", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start measurement", None))
        self.saveLineEdit.setText("")
        self.saveLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CSV file name", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

