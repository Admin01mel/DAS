# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wifiConfig.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import deviceConfig 
import lanConfig
import displayConfig 
import displayConfig 
import systemConfig 
import accountConfig
import das01
import db
import log
class Ui_WifiWindow(object):
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
        self.windows.destroy()
        self.window.show()
    def openHome(self):
        print("gotoHome")
        self.window = QtWidgets.QMainWindow()
        self.ui = das01.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.windows.destroy()
        das01.Ui_MainWindow.windows=self.window
    def openConfig(self):
        self.window = QtWidgets.QMainWindow()
        #print(deviceConfig)
        self.ui = deviceConfig.Ui_ConfigWindow()
        self.ui.setupUi(self.window)
        deviceConfig.Ui_ConfigWindow.windows=self.window
        self.window.show()
        self.windows.destroy()
    def openLan(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = lanConfig.Ui_LanWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.windows.destroy()
        lanConfig.Ui_LanWindow.windows=self.window
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

    def setupUi(self, WifiWindow):
        WifiWindow.setObjectName("WifiWindow")
        WifiWindow.resize(1280, 800)
        max_x=WifiWindow.width()
        max_y=WifiWindow.height()
        WifiWindow.showFullScreen()
        WifiWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget = QtWidgets.QWidget(WifiWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(30, 100, max_x-60, 171))
        self.listView.setObjectName("listView")
        self.lineEdit_ssid = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ssid.setGeometry(QtCore.QRect(40, 140, max_x-80, 26))
        self.lineEdit_ssid.setObjectName("lineEdit_ssid")
        self.label_form = QtWidgets.QLabel(self.centralwidget)
        self.label_form.setGeometry(QtCore.QRect(40, 120, 97, 20))
        self.label_form.setObjectName("label_form")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pass.setGeometry(QtCore.QRect(40, 190, max_x-80, 26))
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_form_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_form_2.setGeometry(QtCore.QRect(40, 170, 97, 20))
        self.label_form_2.setObjectName("label_form_2")
        self.pb_save_wifi = QtWidgets.QPushButton(self.centralwidget)
        self.pb_save_wifi.setGeometry(QtCore.QRect(40, 230, 191, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_save_wifi.setFont(font)
        self.pb_save_wifi.setObjectName("pb_save_wifi")
        self.pb_save_wifi.clicked.connect(self.showDialog)

        self.pb_device = QtWidgets.QPushButton(self.centralwidget)
        self.pb_device.setGeometry(QtCore.QRect(30, 40, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pb_device.setFont(font)
        self.pb_device.setObjectName("pb_device")
        self.pb_device.clicked.connect(self.openConfig)

        self.pb_lan = QtWidgets.QPushButton(self.centralwidget)
        self.pb_lan.setGeometry(QtCore.QRect(130, 40, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_lan.setFont(font)
        self.pb_lan.setObjectName("pb_lan")
        self.pb_lan.clicked.connect(self.openLan)

        self.pb_wifi_active = QtWidgets.QPushButton(self.centralwidget)
        self.pb_wifi_active.setGeometry(QtCore.QRect(230, 40, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_wifi_active.setFont(font)
        self.pb_wifi_active.setObjectName("pb_wifi_active")
        self.pb_display = QtWidgets.QPushButton(self.centralwidget)
        self.pb_display.setGeometry(QtCore.QRect(330, 40, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_display.setFont(font)
        self.pb_display.setObjectName("pb_display")
        self.pb_display.clicked.connect(self.openDisplay)
        
        self.pb_system = QtWidgets.QPushButton(self.centralwidget)
        self.pb_system.setGeometry(QtCore.QRect(430, 40, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_system.setFont(font)
        self.pb_system.setObjectName("pb_system")
        self.pb_system.clicked.connect(self.openSystem)

        self.pb_account = QtWidgets.QPushButton(self.centralwidget)
        self.pb_account.setGeometry(QtCore.QRect(530, 40, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pb_account.setFont(font)
        self.pb_account.setObjectName("pb_account")
        self.pb_account.clicked.connect(self.openAccount)

        self.label_device = QtWidgets.QLabel(self.centralwidget)
        self.label_device.setGeometry(QtCore.QRect(30, 80, max_x-60, 31))
        self.label_device.setObjectName("label_device")
        WifiWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WifiWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        WifiWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WifiWindow)
        self.statusbar.setObjectName("statusbar")
        WifiWindow.setStatusBar(self.statusbar)

        self.retranslateUi(WifiWindow)
        QtCore.QMetaObject.connectSlotsByName(WifiWindow)
        das01.Ui_MainWindow.setupfooter(self,WifiWindow)



    def retranslateUi(self, WifiWindow):
        _translate = QtCore.QCoreApplication.translate
        WifiWindow.setWindowTitle(_translate("WifiWindow", "MainWindow"))
        self.label_form.setText(_translate("WifiWindow", "SSID"))
        self.label_form_2.setText(_translate("WifiWindow", "PASSWORD"))
        self.pb_save_wifi.setText(_translate("WifiWindow", "Save Configuration"))
        self.pb_device.setText(_translate("WifiWindow", "Device Setting"))
        self.pb_lan.setText(_translate("WifiWindow", "LAN Setting"))
        self.pb_wifi_active.setText(_translate("WifiWindow", "WiFi Setting"))
        self.pb_display.setText(_translate("WifiWindow", "Display Setting"))
        self.pb_system.setText(_translate("WifiWindow", "System"))
        self.pb_account.setText(_translate("WifiWindow", "My Account"))
        self.label_device.setText(_translate("WifiWindow", "   WIFI Setting "))
        cfg= db.readDb.readDataTabel(1,"wifi")
        self.lineEdit_ssid.setText(cfg[0]["ssid"])
        self.lineEdit_pass.setText(cfg[0]["pass"])
    
    def showDialog(self):
        msgBox      = QtWidgets.QMessageBox()
        ssid        =self.lineEdit_ssid.text()
        password    =self.lineEdit_pass.text()
      
      
        if len(ssid)>0 and len(password)>0 :
            db.updDb.updateWifi(0,ssid,password)
            #res=db.updDb.updDeviceConfig(1,nama,lokasi)
            #print(res)
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WifiWindow = QtWidgets.QMainWindow()
    ui = Ui_WifiWindow()
    ui.setupUi(WifiWindow)
    WifiWindow.show()
    sys.exit(app.exec_())
