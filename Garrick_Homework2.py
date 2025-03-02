import sys, os, shutil
import numpy as np
import matplotlib.pyplot as plt

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QToolBar, QStatusBar
from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QColor, QPalette, QPixmap, QBrush
from PIL import Image
from matplotlib import pyplot as plt

from matplotlib.patches import Circle
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.animation import FuncAnimation
import circlesandcolor

#︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶#

#Basic Window Settings
class MainWindow(QMainWindow): 
    def __init__(self):
        super().__init__()        
        self.setWindowTitle("୨୧ Tech Foundations II - Homework 2 ୨୧")
        self.setFixedSize(1000,600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QHBoxLayout(central_widget)

        #︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶#

        #Left side of the window
        self.image_label = QLabel(central_widget)
        self.image_label.setGeometry(0, 0, 500, 600)
        pixmap = QtGui.QPixmap("/Users/jadagarrick/Downloads/PythonCode/PE.jpg")
        scaled_pixmap = pixmap.scaled(500, 600, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.image_label.setPixmap(scaled_pixmap)
        layout.addWidget(self.image_label)

        #︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶#

        #Right side of the window
        self.figure = plt.Figure(figsize=(5, 6), dpi=100)  # Set figure size to match the window size
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setFixedSize(500, 600)  # Set canvas size to 500x600
        layout.addWidget(self.canvas)

        #︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶#

        #Basics of Toolbar
        toolbar = QToolBar("୨୧ Main Toolbar ୨୧")
        self.addToolBar(toolbar)
        toolbar.addAction("Quit :(", self.close)

        #︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶#

        #Generate Geometry Button
        button_action = QAction("୨୧ Generate Geometry ୨୧", self) 
        button_action.setToolTip("This is the button to generate geometry ⁺ . ✦")
        button_action.triggered.connect(self.start_animation)
        toolbar.addAction(button_action)
        
        self.animation = None  #placeholder!

        #︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶#

        #Stop Generating Geometry Button
        button_action2 = QAction("୨୧ Stop Generating Geometry ୨୧", self) 
        button_action2.setToolTip("This is the button to stop generating geometry ⁺ . ✦")
        button_action2.triggered.connect(self.stop_animation)
        toolbar.addAction(button_action2)

#︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶#

    #Definition of start_animation
    def start_animation(self):
        print("Starting to Generate Geometry ⁺ . ✦")
        self.figure.clear() 

        ax = self.figure.add_subplot(111)
        ax.set_xlim(0, 100)  # Maybe adjust limits to fit resized image??
        ax.set_ylim(0, 100)

        self.animation = circlesandcolor.main(ax, self.canvas) 
        self.canvas.draw()

    #Definition of stop_animation
    def stop_animation(self):
        print("Stopping Generation of Geometry ⁺ . ✦")
        if self.animation:
            self.animation.event_source.stop()


#︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶︶⊹︶︶୨୧︶︶⊹︶#

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
