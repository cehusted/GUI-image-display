# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\LR Admin\QtProjects\display_image_test\mainwindow.ui',
# licensing of 'C:\Users\LR Admin\QtProjects\display_image_test\mainwindow.ui' applies.
#
# Created: Wed May 29 15:39:10 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 659)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 550, 261, 51))
        self.pushButton.setStyleSheet("font: 81 11pt \"Open Sans ExtraBold\";\n"
"color: rgb(255, 255, 127);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 0, 255));")
        self.pushButton.setObjectName("pushButton")
        self.fontComboBox = QtWidgets.QFontComboBox(self.centralWidget)
        self.fontComboBox.setGeometry(QtCore.QRect(360, 530, 261, 22))
        self.fontComboBox.setStyleSheet("border: transparent;")
        font = QtGui.QFont()
        font.setFamily("Open Sans ExtraBold")
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.fontComboBox.setCurrentFont(font)
        self.fontComboBox.setObjectName("fontComboBox")
        self.radioButton = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton.setGeometry(QtCore.QRect(140, 540, 95, 20))
        self.radioButton.setStyleSheet("")
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralWidget)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 570, 95, 20))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 471, 251))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(710, 530, 171, 51))
        self.label_5.setStyleSheet("font: 28pt \"Pristina\";")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 270, 471, 251))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(490, 10, 471, 251))
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(490, 270, 471, 251))
        self.label_4.setStyleSheet("")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1008, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "Load Next Image", None, -1))
        self.radioButton.setText(QtWidgets.QApplication.translate("MainWindow", "Cycle", None, -1))
        self.radioButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "Use Button", None, -1))

