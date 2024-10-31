from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Define a class MplWidget that inherits from QWidget
class MplWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)  # Call the parent class (QWidget) constructor

        # Create a FigureCanvas object which will serve as the Matplotlib canvas
        self.canvas = FigureCanvas(Figure())

        # Create a vertical layout to hold the canvas
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)  # Add the canvas to the layout

        # Add a subplot to the canvas
        self.canvas.axes = self.canvas.figure.add_subplot(111)

        # Set the layout of the widget to the vertical layout
        self.setLayout(vertical_layout)
