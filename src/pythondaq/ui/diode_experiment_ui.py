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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(927, 509)
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

        self.verticalLayout_2.addWidget(self.start_label)

        self.startSpinBox = QSpinBox(self.centralwidget)
        self.startSpinBox.setObjectName(u"startSpinBox")
        self.startSpinBox.setMaximum(1023)

        self.verticalLayout_2.addWidget(self.startSpinBox)


        self.range_buttons.addLayout(self.verticalLayout_2)

        self.startLayout = QVBoxLayout()
        self.startLayout.setObjectName(u"startLayout")
        self.stop_label = QLabel(self.centralwidget)
        self.stop_label.setObjectName(u"stop_label")

        self.startLayout.addWidget(self.stop_label)

        self.stopSpinBox = QSpinBox(self.centralwidget)
        self.stopSpinBox.setObjectName(u"stopSpinBox")
        self.stopSpinBox.setMaximum(1023)
        self.stopSpinBox.setValue(1023)

        self.startLayout.addWidget(self.stopSpinBox)


        self.range_buttons.addLayout(self.startLayout)


        self.verticalLayout.addLayout(self.range_buttons)

        self.iterationsLayout = QVBoxLayout()
        self.iterationsLayout.setObjectName(u"iterationsLayout")
        self.iterations_label = QLabel(self.centralwidget)
        self.iterations_label.setObjectName(u"iterations_label")

        self.iterationsLayout.addWidget(self.iterations_label)

        self.iterationsSpinBox = QSpinBox(self.centralwidget)
        self.iterationsSpinBox.setObjectName(u"iterationsSpinBox")
        self.iterationsSpinBox.setMaximum(50)
        self.iterationsSpinBox.setValue(2)

        self.iterationsLayout.addWidget(self.iterationsSpinBox)


        self.verticalLayout.addLayout(self.iterationsLayout)

        self.deviceLayout = QVBoxLayout()
        self.deviceLayout.setObjectName(u"deviceLayout")
        self.device_label = QLabel(self.centralwidget)
        self.device_label.setObjectName(u"device_label")

        self.deviceLayout.addWidget(self.device_label)

        self.deviceComboBox = QComboBox(self.centralwidget)
        self.deviceComboBox.setObjectName(u"deviceComboBox")

        self.deviceLayout.addWidget(self.deviceComboBox)


        self.verticalLayout.addLayout(self.deviceLayout)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")

        self.verticalLayout.addWidget(self.start_button)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout.addWidget(self.saveButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.plot_widget = PlotWidget(self.centralwidget)
        self.plot_widget.setObjectName(u"plot_widget")

        self.verticalLayout_4.addWidget(self.plot_widget)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_4.addWidget(self.progressBar)


        self.horizontalLayout.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 927, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start_label.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stop_label.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.iterations_label.setText(QCoreApplication.translate("MainWindow", u"Iterations", None))
        self.device_label.setText(QCoreApplication.translate("MainWindow", u"Device", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start measurement", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

