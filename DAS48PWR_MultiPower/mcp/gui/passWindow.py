# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pass.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from pathlib import Path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from functools import partial
import deviceConfig
import das01
import db
inPass=""
bufPass=""

class Ui_PassWindow(object):
    windows=None
    windows2=None
    tim=None

    def setupUi(self, PassWindow):
        PassWindow.setObjectName("PassWindow")
        PassWindow.resize(1280, 800)
        PassWindow.showFullScreen()
        max_x=PassWindow.width()
        max_y=PassWindow.height()
        PassWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        PassWindow.setWindowOpacity(0.9) 
        self.centralwidget = QtWidgets.QWidget(PassWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pb1 = QtWidgets.QPushButton(self.centralwidget)
        self.pb1.setGeometry(QtCore.QRect((max_x/2-(321/2)), 360, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pb1.setFont(font)
        self.pb1.setObjectName("pb1")
        self.pb1.clicked.connect(partial(self.addLCD,1))
        self.pb2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb2.setGeometry(QtCore.QRect((max_x/2-(321/2))+110, 360, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pb2.setFont(font)
        self.pb2.setObjectName("pb2")
        self.pb2.clicked.connect(partial(self.addLCD,2))
        self.pb3 = QtWidgets.QPushButton(self.centralwidget)
        self.pb3.setGeometry(QtCore.QRect((max_x/2-(321/2))+220, 360, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pb3.setFont(font)
        self.pb3.setObjectName("pb3")
        self.pb3.clicked.connect(partial(self.addLCD,3))
        self.pb6 = QtWidgets.QPushButton(self.centralwidget)
        self.pb6.setGeometry(QtCore.QRect((max_x/2-(321/2))+220, 430, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pb6.setFont(font)
        self.pb6.setObjectName("pb6")
        self.pb6.clicked.connect(partial(self.addLCD,6))
        self.pb5 = QtWidgets.QPushButton(self.centralwidget)
        self.pb5.setGeometry(QtCore.QRect((max_x/2-(321/2))+110, 430, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pb5.setFont(font)
        self.pb5.setObjectName("pb5")
        self.pb5.clicked.connect(partial(self.addLCD,5))
        self.pb4 = QtWidgets.QPushButton(self.centralwidget)
        self.pb4.setGeometry(QtCore.QRect((max_x/2-(321/2)), 430, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pb4.setFont(font)
        self.pb4.setObjectName("pb4") 
        self.pb4.clicked.connect(partial(self.addLCD,4))
        self.pb9 = QtWidgets.QPushButton(self.centralwidget)
        self.pb9.setGeometry(QtCore.QRect((max_x/2-(321/2))+220, 500, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pb9.setFont(font)
        self.pb9.setObjectName("pb9")
        self.pb9.clicked.connect(partial(self.addLCD,9))
        self.pb8 = QtWidgets.QPushButton(self.centralwidget)
        self.pb8.setGeometry(QtCore.QRect((max_x/2-(321/2))+110, 500, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pb8.setFont(font)
        self.pb8.setObjectName("pb8")
        self.pb8.clicked.connect(partial(self.addLCD,8))
        self.pb7 = QtWidgets.QPushButton(self.centralwidget)
        self.pb7.setGeometry(QtCore.QRect((max_x/2-(321/2)), 500, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pb7.setFont(font)
        self.pb7.setObjectName("pb7")
        self.pb7.clicked.connect(partial(self.addLCD,7))
        self.pbclear = QtWidgets.QPushButton(self.centralwidget)
        self.pbclear.setGeometry(QtCore.QRect(max_x/2-(321/2)+220, 570, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pbclear.setFont(font)
        self.pbclear.setObjectName("pbclear")
        self.pbclear.clicked.connect(partial(self.addLCD,"#"))
        self.pb0 = QtWidgets.QPushButton(self.centralwidget)
        self.pb0.setGeometry(QtCore.QRect((max_x/2-(321/2))+110, 570, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pb0.setFont(font)
        self.pb0.setObjectName("pb0")
        self.pb0.clicked.connect(partial(self.addLCD,0))
        self.pbdel = QtWidgets.QPushButton(self.centralwidget)
        self.pbdel.setGeometry(QtCore.QRect((max_x/2-(321/2)), 570, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pbdel.setFont(font)
        self.pbdel.setObjectName("pbdel")
        self.pbdel.clicked.connect(partial(self.addLCD,"*"))
        self.pbenter = QtWidgets.QPushButton(self.centralwidget)
        self.pbenter.setGeometry(QtCore.QRect((max_x/2-(321/2))+160, 300, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pbenter.setFont(font)
        self.pbenter.setObjectName("pbenter")
        self.pbenter.clicked.connect(self.enterLCD)
        self.pbcancel = QtWidgets.QPushButton(self.centralwidget)
        self.pbcancel.setGeometry(QtCore.QRect(max_x/2-(321/2), 300, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pbcancel.setFont(font)
        self.pbcancel.setObjectName("pbcancel")
        self.pbcancel.clicked.connect(self.cancelLCD)
        self.lcd = QtWidgets.QFrame(self.centralwidget)
        self.lcd.setGeometry(QtCore.QRect(max_x/2-(321/2), 210, 321, 81))
        self.lcd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcd.setObjectName("lcd")
        self.lcd_pass = QtWidgets.QLineEdit(self.lcd)
        self.lcd.setWindowOpacity(1) 
        
        self.lcd_pass.setGeometry(QtCore.QRect(70, 40, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lcd_pass.setFont(font)
        self.lcd_pass.setAutoFillBackground(False)
        self.lcd_pass.setMaxLength(6)
        self.lcd_pass.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lcd_pass.setReadOnly(True)
        self.lcd_pass.setClearButtonEnabled(False)
        #self.lcd_pass.setEchoMode(QtWidgets.QLineEdit.Password)
       
        self.lcd_pass.setObjectName("lcd_pass")
        self.label = QtWidgets.QLabel(self.lcd)
        self.label.setGeometry(QtCore.QRect(80, 10, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        PassWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PassWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 339, 21))
        self.menubar.setObjectName("menubar")
        PassWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PassWindow)
        self.statusbar.setObjectName("statusbar")
        PassWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PassWindow)
        QtCore.QMetaObject.connectSlotsByName(PassWindow)
    def cancelLCD(self):
        #self.tim.start()
        self.windows.destroy()
    def enterLCD(self):
        global inPass
        bufAuth =db.readDb.readM_mesin(1)
        print(bufAuth)
        print(bufAuth[0]["auth"])
        print("================")
        print(inPass)
        if (str(bufAuth[0]["auth"])==inPass):
            self.window = QtWidgets.QMainWindow()
            self.ui = deviceConfig.Ui_ConfigWindow()
            self.ui.setupUi(self.window)
            deviceConfig.Ui_ConfigWindow.windows=self.window
            self.windows.destroy()
            self.windows2.destroy()
            self.window.show()
            if ( self.tim != None):
                self.tim.stop()
            
        else:
            _translate = QtCore.QCoreApplication.translate
            self.label.setText(_translate("PassWindow", "Pass Invalid"))
        
    def addLCD(self,param): 
        global inPass
        global bufPass
        if param =="*":
            print("clear")
            inPass=inPass[:-1]
            bufPass=bufPass[:-1]
        elif param =="#":
            inPass=""
            bufPass=""
        else:
            if len(inPass)<6:
                inPass +=str(param)
                bufPass += "*"
        _translate = QtCore.QCoreApplication.translate
        self.lcd_pass.setText(_translate("PassWindow", str(bufPass)))

    def retranslateUi(self, PassWindow):
        global inPass,bufPass
        inPass=""
        bufPass=""
        _translate = QtCore.QCoreApplication.translate
        PassWindow.setWindowTitle(_translate("PassWindow", "PassWindow"))
        self.pb1.setText(_translate("PassWindow", "1"))
        self.pb2.setText(_translate("PassWindow", "2"))
        self.pb3.setText(_translate("PassWindow", "3"))
        self.pb6.setText(_translate("PassWindow", "6"))
        self.pb5.setText(_translate("PassWindow", "5"))
        self.pb4.setText(_translate("PassWindow", "4"))
        self.pb9.setText(_translate("PassWindow", "9"))
        self.pb8.setText(_translate("PassWindow", "8"))
        self.pb7.setText(_translate("PassWindow", "7"))
        self.pbclear.setText(_translate("PassWindow", "#"))
        self.pb0.setText(_translate("PassWindow", "0"))
        self.pbdel.setText(_translate("PassWindow", "*"))
        self.pbenter.setText(_translate("PassWindow", "ENTER"))
        self.pbcancel.setText(_translate("PassWindow", "CANCEL"))
        self.lcd_pass.setText(_translate("PassWindow", ""))
        self.label.setText(_translate("PassWindow", "ENTER PIN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PassWindow = QtWidgets.QMainWindow()
    
    app.setStyle(QStyleFactory.create('Cleanlooks'))
    app.setStyleSheet(Path('style.qss').read_text())
    ui = Ui_PassWindow()
    ui.setupUi(PassWindow)
    PassWindow.show()
    sys.exit(app.exec_())
