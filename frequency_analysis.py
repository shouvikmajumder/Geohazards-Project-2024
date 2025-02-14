# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frequency_analysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.




from PyQt5 import QtCore, QtGui, QtWidgets

import datetime
import foreseeTools as das
import numpy as np

from scipy import signal
import matplotlib.pyplot as plt

from PyQt5 import QtCore, QtGui, QtWidgets

from LoadingWindow  import Ui_LoadingWindow
import h5py
from tdms_reader import TdmsReader

import obspy
class Ui_MainWindow_FreqAnalysis(object):
    def __init__(self,data2):
        self.data2 = data2
        self.chlist_input = '0-2137'


    def plot_graph(self):
        plot_type = self.cb_PlotType.currentText()

        # print(plot_type) This works

        if plot_type == "x-t":
            self.plot_xt()
        elif plot_type == "x-f":
            self.plot_xf()
        elif plot_type == "f-t":
            self.plot_ft()

        # THIS ONE FULLY WORKS
    def plot_xt(self):
        # Assuming the correct function or method exists for converting stream to array
        ch1 = int(self.chlist_input.split('-')[0])
        ch2 = int(self.chlist_input.split('-')[1])
        window_length = 120

        # Replace das.stream2array with the correct function if it exists
        section = das.stream2array(self.data2)[ch1: ch2] # Assuming self.data2 is an ObsPy Stream object

        cmax = np.percentile(section, 80)
        self.MplWidget.canvas.axes.imshow(section, vmin=-cmax, vmax=cmax, aspect='auto', extent=[0, window_length, ch2, ch1], cmap='seismic')
        self.MplWidget.canvas.axes.set(ylabel='Channels', xlabel='Time(s)')
        self.MplWidget.canvas.draw()

        #THIS ONE FULLY WORKS
    def plot_xf(self):
        ch1 = int(self.chlist_input.split('-')[0])
        ch2 = int(self.chlist_input.split('-')[1])
        window_length = 120
        
        # print( f" PRINT STATEMENT HERE !!!!!!!! {self.data2}")

        section = das.stream2array(self.data2)[ch1: ch2]
        print(section)

        
        # Calculate Welch's power spectral density estimate
        f, Pxx_den = signal.welch(section, fs=self.data2[0].stats.sampling_rate)
        
        cmin = np.percentile(np.log(Pxx_den), 5)
        cmax = np.percentile(np.log(Pxx_den), 95)

        # Clear the axes before plotting
        self.MplWidget.canvas.axes.clear()

        # Plotting
        self.MplWidget.canvas.axes.pcolormesh(f, np.arange(ch1, ch2), np.log(Pxx_den), vmin=cmin, vmax=cmax, shading='gouraud')
        self.MplWidget.canvas.axes.set(ylabel='Channels', xlabel='Frequency (Hz)')
        
        # Draw the updated plot
        self.MplWidget.canvas.draw()



    def plot_ft(self):
        chlist_input = '356-364'
        ch1 = int(chlist_input.split('-')[0])
        ch2 = int(chlist_input.split('-')[1])

        D_sub = obspy.Stream()
        chlist = np.arange(ch1, ch2 + 1)  # Include the upper bound channel
        for channel in chlist:
                D_sub += self.data2.select(channel=str('%04d' % channel))
        D_sub = D_sub.stack(group_by='all')

        # Clear any previous plots
        self.MplWidget.canvas.axes.clear()
        
        # Plot the spectrogram
        D_sub.spectrogram(log=True, axes=self.MplWidget.canvas.axes)
        
        # Set labels
        self.MplWidget.canvas.axes.set_ylabel('Frequency (Hz)')
        self.MplWidget.canvas.axes.set_xlabel('Time (s)')
        
        # Refresh the canvas to show the plot
        self.MplWidget.canvas.draw()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 624)
        MainWindow.setStyleSheet("QMainWindow{\n"
"\n"
"background: #FFFFFF;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(81, 10, 849, 552))
        self.widget.setObjectName("widget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_5 = QtWidgets.QFrame(self.widget)
        self.frame_5.setMinimumSize(QtCore.QSize(160, 542))
        self.frame_5.setMaximumSize(QtCore.QSize(160, 542))
        self.frame_5.setStyleSheet("QFrame{\n"
"background: #0276FF;\n"
"border-radius: 10px\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setMinimumSize(QtCore.QSize(131, 261))
        self.frame_8.setMaximumSize(QtCore.QSize(131, 261))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_8)
        self.frame_4.setMinimumSize(QtCore.QSize(131, 45))
        self.frame_4.setMaximumSize(QtCore.QSize(131, 45))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setMinimumSize(QtCore.QSize(69, 19))
        self.label.setMaximumSize(QtCore.QSize(69, 19))
        self.label.setStyleSheet("QLabel{\n"
"color: rgb(16, 19, 7);\n"
"font-weight: bold;\n"
"font-size: 16px;\n"
"}")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_time = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_time.setMinimumSize(QtCore.QSize(30, 21))
        self.lineEdit_time.setMaximumSize(QtCore.QSize(30, 21))
        self.lineEdit_time.setTabletTracking(False)
        self.lineEdit_time.setStyleSheet("QLineEdit{\n"
"background: rgb(255,255,255);\n"
"color: rgb(11, 7, 4);\n"
"}\n"
"")
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.gridLayout_2.addWidget(self.lineEdit_time, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_4, 1, 0, 1, 1)
        self.pushButton_plot = QtWidgets.QPushButton(self.frame_8, clicked = lambda: self.plot_graph())
        self.pushButton_plot.setMinimumSize(QtCore.QSize(107, 32))
        self.pushButton_plot.setMaximumSize(QtCore.QSize(107, 32))
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.gridLayout_4.addWidget(self.pushButton_plot, 3, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame_8)
        self.frame_2.setMinimumSize(QtCore.QSize(121, 50))
        self.frame_2.setMaximumSize(QtCore.QSize(121, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMinimumSize(QtCore.QSize(36, 16))
        self.label_4.setMaximumSize(QtCore.QSize(36, 16))
        self.label_4.setStyleSheet("QLabel{\n"
"color: rgb(16, 19, 7);\n"
"font-weight: bold;\n"
"font-size: 16px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.cb_PlotType = QtWidgets.QComboBox(self.frame_2)
        self.cb_PlotType.setMinimumSize(QtCore.QSize(59, 32))
        self.cb_PlotType.setMaximumSize(QtCore.QSize(59, 32))
        self.cb_PlotType.setObjectName("cb_PlotType")
        self.cb_PlotType.addItem("")
        self.cb_PlotType.addItem("")
        self.cb_PlotType.addItem("")
        self.gridLayout.addWidget(self.cb_PlotType, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_8)
        self.frame_6.setMinimumSize(QtCore.QSize(145, 45))
        self.frame_6.setMaximumSize(QtCore.QSize(145, 45))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setMinimumSize(QtCore.QSize(62, 19))
        self.label_2.setMaximumSize(QtCore.QSize(62, 19))
        self.label_2.setStyleSheet("QLabel{\n"
"color: rgb(16, 19, 7);\n"
"font-weight: bold;\n"
"font-size: 16px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_ch = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_ch.setMinimumSize(QtCore.QSize(51, 21))
        self.lineEdit_ch.setMaximumSize(QtCore.QSize(51, 21))
        self.lineEdit_ch.setStyleSheet("QLineEdit{\n"
"background: rgb(255,255,255);\n"
"color: rgb(11, 7, 4);\n"
"}\n"
"")
        self.lineEdit_ch.setObjectName("lineEdit_ch")
        self.gridLayout_3.addWidget(self.lineEdit_ch, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_6, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_8, 0, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setMinimumSize(QtCore.QSize(152, 69))
        self.frame_7.setMaximumSize(QtCore.QSize(152, 69))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit.setGeometry(QtCore.QRect(12, 36, 125, 21))
        self.lineEdit.setMinimumSize(QtCore.QSize(125, 21))
        self.lineEdit.setMaximumSize(QtCore.QSize(125, 21))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: transparent;\n"
"}\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_5.addWidget(self.frame_7, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setMinimumSize(QtCore.QSize(128, 16))
        self.label_3.setMaximumSize(QtCore.QSize(128, 16))
        self.label_3.setStyleSheet("QLabel{\n"
"color: rgb(16, 19, 7);\n"
"font-weight: bold;\n"
"font-size: 16px;\n"
"}")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_5, 0, 0, 3, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setMinimumSize(QtCore.QSize(546, 45))
        self.textBrowser.setMaximumSize(QtCore.QSize(546, 45))
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"border:none;\n"
"background: #FFFFFF;\n"
"color: #000000\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_6.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.MplWidget = MplWidget(self.widget)
        self.MplWidget.setMinimumSize(QtCore.QSize(671, 411))
        self.MplWidget.setMaximumSize(QtCore.QSize(671, 411))
        self.MplWidget.setObjectName("MplWidget")
        self.gridLayout_6.addWidget(self.MplWidget, 1, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setMinimumSize(QtCore.QSize(220, 68))
        self.frame_3.setMaximumSize(QtCore.QSize(220, 68))
        self.frame_3.setStyleSheet("QFrame{\n"
"background: #0276FF;\n"
"border-radius: 10px\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setGeometry(QtCore.QRect(30, 13, 151, 41))
        self.frame.setMinimumSize(QtCore.QSize(151, 41))
        self.frame.setMaximumSize(QtCore.QSize(151, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_back = QtWidgets.QPushButton(self.frame)
        self.pushButton_back.setGeometry(QtCore.QRect(12, 8, 60, 32))
        self.pushButton_back.setMinimumSize(QtCore.QSize(60, 32))
        self.pushButton_back.setMaximumSize(QtCore.QSize(60, 32))
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_next = QtWidgets.QPushButton(self.frame)
        self.pushButton_next.setGeometry(QtCore.QRect(86, 8, 58, 32))
        self.pushButton_next.setMinimumSize(QtCore.QSize(58, 32))
        self.pushButton_next.setMaximumSize(QtCore.QSize(58, 32))
        self.pushButton_next.setObjectName("pushButton_next")
        self.gridLayout_6.addWidget(self.frame_3, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Start min"))
        self.lineEdit_time.setText(_translate("MainWindow", "0"))
        self.pushButton_plot.setText(_translate("MainWindow", "Plot"))
        self.label_4.setText(_translate("MainWindow", "Types"))
        self.cb_PlotType.setItemText(0, _translate("MainWindow", "x-t"))
        self.cb_PlotType.setItemText(1, _translate("MainWindow", "x-f"))
        self.cb_PlotType.setItemText(2, _translate("MainWindow", "f-t"))
        self.label_2.setText(_translate("MainWindow", "Channel"))
        self.lineEdit_ch.setText(_translate("MainWindow", "0-2120"))
        self.lineEdit.setText(_translate("MainWindow", "60"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Frequency analysis</span></p></body></html>"))
        self.pushButton_back.setText(_translate("MainWindow", "Back"))
        self.pushButton_next.setText(_translate("MainWindow", "Next"))
from mplwidget import MplWidget
