"""
This script aims at develop GUI for data read from existing files and after doing some
data cleaning works, save the results and exit GUI

developed by: Shuai Zhu @GE
10-10-2010
"""
"""
This script aims at find ways to implement the previous code in python GUI with the help of pyQT5
"""
import os
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, QMessageBox, QAction, QTableWidget,
                             QTableWidgetItem, QInputDialog, QLineEdit, QFileDialog)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout)


class App_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'GE Digital'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Buttons
        read_data = QPushButton('LOAD DATA', self)
        read_data.setToolTip('Loading data from file')
        read_data.move(20, 70)
        read_data.clicked.connect(self.on_click_read)

        tran_data = QPushButton('Transform DATA', self)
        tran_data.setToolTip('Transforming data format')
        tran_data.move(320, 70)
        tran_data.clicked.connect(self.on_click_clean)

        save_data = QPushButton('SAVE DATA', self)
        save_data.setToolTip('Save data into file')
        save_data.move(620, 70)
        save_data.clicked.connect(self.on_click_save)
        self.show()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Excel Files (*.xlsx);;CSV Files (*.csv);;Dat Files (*.dat)", options=options)
        if fileName:
            print(fileName)

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                  "All Files (*);;Excel Files (*.xlsx);;CSV Files (*.csv);;Dat Files (*.dat)", options=options)
        if files:
            print(files)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Excel Files (*.xlsx);;CSV Files (*.csv);;Dat Files (*.dat)", options=options)
        if fileName:
            print(fileName)


    @pyqtSlot()
    def on_click_read(self):
        print('Read data!')
    def on_click_clean(self):
        print('data clean!')
    def on_click_save(self):
        print('Save data!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App_widget()
    sys.exit(app.exec_())
