# Pictures sampled are from houses dataset: https://github.com/emanhamed/Houses-dataset

###########################################################################
# Covert .ui file to .py
#    pyside2-uic "C:\Users\LR Admin\QtProjects\display_image_test\mainwindow.ui" -o "C:\Users\LR Admin\PycharmProjects\qt_stuff\gui_image_test.py"
###########################################################################

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Slot, QTimer
from PySide2.QtGui import QPixmap
import sys
from gui_image_test import Ui_MainWindow

basePath = "C:/Users/LR Admin/Downloads/Houses-dataset-master/Houses Dataset/"
imageDict = {0: "bathroom", 1: "bedroom", 2: "frontal", 3: "kitchen"}
counter = 0

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.labelList = [self.label, self.label_2, self.label_3, self.label_4]
        self.connect()
        # radioButton is "Cycle" --- radioButton_2 is "Use Button"

    def connect(self):
        self.pushButton.clicked.connect(self.load_image)
        self.radioButton.toggled.connect(self.cycle_images)
        self.fontComboBox.currentFontChanged.connect(self.changeFont)

    @Slot()
    def load_image(self):
        a = self.sender() == self.pushButton and self.radioButton_2.isChecked()
        b = self.sender() != self.pushButton and self.radioButton.isChecked()
        if a or b:
            global counter
            counter += 1
            self.label_5.setText("House #" + str(counter))
            for room, label in zip(imageDict, self.labelList):
                imagePath = basePath + str(counter) + "_" + imageDict[room] + ".jpg"
                label.setPixmap(QPixmap(imagePath).scaled(label.width(), label.height()))

    @Slot()
    def cycle_images(self):
        if self.radioButton.isChecked():
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.load_image)
            self.timer.start(1500)
        else:
            self.timer.stop()

    @Slot()
    def changeFont(self):
        qfont = self.fontComboBox.currentFont()
        qfont.setPointSize(8)
        self.pushButton.setFont(qfont)
        self.pushButton.setStyleSheet('QPushButton {color: rgb(255, 255, 127);'
                                      'background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,'
                                      '     stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 0, 255));'
                                      'font: qfont;'
                                      'font-size: 11pt}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
