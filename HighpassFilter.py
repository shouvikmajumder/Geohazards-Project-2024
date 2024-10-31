# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HighpassFilter.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_HighPass(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget_HighPass = QtWidgets.QWidget(MainWindow)
        self.centralwidget_HighPass.setObjectName("centralwidget_HighPass")
        self.frame_HighPass = QtWidgets.QFrame(self.centralwidget_HighPass)
        self.frame_HighPass.setGeometry(QtCore.QRect(0, 0, 791, 471))
        self.frame_HighPass.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_HighPass.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_HighPass.setObjectName("frame_HighPass")
        self.frame_2_HighPass = QtWidgets.QFrame(self.frame_HighPass)
        self.frame_2_HighPass.setGeometry(QtCore.QRect(240, 20, 301, 41))
        self.frame_2_HighPass.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2_HighPass.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2_HighPass.setObjectName("frame_2_HighPass")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2_HighPass)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 301, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.frame_3_HighPass = QtWidgets.QFrame(self.frame_HighPass)
        self.frame_3_HighPass.setGeometry(QtCore.QRect(10, 90, 761, 381))
        self.frame_3_HighPass.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3_HighPass.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3_HighPass.setObjectName("frame_3_HighPass")
        self.frame_4_HighPass = QtWidgets.QFrame(self.frame_3_HighPass)
        self.frame_4_HighPass.setGeometry(QtCore.QRect(10, 10, 221, 361))
        self.frame_4_HighPass.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4_HighPass.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4_HighPass.setObjectName("frame_4_HighPass")
        self.label_3_HighPass = QtWidgets.QLabel(self.frame_4_HighPass)
        self.label_3_HighPass.setGeometry(QtCore.QRect(10, 140, 59, 16))
        self.label_3_HighPass.setObjectName("label_3_HighPass")
        self.label_HighPass = QtWidgets.QLabel(self.frame_4_HighPass)
        self.label_HighPass.setGeometry(QtCore.QRect(10, 40, 59, 16))
        self.label_HighPass.setObjectName("label_HighPass")
        self.lineEdit_freq2_HighPass = QtWidgets.QLineEdit(self.frame_4_HighPass)
        self.lineEdit_freq2_HighPass.setGeometry(QtCore.QRect(140, 140, 51, 21))
        self.lineEdit_freq2_HighPass.setObjectName("lineEdit_freq2_HighPass")
        self.pushButton_test_HighPass = QtWidgets.QPushButton(self.frame_4_HighPass)
        self.pushButton_test_HighPass.setGeometry(QtCore.QRect(80, 200, 113, 32))
        self.pushButton_test_HighPass.setObjectName("pushButton_test_HighPass")
        self.label_4_HighPass = QtWidgets.QLabel(self.frame_4_HighPass)
        self.label_4_HighPass.setGeometry(QtCore.QRect(20, 10, 59, 16))
        self.label_4_HighPass.setObjectName("label_4_HighPass")
        self.lineEdit_ch_HighPass = QtWidgets.QLineEdit(self.frame_4_HighPass)
        self.lineEdit_ch_HighPass.setGeometry(QtCore.QRect(80, 70, 111, 21))
        self.lineEdit_ch_HighPass.setObjectName("lineEdit_ch_HighPass")
        self.lineEdit_time_HighPass = QtWidgets.QLineEdit(self.frame_4_HighPass)
        self.lineEdit_time_HighPass.setGeometry(QtCore.QRect(80, 40, 111, 21))
        self.lineEdit_time_HighPass.setTabletTracking(False)
        self.lineEdit_time_HighPass.setObjectName("lineEdit_time_HighPass")
        self.pushButton_setup_parameters_HighPass = QtWidgets.QPushButton(self.frame_4_HighPass)
        self.pushButton_setup_parameters_HighPass.setGeometry(QtCore.QRect(80, 170, 113, 32))
        self.pushButton_setup_parameters_HighPass.setObjectName("pushButton_setup_parameters_HighPass")
        self.checkBox_normalize_HighPass = QtWidgets.QCheckBox(self.frame_4_HighPass)
        self.checkBox_normalize_HighPass.setGeometry(QtCore.QRect(80, 90, 111, 20))
        self.checkBox_normalize_HighPass.setObjectName("checkBox_normalize_HighPass")
        self.pushButton_export_HighPass = QtWidgets.QPushButton(self.frame_4_HighPass)
        self.pushButton_export_HighPass.setGeometry(QtCore.QRect(40, 320, 121, 31))
        self.pushButton_export_HighPass.setObjectName("pushButton_export_HighPass")
        self.lineEdit_freq1_HighPass = QtWidgets.QLineEdit(self.frame_4_HighPass)
        self.lineEdit_freq1_HighPass.setGeometry(QtCore.QRect(80, 140, 51, 21))
        self.lineEdit_freq1_HighPass.setObjectName("lineEdit_freq1_HighPass")
        self.label_2_HighPass = QtWidgets.QLabel(self.frame_4_HighPass)
        self.label_2_HighPass.setGeometry(QtCore.QRect(10, 70, 59, 16))
        self.label_2_HighPass.setObjectName("label_2_HighPass")
        self.lineEdit_fs_HighPass = QtWidgets.QLineEdit(self.frame_4_HighPass)
        self.lineEdit_fs_HighPass.setGeometry(QtCore.QRect(80, 10, 51, 21))
        self.lineEdit_fs_HighPass.setObjectName("lineEdit_fs_HighPass")
        self.frame_5_HighPass = QtWidgets.QFrame(self.frame_3_HighPass)
        self.frame_5_HighPass.setGeometry(QtCore.QRect(240, 10, 511, 361))
        self.frame_5_HighPass.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5_HighPass.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5_HighPass.setObjectName("frame_5_HighPass")
        self.MplWidget_2_HighPass = MplWidget(self.frame_5_HighPass)
        self.MplWidget_2_HighPass.setGeometry(QtCore.QRect(10, 10, 480, 331))
        self.MplWidget_2_HighPass.setMinimumSize(QtCore.QSize(480, 320))
        self.MplWidget_2_HighPass.setObjectName("MplWidget_2_HighPass")
        MainWindow.setCentralWidget(self.centralwidget_HighPass)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Highpass Filter</span></p></body></html>"))
        self.label_3_HighPass.setText(_translate("MainWindow", "Freq"))
        self.label_HighPass.setText(_translate("MainWindow", "Minute"))
        self.lineEdit_freq2_HighPass.setText(_translate("MainWindow", "24"))
        self.pushButton_test_HighPass.setText(_translate("MainWindow", "test"))
        self.label_4_HighPass.setText(_translate("MainWindow", "Fs"))
        self.lineEdit_ch_HighPass.setText(_translate("MainWindow", "0-2120"))
        self.lineEdit_time_HighPass.setText(_translate("MainWindow", "0"))
        self.pushButton_setup_parameters_HighPass.setText(_translate("MainWindow", "Confirm"))
        self.checkBox_normalize_HighPass.setText(_translate("MainWindow", "Normalization"))
        self.pushButton_export_HighPass.setText(_translate("MainWindow", "Export"))
        self.lineEdit_freq1_HighPass.setText(_translate("MainWindow", "0.5"))
        self.label_2_HighPass.setText(_translate("MainWindow", "Channel"))
        self.lineEdit_fs_HighPass.setText(_translate("MainWindow", "500"))
from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_HighPass = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_HighPass()
    ui.setupUi(MainWindow_HighPass)
    MainWindow_HighPass.show()
    sys.exit(app.exec_())