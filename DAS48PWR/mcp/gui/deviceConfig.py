# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deviceConfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import das01
import lanConfig 
import displayConfig 
import wifiConfig 
import displayConfig 
import systemConfig 
import accountConfig
import db
import log
import os
import sip
os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"

class Ui_ConfigWindow(object):
    windows=None
    def ack(self):
        das01.ack=1
        db.updDb.updData(1,"m_mesin","ack",1,"id",1)
    def mute(self):
        db.updDb.updData(1,"m_mesin","mute",0,"id",1)
    def reset(self):
        das01.ack=0
        db.updDb.rstMesin(1)
    def openLog(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = log.Ui_LogWindow()
        self.ui.setupUi(self.window)
        log.Ui_LogWindow.windows=self.window
        self.windows.close()
        self.window.show()
    def openHome(self):
        print("gotoHome")
       
        self.window = QtWidgets.QMainWindow()
        self.ui = das01.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.windows.destroy()
        self.windows=None
    
        das01.Ui_MainWindow.windows=self.window
    def openConfig(self):
        print("config")
        # self.window = QtWidgets.QMainWindow()
        # self.ui = Ui_ConfigWindow()
        # self.ui.setupUi(self.window)
        # Ui_ConfigWindow.windows=self.window
        # self.window.show()
    def openLan(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = lanConfig.Ui_LanWindow()
        self.ui.setupUi(self.window)
        self.window.show()
       
        sip.delete(self.windows)
        #self.windows.destroy()
        lanConfig.Ui_LanWindow.windows=self.window
    def openWifi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = wifiConfig.Ui_WifiWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        wifiConfig.Ui_WifiWindow.windows=self.window
    def openDisplay(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = displayConfig.Ui_DisplayWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.windows.destroy()
        displayConfig.Ui_DisplayWindow.windows=self.window
    def openSystem(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = systemConfig.Ui_SystemWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.windows.destroy()
        systemConfig.Ui_SystemWindow.windows=self.window
    def openAccount(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = accountConfig.Ui_AccountWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.windows.destroy()
        accountConfig.Ui_AccountWindow.windows=self.window



    def setupUi(self, ConfigWindow):
        ConfigWindow.setObjectName("ConfigWindow")
        ConfigWindow.resize(1280, 800)
        ConfigWindow.showFullScreen()
        #ConfigWindow.setAttribute(QtCore.WA_DeleteOnClose)
        
        max_x=ConfigWindow.width()
        max_y=ConfigWindow.height()
        ConfigWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget = QtWidgets.QWidget(ConfigWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(30, 100, max_x-60, 271))
        self.listView.setObjectName("listView")
        self.lineEdit_code = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_code.setGeometry(QtCore.QRect(40, 140, max_x-80, 26))
        self.lineEdit_code.setObjectName("lineEdit_code")
        self.lineEdit_code.setEnabled(False)

        self.label_form = QtWidgets.QLabel(self.centralwidget)
        self.label_form.setGeometry(QtCore.QRect(40, 120, 97, 20))
        self.label_form.setObjectName("label_form")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(40, 190, max_x-80, 26))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_name.setMaxLength(20)
        self.label_form_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_form_2.setGeometry(QtCore.QRect(40, 170, 97, 20))
        self.label_form_2.setObjectName("label_form_2")
        self.label_form_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_form_3.setGeometry(QtCore.QRect(40, 220, 97, 20))
        self.label_form_3.setObjectName("label_form_3")
        self.lineEdit_loc = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_loc.setGeometry(QtCore.QRect(40, 240, max_x-80, 26))
        self.lineEdit_loc.setObjectName("lineEdit_loc")
        self.lineEdit_loc.setMaxLength(20)
        self.label_form_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_form_4.setGeometry(QtCore.QRect(40, 270, 97, 20))
        self.label_form_4.setObjectName("label_form_4")
        self.lineEdit_bot = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_bot.setGeometry(QtCore.QRect(40, 290, max_x-80, 26))
        self.lineEdit_bot.setObjectName("lineEdit_bot")
        self.lineEdit_bot.setEnabled(False)
        self.pb_save_device = QtWidgets.QPushButton(self.centralwidget)
        self.pb_save_device.setGeometry(QtCore.QRect(40, 330, 191, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_save_device.setFont(font)
        self.pb_save_device.setObjectName("pb_save_device")
        self.pb_save_device.clicked.connect(self.showDialog)

        self.pb_device_active = QtWidgets.QPushButton(self.centralwidget)
        self.pb_device_active.setGeometry(QtCore.QRect(30, 40, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pb_device_active.setFont(font)
        self.pb_device_active.setObjectName("pb_device_active")

        self.pb_lan = QtWidgets.QPushButton(self.centralwidget)
        self.pb_lan.setGeometry(QtCore.QRect(130, 40, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_lan.setFont(font)
        self.pb_lan.setObjectName("pb_lan")
        self.pb_lan.clicked.connect(self.openLan)

        self.pb_wifi = QtWidgets.QPushButton(self.centralwidget)
        self.pb_wifi.setGeometry(QtCore.QRect(230, 40, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_wifi.setFont(font)
        self.pb_wifi.setObjectName("pb_wifi")
        self.pb_wifi.clicked.connect(self.openWifi)

        self.pb_display = QtWidgets.QPushButton(self.centralwidget)
        self.pb_display.setGeometry(QtCore.QRect(330, 40, 101, 31))
        self.pb_display.clicked.connect(self.openDisplay)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_display.setFont(font)
        self.pb_display.setObjectName("pb_display")

        self.pb_system = QtWidgets.QPushButton(self.centralwidget)
        self.pb_system.setGeometry(QtCore.QRect(430, 40, 101, 31))
        self.pb_system.clicked.connect(self.openSystem)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_system.setFont(font)
        self.pb_system.setObjectName("pb_system")

        self.pb_account = QtWidgets.QPushButton(self.centralwidget)
        self.pb_account.setGeometry(QtCore.QRect(530, 40, 101, 31))
        self.pb_account.clicked.connect(self.openAccount)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_account.setFont(font)
        self.pb_account.setObjectName("pb_account")
        
        self.label_device = QtWidgets.QLabel(self.centralwidget)
        self.label_device.setGeometry(QtCore.QRect(30, 80, max_x-60, 31))
        self.label_device.setObjectName("label_device")
        ConfigWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ConfigWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        ConfigWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ConfigWindow)
        self.statusbar.setObjectName("statusbar")
        ConfigWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ConfigWindow)
        QtCore.QMetaObject.connectSlotsByName(ConfigWindow)
        das01.Ui_MainWindow.setupfooter(self,ConfigWindow)

    def retranslateUi(self, ConfigWindow):
        _translate = QtCore.QCoreApplication.translate
        ConfigWindow.setWindowTitle(_translate("ConfigWindow", "MainWindow"))
        self.label_form.setText(_translate("ConfigWindow", "Device Code"))
        self.label_form_2.setText(_translate("ConfigWindow", "Device Name"))
        self.label_form_3.setText(_translate("ConfigWindow", "Location"))
        self.label_form_4.setText(_translate("ConfigWindow", "Bot Name"))
        self.pb_save_device.setText(_translate("ConfigWindow", "Save Configuration"))
        self.pb_device_active.setText(_translate("ConfigWindow", "Device Setting"))
        self.pb_lan.setText(_translate("ConfigWindow", "LAN Setting"))
        self.pb_wifi.setText(_translate("ConfigWindow", "WiFi Setting"))
        self.pb_display.setText(_translate("ConfigWindow", "Display Setting"))
        self.pb_system.setText(_translate("ConfigWindow", "System"))
        self.pb_account.setText(_translate("ConfigWindow", "My Account"))
        self.label_device.setText(_translate("ConfigWindow", "   Device Setting "))
        cfg= db.readDb.readM_mesin(1)
        print(cfg)

        self.lineEdit_code.setText(cfg[0]["sn"])
        self.lineEdit_name.setText(cfg[0]["nama"])
        self.lineEdit_loc.setText(cfg[0]["lokasi"])
        self.lineEdit_bot.setText(cfg[0]["botname"])
    def showDialog(self):
        msgBox = QtWidgets.QMessageBox()
        nama =self.lineEdit_name.text()
        lokasi=self.lineEdit_loc.text()
        if len(nama)>0 and len(lokasi)>0:
            res=db.updDb.updDeviceConfig(1,nama,lokasi)
            print(res)
            msgBox.setText("Your Data Has been Saved")
            msgBox.setWindowTitle("Status Message")  
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            returnValue = msgBox.exec()
            
        else:
            msgBox.setText("Your Data is Empty")
            msgBox.setWindowTitle("Status Message")  
            msgBox.setIcon(QtWidgets.QMessageBox.Warning)
            msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            returnValue = msgBox.exec()
            print("data is Empty")


        
        # msgBox.setText("Your Data Has Been Saved")
        # msgBox.setWindowTitle("Status Message")   
       
        # msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        # msgBox.buttonClicked.connect(self.msgButtonClick)
        # returnValue = msgBox.exec()
        # if returnValue == QtWidgets.QMessageBox.Ok:
        #     print('OK clicked')
    def msgButtonClick(self,i):
        print("Button clicked is:",i.text())
        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfigWindow = QtWidgets.QMainWindow()
    
    ui = Ui_ConfigWindow()
    ui.setupUi(ConfigWindow)
    ConfigWindow.show()
    sys.exit(app.exec_())
