import game
import pugs
import team
import user
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QComboBox, QLineEdit

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

        # Create two columns and five rows of cells
        for column in range(2):
            for row in range(5):
                # Create a dropdown box
                combo_box = QComboBox(self)
                grid_layout.addWidget(combo_box, row, column * 9)

                # Create eight empty boxes for text input
                for i in range(8):
                    line_edit = QLineEdit(self)
                    grid_layout.addWidget(line_edit, row, column * 9 + i + 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())