import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import *


class VKQLineEdit(QLineEdit):
    def __init__(self, parent=None, name=None, mainWindowObj=None):
        super(VKQLineEdit, self).__init__(parent)
        self.name = name
        self.setFixedHeight(40)
        self.mainWindowObj = mainWindowObj
        self.setFocusPolicy(Qt.ClickFocus)

    def focusInEvent(self, e):
        self.mainWindowObj.keyboardWidget.currentTextBox = self
        self.mainWindowObj.keyboardWidget.show()

        self.setStyleSheet("border: 1px solid red;")
        super(VKQLineEdit, self).focusInEvent(e)

    def mousePressEvent(self, e):
        # print(e)
        self.setFocusPolicy(Qt.ClickFocus)
        super(VKQLineEdit, self).mousePressEvent(e)


class KeyboardWidget(QWidget):
    def __init__(self, parent=None):
        super(KeyboardWidget, self).__init__(parent)
        self.currentTextBox = None

        self.signalMapper = QSignalMapper(self)
        self.signalMapper.mapped[int].connect(self.buttonClicked)

        self.initUI()

    @pyqtSlot()
    def do_caps(self):
        # self.timer.start()
        self.names = self.names_caps
        self.buttonAdd()
        self.cap_button.setText("Caps")
        self.cap_button.clicked.disconnect()
        self.cap_button.clicked.connect(self.do_small)

    @pyqtSlot()
    def do_small(self):
        # self.timer.stop()
        self.names = self.names_small
        self.buttonAdd()
        self.cap_button.setText("Small")
        self.cap_button.clicked.disconnect()
        self.cap_button.clicked.connect(self.do_caps)

    def initUI(self):
        self.layout = QGridLayout()

        # p = self.palette()
        # p.setColor(self.backgroundRole(),Qt.white)
        # self.setPalette(p)
        self.setAutoFillBackground(True)
        self.text_box = QTextEdit()
        self.text_box.setFont(QFont('Arial', 12))
        # text_box.setFixedHeight(50)
        # self.text_box.setFixedWidth(300)
        self.layout.addWidget(self.text_box, 0, 0, 1, 10)

        self.names_caps = ['1', '2', '3', '4', '5', '5', '7', '8', '9', '0', '.', '(', ')',
                           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.names_small = ['1', '2', '3', '4', '5', '5', '7', '8', '9', '0', '.', '(', ')',
                            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.names_sym = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.',
                          '~', '`', '@', '#', '$', '%', '^', '&&', '*', '(',
                          ')', '_', '-', '+', '=', '|', '[', ']', '{', '}', "'",
                          '"', '<', '>', '?', '\\', '/', '!']
        self.names = self.names_small
        self.buttonAdd()
        # Cancel button
        # cancel_button.setFixedHeight(25)
        '''cancel_button = QPushButton('Cancel')
        cancel_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        cancel_button.setFont(QFont('Arial', 12))
        cancel_button.KEY_CHAR = Qt.Key_Cancel
        self.layout.addWidget(cancel_button, 5, 0, 1, 2)
        cancel_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(cancel_button, cancel_button.KEY_CHAR)'''
        # cancel_button.setFixedWidth(60)

        # Cancel button
        clear_button = QPushButton('Clear')
        # clear_button.setFixedHeight(25)
        clear_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        clear_button.setFont(QFont('Arial', 12))
        clear_button.KEY_CHAR = Qt.Key_Clear
        self.layout.addWidget(clear_button, 5, 0, 1, 2)
        # self.layout.addWidget(clear_button, 8, 2, 1, 2)
        clear_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(clear_button, clear_button.KEY_CHAR)
        # clear_button.setFixedWidth(60)

        # Space button
        space_button = QPushButton('Space')
        # space_button.setFixedHeight(25)
        space_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        space_button.setFont(QFont('Arial', 12))
        space_button.KEY_CHAR = Qt.Key_Space
        self.layout.addWidget(space_button, 5, 2, 1, 2)
        # self.layout.addWidget(space_button, 5, 4, 1, 3)
        space_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(space_button, space_button.KEY_CHAR)
        # space_button.setFixedWidth(85)

        # Back button
        back_button = QPushButton('Back')
        # back_button.setFixedHeight(25)
        back_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        back_button.setFont(QFont('Arial', 12))
        back_button.KEY_CHAR = Qt.Key_Backspace
        self.layout.addWidget(back_button, 5, 4, 1, 2)
        # self.layout.addWidget(back_button, 5, 7, 1, 2)
        back_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(back_button, back_button.KEY_CHAR)
        # back_button.setFixedWidth(60)

        # Enter button
        enter_button = QPushButton('Enter')
        # enter_button.setFixedHeight(25)
        enter_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        enter_button.setFont(QFont('Arial', 12))
        enter_button.KEY_CHAR = Qt.Key_Enter
        self.layout.addWidget(enter_button, 5, 6, 1, 2)
        # self.layout.addWidget(enter_button, 5, 9, 1, 2)
        enter_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(enter_button, enter_button.KEY_CHAR)
        # enter_button.setFixedWidth(60)

        # Done button
        done_button = QPushButton('Done')
        # done_button.setFixedHeight(25)
        done_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        done_button.setFont(QFont('Arial', 12))
        done_button.KEY_CHAR = Qt.Key_Home
        self.layout.addWidget(done_button, 4, 9, 1, 1)
        # self.layout.addWidget(done_button, 5, 11, 1, 2)
        done_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(done_button, done_button.KEY_CHAR)
        # done_button.setFixedWidth(60)

        # Done button
        self.cap_button = QPushButton('Caps')
        # self.cap_button.setFixedHeight(25)
        self.cap_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.cap_button.setFont(QFont('Arial', 12))
        self.cap_button.KEY_CHAR = Qt.Key_Up
        self.layout.addWidget(self.cap_button, 5, 8, 1, 1)
        # self.layout.addWidget(self.cap_button, 5, 13, 1, 2)
        self.cap_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(self.cap_button, self.cap_button.KEY_CHAR)
        # self.cap_button.setFixedWidth(60)
        self.cap_button.clicked.connect(self.do_caps)
        # Done button

        sym_button = QPushButton('Sym')
        # sym_button.setFixedHeight(25)
        # sym_button.setFixedWidth(60)
        sym_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sym_button.setFont(QFont('Arial', 12))
        sym_button.KEY_CHAR = Qt.Key_Down
        self.layout.addWidget(sym_button, 5, 9, 1, 1)
        # self.layout.addWidget(sym_button, 5, 15, 1, 2)
        sym_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(sym_button, sym_button.KEY_CHAR)

        self.setGeometry(0, 0, 480, 300)

        self.setLayout(self.layout)

    def buttonAdd(self):
        # self.names = self.names_small
        print("loe")
        positions = [(i + 1, j) for i in range(6) for j in range(10)]

        for position, name in zip(positions, self.names):

            if name == '':
                continue
            button = QPushButton(name)
            button.setFont(QFont('Arial', 12))
            # button.setFixedHeight(25)
            # button.setFixedWidth(25)
            # button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

            button.KEY_CHAR = ord(name[-1])
            button.clicked.connect(self.signalMapper.map)
            self.signalMapper.setMapping(button, button.KEY_CHAR)
            self.layout.addWidget(button, *position)

    def buttonClicked(self, char_ord):
        txt = self.text_box.toPlainText()
        if char_ord == Qt.Key_Up:
            pass
        elif char_ord == Qt.Key_Down:
            self.names = self.names_sym
            self.buttonAdd()
        elif char_ord == Qt.Key_Backspace:
            txt = txt[:-1]
        elif char_ord == Qt.Key_Enter:
            txt += chr(10)
        elif char_ord == Qt.Key_Home:
            self.currentTextBox.setText(txt)
            self.text_box.setText("")
            self.hide()
            return
        elif char_ord == Qt.Key_Clear:
            txt = ""
        elif char_ord == Qt.Key_Space:
            txt += ' '
        else:
            txt += chr(char_ord)

        self.text_box.setText(txt)


class cQLineEdit(QLineEdit):
    clicked = pyqtSignal()

    def __init__(self, widget):
        super().__init__(widget)

    def mousePressEvent(self, QMouseEvent):
        self.se=KeyboardWidget()
        self.se.show()
        self.clicked.emit()


class KeyboardUI(QMainWindow):
    def __init__(self, obj):
        super().__init__()
        self.einiUI2(obj)

    def einiUI2(self, obj):
        first_name = VKQLineEdit(name=obj, mainWindowObj=self)

        mainWidget = QWidget()
        layout = QGridLayout()
        layout.addWidget(first_name, 0, 0)
        self.keyboardWidget = KeyboardWidget()
        layout.addWidget(self.keyboardWidget, 0, 0, 10, 10)
        mainWidget.setLayout(layout)

        self.keyboardWidget.hide()
        self.setCentralWidget(mainWidget)
        # self.statusBar().showMessage('Ready')
        self.setGeometry(0, 0, 480, 320)
        self.setWindowTitle('Keyboard')
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    ex = KeyboardUI(app)
    ex.show()
    sys.exit(app.exec_())