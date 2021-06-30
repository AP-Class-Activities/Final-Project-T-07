
#this file include LOGIN graphic codes for operator

from PyQt5 import QtCore , QtGui , QtWidgets

class Ui_Form(object):
    def setupUi(self,window):
        window.setObjectName("Online Shopping")
        window.resize(621, 529)
        Form = QtWidgets.QWidget(window)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(16777215,50))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.UserLine = QtWidgets.QLineEdit(Form)
        self.UserLine.setObjectName("userLine")
        self.gridLayout.addWidget(self.UserLine , 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1,1)
        self.passLine = QtWidgets.QLineEdit(Form)
        self.passLine.setInputMask("")
        self.passLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passLine.setObjectName("PassLine")
        self.gridLayout.addWidget(self.passLine, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.Login = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Login.setFont(font)
        self.Login.setObjectName("Login")
        self.verticalLayout.addWidget(self.Login)
        self.Login.clicked.connect(self.loginaccount)
        self.LogLabel = QtWidgets.QLabel(Form)
        self.LogLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LogLabel.setFont(font)
        self.LogLabel.setText("")
        self.LogLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LogLabel.setObjectName("LogLabel")
        self.verticalLayout.addWidget(self.LogLabel)
        window.setCentralWidget(window)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    
    def loginaccount(self):
        username = self.UserLine.text()
        password = self.passLine.text()
        if username == 'admin1234' and password == 'admin1234':
            self.LogLabel.setStyleSheet('color:green;')
            self.LogLabel.setText("ورود اپراتور با موفقیت صورت گرفت")
        else:
            self.LogLabel.setStyleSheet('color:red;')
            self.LogLabel.setText("تنها ورود اپراتور مجاز است")
    
    
    def retranslateUi(self,Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Online Shopping","Online Shopping"))
        self.label.setText(_translate("Online Shopping","ورود اپراتور"))
        self.label_2.setText(_translate("Online Shopping","نام اپراتور"))
        self.label_3.setText(_translate("Online Shopping","کلمه عبور:"))
        self.Login.setText(_translate("Online Shopping","ورود"))


if __name__ =="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


