
#this file include SIGNUP graphic codes for client


import salesMan_login
from PyQt5 import QtCore , QtGui , QtWidgets

class Ui_Form(object):
    def setupUi(self,window):
        window.setObjectName("Online Shopping")
        window.resize(621, 529)
        Form = QtWidgets.QWidget(window)
        Form.setObjectName("centralwidget")
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
        self.signin = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.signin.setFont(font)
        self.signin.setObjectName("signin")
        self.verticalLayout.addWidget(self.signin)
        self.signin.clicked.connect(self.signinaccount)
        self.signLabel = QtWidgets.QLabel(Form)
        self.signLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.signLabel.setFont(font)
        self.signLabel.setText("")
        self.signLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.signLabel.setObjectName("signLabel")
        self.verticalLayout.addWidget(self.signLabel)
        window.setCentralWidget(Form)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def gotologin(self):
        self.loginpage = QtWidgets.QMainWindow()
        self.ui = salesMan_login.Ui_Form()
        self.ui.setupUi(self.loginpage)
        self.loginpage.show()
        Form.close()

    def signinaccount(self):
        username = self.UserLine.text()
        password = self.passLine.text()
        username1 = str([a.replace('\n','').split() for a in username])
        password1 = str([a.replace('\n','').split() for a in password])
        if (len(username1[0])!=0) and (len(password1[0])!=0):
            users = open('database.txt','r')
            users.readlines()
            users = [u.replace('\n','').split() for u in users]
            flag = False
            for i in range (len(users)):
                if username == users[i][0] :
                    flag = True
                    self.signLabel.setStyleSheet('color:red;')
                    self.signLabel.setText("نام کاربری یا رمز عبور معتبر نمیباشد")
                    break
            if flag == False:
                self.signLabel.setStyleSheet('color:green;')
                self.signLabel.setText("ثبت نام با موفقیت صورت گرفت \n {} خوش آمدید".format(username))
                users = open('database.txt','a')
                users.write("\n"+username+" "+password)
                users.close()
                self.gotologin()
        else:
            self.signLabel.setStyleSheet('color:red;')
            self.signLabel.setText("نام کاربری یا رمز عبور معتبر نمیباشد")
        
    def retranslateUi(self,Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Online Shopping","Online Shopping"))
        self.label.setText(_translate("Online Shopping","ثبت نام فروشنده"))
        self.label_2.setText(_translate("Online Shopping","نام کاربری:"))
        self.label_3.setText(_translate("Online Shopping","رمز عبور:"))
        self.signin.setText(_translate("Online Shopping","ذخیره"))


if __name__ =="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())




