from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from plotWindow import Ui_plotWindow
from tdms_reader import TdmsReader
from foreseeTools import downsample
from startup import Ui_MainWindow2
import datetime
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from matplotlib import cm
import numpy as np
import scipy.io
from LoadingWindow import Ui_LoadingWindow
import h5py
from scipy import signal
import matplotlib.pyplot as plt
import obspy
import foreseeTools as das
# Define a class Mymain that inherits from QMainWindow
class Mymain(QtWidgets.QMainWindow):
    

    def __init__(self):
        super().__init__()  # Call the parent class (QMainWindow) constructor
        loadUi("LoadingWindow.ui", self)  # Load the UI file
        self.setWindowTitle("DAS Data Visualization")  # Set the window title

        # Connect buttons to their respective methods
        self.pushButton_2ndwindow.clicked.connect(self.open2ndwindow)


        self.pushButton_start.clicked.connect(self.start)
        # self.pushButtoncombo_2.connect(self.confirmsys)
        # self.pushButtoncombo_2.connect(self.confirmfiletype)
        # Initialize variables
        self.data = None  # Initialize self.data
        self.label = np.array
        self.plot_type = 'Color Plot'
        self.chlist_input = '0-2137'
        self.sys_name = self.comboBox.currentText() 
        self.file_format = self.comboBox_5.currentText()

        # self.datadir = '/Users/shouvikmajumder/Desktop/DAS_GUI/DasData/'
   

        # self.fs = None  # This line is commented out, fs is set in start method

    # Method to open the second window that has the User interface

    def open2ndwindow(self):
        if self.data is None:  # Check if data is loaded
            QtWidgets.QMessageBox.warning(self, "Warning", "No data loaded. Please load data first.")
            return
        # self.window = QtWidgets.QMainWindow()  # Create a new QMainWindow
        # self.ui2 = Ui_plotWindow(self.data)  # Initialize Ui_plotWindow with data
        # self.ui2.setupUi(self.window)  # Set up the UI
        # self.window.addToolBar(NavigationToolbar(self.ui2.MplWidget.canvas, self))  # Add a toolbar for navigation
        # self.window.show()  # Show the second window
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2(self.data) # send the data from the loading screen to startup.py
        self.ui.setupUi(self.window)
        self.window.show()

    # Method to start data processing
    def start2(self):
        datadir = '/Users/shouvikmajumder/Desktop/DAS_GUI/DasData/'   # Set the data directory
        # t1 = self.lineEdit_stime.text()  # Get start time from the UI
        # t2 = self.lineEdit_etime.text()  # Get end time from the UI
        # Parse start time
        stime = datetime.datetime(
            int(self.lineEdit_stime_1.text()), int(self.lineEdit_stime_2.text()),
            int(self.lineEdit_stime_3.text()), int(self.lineEdit_stime_4.text()),
            int(self.lineEdit_stime_5.text()), int(self.lineEdit_stime_6.text()),
            int(self.lineEdit_stime_7.text()) * 1000
        )
        etime = datetime.datetime(
            int(self.lineEdit_etime_1.text()), int(self.lineEdit_etime_2.text()),
            int(self.lineEdit_etime_3.text()), int(self.lineEdit_etime_4.text()),
            int(self.lineEdit_etime_5.text()), int(self.lineEdit_etime_6.text()),
            int(self.lineEdit_etime_7.text()) * 1000
        )

        ch1 = int(self.chlist_input.split('-')[0])
        ch2 = int(self.chlist_input.split('-')[1])
        chlist = np.arange(ch1, ch2)
        fs = 250

        if self.sys_name=='PSU':
            calibration = True
            good_traces_index = das.foresee_calibration()
        else:
            calibration = False
            good_traces_index = chlist
        # define original fs
        timestamp = str(stime)
        timestamp = timestamp.replace('-', '').replace(' ', '_').replace(':', '')[0:-3]
        inputFile = datadir + 'PSUDAS_UTC_' + timestamp + "." + self.file_format #HERE IS THE PROBLEM!!!!!!
        tdms = TdmsReader(inputFile)  # Read the TDMS file
        if self.file_format == 'h5': 
            f = h5py.File(inputFile, 'r')
            dset = f['Acoustic']
            fs0 = dset.shape[0]//60
        elif self.file_format == 'tdms':
            tdms = TdmsReader(inputFile)
            fs0 = int(tdms.get_properties()['SamplingFrequency[Hz]'])

        nsample_1min = fs0*60
        n_file = int((etime - stime).total_seconds() / 60.0)

        data = np.empty([len(chlist), nsample_1min * n_file])
        for i in range(n_file):
            timestamp = str(stime + datetime.timedelta(minutes=i))
            timestamp = timestamp.replace('-', '').replace(' ', '_').replace(':', '')[0:-3]
            inputFile = datadir + 'PSUDAS_UTC_' + timestamp + "."+ self.file_format

            tdms = TdmsReader(inputFile)  # Read the TDMS file
            
            if self.file_format == 'h5': 
                f = h5py.File(inputFile, 'r')
                dset = f['Acoustic']
                data[:, nsample_1min * i:nsample_1min * (i + 1)] = dset[:, good_traces_index[chlist]].T
                
            elif self.file_format == 'tdms':
                tdms = TdmsReader(inputFile)
                props = tdms.get_properties()
                nCh = tdms.fileinfo['n_channels']
                if nCh == 2496:
                    data0 = tdms.get_data(64, nCh, 0, tdms.channel_length - 1)
                else:
                    data0 = tdms.get_data(0, nCh, 0, tdms.channel_length - 1)
                data[:, nsample_1min * i:nsample_1min * (i + 1)] = np.transpose(data0)[good_traces_index[chlist]]
                
        param = {'network':self.sys_name, 'station':'--','fs':int(fs0),'dt':1/fs0, 'start':stime,
        'dx':2,'gl':10, 'units':'nanostrain/s', 'chlist':chlist}
        D = das.array2stream(data, param)
        if fs0 != fs:
            D.decimate(fs0//fs) # downsample
        self.data = D 
    
    


    def start(self):
        datadir = '/Users/shouvikmajumder/Desktop/DAS_GUI/DasData/'  # Set the data directory
        # t1 = self.lineEdit_stime.text()  # Get start time from the UI
        # t2 = self.lineEdit_etime.text()  # Get end time from the UI
        
        # Parse start time
        stime = datetime.datetime(
            int(self.lineEdit_stime_1.text()), int(self.lineEdit_stime_2.text()),
            int(self.lineEdit_stime_3.text()), int(self.lineEdit_stime_4.text()),
            int(self.lineEdit_stime_5.text()), int(self.lineEdit_stime_6.text()),
            int(self.lineEdit_stime_7.text()) * 1000
        )
        etime = datetime.datetime(
            int(self.lineEdit_etime_1.text()), int(self.lineEdit_etime_2.text()),
            int(self.lineEdit_etime_3.text()), int(self.lineEdit_etime_4.text()),
            int(self.lineEdit_etime_5.text()), int(self.lineEdit_etime_6.text()),
            int(self.lineEdit_etime_7.text()) * 1000
        )

        
        nsample_1min = 15000  # Number of samples per minute

        fs = int(self.lineEdit_fs.text())  # Get sampling frequency from the UI
        location = np.loadtxt('DAS_location.txt')  # Load channel location info
        ch_info = location[:, 1].astype(int)  # Extract channel info as integers
        n_file = int((etime - stime).total_seconds() / 60.0)  # Calculate number of files
        data = np.empty([2120, nsample_1min * n_file])  # Initialize data array
        
        # Loop over each file based on the time range
        for i in range(n_file):
            # Generate the timestamp for the current file
            timestamp = str(stime + datetime.timedelta(minutes=i))
            timestamp = timestamp.replace('-', '').replace(' ', '_').replace(':', '')[0:-3]
            inputFile = datadir + 'PSUDAS_UTC_' + timestamp + '.tdms'   # Construct the file path
            tdms = TdmsReader(inputFile)  # Read the TDMS file
            props = tdms.get_properties()  # Get properties of the TDMS file
            nCh = tdms.fileinfo['n_channels']  # Get number of channels
            
            # Read data based on the number of channels
            if nCh == 2432:
                data0 = tdms.get_data(0, nCh, 0, tdms.channel_length - 1)
            else:
                data0 = tdms.get_data(64, nCh, 0, tdms.channel_length - 1)
            
            # Store the data in the array
            data[:, nsample_1min * i:nsample_1min * (i + 1)] = np.transpose(data0)[ch_info]
        
        # Downsample the data to match the sampling frequency
        self.data = downsample(data, 250 / fs)
   
    # Method to load .mat file data
    # def get_mat(self):
    #     # Open file dialog to select a .mat file
    #     filePath, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select data", '/Users/shouvikmajumder/Desktop/DAS_GUI/DasDataa/', '*.mat')
    #     if filePath:  # If a file is selected
    #         inputf = scipy.io.loadmat(str(filePath))  # Load the .mat file
    #         self.data = np.array(inputf['data'])  # Store the data in self.data

        

# Entry point of the application
if __name__ == '__main__':
    app = QtWidgets.QApplication([])  # Create a Qt application
    window = Mymain()  # Create an instance of Mymain
    window.show()  # Show the main window
    app.exec_()  # Start the event loop
