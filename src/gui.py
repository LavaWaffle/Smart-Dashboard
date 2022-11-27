from PyQt5 import QtCore, QtGui, QtWidgets, sip

class KeyValueFrame(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("frame2")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(6)
        self.layout.setObjectName("verticalLayout_2")
        self.key = QtWidgets.QLabel(self)
        self.key.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.key.setFont(font)
        self.key.setAutoFillBackground(False)
        self.key.setTextFormat(QtCore.Qt.AutoText)
        self.key.setAlignment(QtCore.Qt.AlignCenter)
        self.key.setObjectName("key")
        self.layout.addWidget(self.key, 0, QtCore.Qt.AlignTop)
        self.value = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.value.setFont(font)
        self.value.setAlignment(QtCore.Qt.AlignCenter)
        self.value.setObjectName("value")
        self.layout.addWidget(self.value)

    def set_key(self, key):
        if self.key.text() != key:
            self.key.setText(key)
            self.key.repaint()
    
    def set_value(self, value):
        # check if value isnt current text
        if self.value.text() != value:
            self.value.setText(str(value))
            self.value.repaint()
    
    def set_key_value(self, key, value):
        self.set_key(key)
        self.set_value(value)
        
    
    def remove(self, layout):
        layout.removeWidget(self)
        sip.delete(self)
        self = None

        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Smart Dashboard")
        MainWindow.resize(800, 598)
        MainWindow.setStyleSheet("* {\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"}\n"
"#centralwidget {\n"
"    background-color: #191925;\n"
"}\n"
"QFrame {\n"
"    border: 2px solid #000;\n"
"    background-color: #101018;\n"
"}\n"
"#key{\n"
"    color: white;\n"
"    background-color: #3c3c50;\n"
"    border: none;\n"
"}\n"
"#value{\n"
"    border: none;\n"
"    text-decoration: underline;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sideMenu = QtWidgets.QWidget(self.centralwidget)
        self.sideMenu.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sideMenu.setObjectName("sideMenu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sideMenu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.sideMenu)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.sideMenu)
        self.mainMenu = QtWidgets.QWidget(self.centralwidget)
        self.mainMenu.setObjectName("mainMenu")
        self.gridLayout = QtWidgets.QGridLayout(self.mainMenu)
        self.gridLayout.setObjectName("gridLayout")
        
        self.frames = []
        for i in range(16):
            self.frames.append(KeyValueFrame(self.mainMenu))
            self.frames[i].set_key_value('key '+str(i), 'value '+str(i))
            self.gridLayout.addWidget(self.frames[i], i // 4, i % 4, 1, 1)



        self.horizontalLayout.addWidget(self.mainMenu)

        

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TODO: ADD SIDE MENU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())