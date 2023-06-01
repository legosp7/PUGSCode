import game
import pugs
import team
import user
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QComboBox, QLineEdit, QPushButton, QTextEdit
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UI Window")
        self.setGeometry(100, 100, 600, 400)

        # Create a central widget and set it as the main window's central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a grid layout for the central widget
        grid_layout = QGridLayout(central_widget)

        # Create two columns and six rows of cells
        for column in range(2):
            for row in range(6):
                # Create a dropdown box
                combo_box = QComboBox(self)
                grid_layout.addWidget(combo_box, row, column * 9)

                # Create eight empty boxes for text input for the last five rows
                if row >= 1:
                    for i in range(8):
                        line_edit = QLineEdit(self)
                        grid_layout.addWidget(line_edit, row, column * 9 + i + 1)

        # Create a submit button
        submit_button = QPushButton("Submit", self)
        grid_layout.addWidget(submit_button, 6, 0, 1, 2)

        # Create a menu bar
        menu_bar = self.menuBar()

        # Create a menu for switching windows
        switch_menu = menu_bar.addMenu("Switch Window")

        # Create an action to switch to a different window
        switch_action = QAction("Switch to Window", self)
        switch_action.triggered.connect(self.switch_to_window)
        switch_menu.addAction(switch_action)

    def switch_to_window(self):
        # Create a new window for switching
        switch_window = SwitchWindow()
        switch_window.show()

class SwitchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Switch Window")
        self.setGeometry(100, 100, 400, 300)

        # Create a text box
        text_box = QTextEdit(self)
        text_box.setGeometry(50, 50, 300, 200)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
