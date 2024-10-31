# Now import the necessary modules
# sys.path.append(os.path.join(os.path.dirname(__file__), 'DAS_GUI'))

from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from OpeningWindow import Ui_MainWindow  # Ensure this file is correctly set up


# from DAS_GUI import main



class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Main Menu")

        # Assuming `self.icon_name_widget` exists in your `Ui_MainWindow`
        self.icon_name_widget.setHidden(True)

        # Connecting the buttons (assuming these exist in your `Ui_MainWindow`)
        self.HomeButton.clicked.connect(self.switch_to_home)
        self.HomeButton_2.clicked.connect(self.switch_to_home)
        self.LoadDataButton.clicked.connect(self.switch_to_loaddata)
        self.LoadDataButton_2.clicked.connect(self.switch_to_loaddata)
        self.SearchButton.clicked.connect(self.switch_to_search)
        self.SearchButton_2.clicked.connect(self.switch_to_search)
        self.MoreInfoButton.clicked.connect(self.switch_to_moreinfo)
        self.MoreInfoButton_2.clicked.connect(self.switch_to_moreinfo)

    def switch_to_home(self):
        self.Header_Widget.setCurrentIndex(0)

    def switch_to_loaddata(self):
        self.Header_Widget.setCurrentIndex(3)

    def switch_to_search(self):
        self.Header_Widget.setCurrentIndex(1)

    def switch_to_moreinfo(self):
        self.Header_Widget.setCurrentIndex(2)
    
    

if __name__ == "__main__":
    app = QApplication([])
    window = MySideBar()
    window.show()
    app.exec()
