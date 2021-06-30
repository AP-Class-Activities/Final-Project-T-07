
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_client_page(object):
    def setupUi(self, client_page):
        client_page.setObjectName("client_page")
        client_page.resize(501, 356)
        self.gridLayout_2 = QtWidgets.QGridLayout(client_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(client_page)
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.product_button = QtWidgets.QPushButton(client_page)
        self.product_button.setMaximumSize(QtCore.QSize(16777215, 35))
        self.product_button.setObjectName("product_button")
        self.verticalLayout.addWidget(self.product_button)
        self.wallet_Button = QtWidgets.QPushButton(client_page)
        self.wallet_Button.setMaximumSize(QtCore.QSize(16777215, 35))
        self.wallet_Button.setObjectName("wallet_Button")
        self.verticalLayout.addWidget(self.wallet_Button)
        self.sabad_Button = QtWidgets.QPushButton(client_page)
        self.sabad_Button.setMaximumSize(QtCore.QSize(16777215, 35))
        self.sabad_Button.setObjectName("sabad_Button")
        self.verticalLayout.addWidget(self.sabad_Button)
        self.wish_list_Button = QtWidgets.QPushButton(client_page)
        self.wish_list_Button.setMaximumSize(QtCore.QSize(16777215, 35))
        self.wish_list_Button.setObjectName("wish_list_Button")
        self.verticalLayout.addWidget(self.wish_list_Button)
        self.history_Button = QtWidgets.QPushButton(client_page)
        self.history_Button.setMaximumSize(QtCore.QSize(16777215, 35))
        self.history_Button.setObjectName("history_Button")
        self.verticalLayout.addWidget(self.history_Button)
        self.profile_Button = QtWidgets.QPushButton(client_page)
        self.profile_Button.setMaximumSize(QtCore.QSize(16777215, 35))
        self.profile_Button.setObjectName("profile_Button")
        self.verticalLayout.addWidget(self.profile_Button)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(client_page)
        QtCore.QMetaObject.connectSlotsByName(client_page)
        client_page.setTabOrder(self.product_button, self.wallet_Button)
        client_page.setTabOrder(self.wallet_Button, self.sabad_Button)
        client_page.setTabOrder(self.sabad_Button, self.wish_list_Button)
        client_page.setTabOrder(self.wish_list_Button, self.history_Button)

    def retranslateUi(self, client_page):
        _translate = QtCore.QCoreApplication.translate
        client_page.setWindowTitle(_translate("client_page", "Form"))
        self.label.setText(_translate("client_page", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#00aa00;\">منو مشتری</span></p><p align=\"center\"><span style=\" font-size:14pt;\">:یکی ازگزینه های زیر را انتخاب کنید</span></p></body></html>"))
        self.product_button.setText(_translate("client_page", "لیست محصولات"))
        self.wallet_Button.setText(_translate("client_page", "شارژ کیف پول"))
        self.sabad_Button.setText(_translate("client_page", "سبد خرید"))
        self.wish_list_Button.setText(_translate("client_page", "wish list"))
        self.history_Button.setText(_translate("client_page", "تاریخچه خرید های قبلی"))
        self.profile_Button.setText(_translate("client_page", "پروفایل"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    client_page = QtWidgets.QWidget()
    ui = Ui_client_page()
    ui.setupUi(client_page)
    client_page.show()
    sys.exit(app.exec_())
