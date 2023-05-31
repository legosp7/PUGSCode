import pickle
import sys
import UI
from user import *
from team import *

from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PyQt6.QtCore import Qt

with open("users.rkb","rb") as opf:
    userdict = pickle.load(opf)
with open("teams.rkb","rb") as teams:
    teamdict = pickle.load(teams)
    
    
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        
        widget1 = QComboBox()
        widget1.addItems(teamdict)
        widget1.currentIndexChanged.connect( self.index_changed )

        # There is an alternate signal to send the text.
        widget1.currentTextChanged.connect( self.text_changed )

        self.setCentralWidget(widget1)


    def index_changed(self, i): # i is an int
        print(i)

    def text_changed(self, s): # s is a str
        print(s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()