# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saleman_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_saleman(object):
    def setupUi(self, saleman):
        saleman.setObjectName("saleman")
        saleman.resize(533, 467)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(saleman)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.saleman_label = QtWidgets.QLabel(saleman)
        self.saleman_label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.saleman_label.setObjectName("saleman_label")
        self.verticalLayout.addWidget(self.saleman_label)
        self.product_Button = QtWidgets.QPushButton(saleman)
        self.product_Button.setEnabled(True)
        self.product_Button.setMaximumSize(QtCore.QSize(16777215, 70))
        self.product_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.product_Button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.product_Button.setAutoRepeat(False)
        self.product_Button.setAutoDefault(False)
        self.product_Button.setDefault(False)
        self.product_Button.setFlat(False)
        self.product_Button.setObjectName("product_Button")
        self.verticalLayout.addWidget(self.product_Button)
        self.saleman_profile_Button = QtWidgets.QPushButton(saleman)
        self.saleman_profile_Button.setMaximumSize(QtCore.QSize(16777215, 70))
        self.saleman_profile_Button.setObjectName("saleman_profile_Button")
        self.verticalLayout.addWidget(self.saleman_profile_Button)
        self.rate_Button = QtWidgets.QPushButton(saleman)
        self.rate_Button.setMaximumSize(QtCore.QSize(16777215, 70))
        self.rate_Button.setObjectName("rate_Button")
        self.verticalLayout.addWidget(self.rate_Button)
        self.history_saleman_Button = QtWidgets.QPushButton(saleman)
        self.history_saleman_Button.setMaximumSize(QtCore.QSize(16777215, 70))
        self.history_saleman_Button.setObjectName("history_saleman_Button")
        self.verticalLayout.addWidget(self.history_saleman_Button)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(saleman)
        QtCore.QMetaObject.connectSlotsByName(saleman)

    def retranslateUi(self, saleman):
        _translate = QtCore.QCoreApplication.translate
        saleman.setWindowTitle(_translate("saleman", "Form"))
        self.saleman_label.setText(_translate("saleman", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#00aa00;\">منو فروشنده</span></p><p align=\"center\"><span style=\" font-size:14pt;\">:یکی از گزینه های زیررا انتخاب کنید</span></p></body></html>"))
        self.product_Button.setText(_translate("saleman", "لیست محصولات"))
        self.saleman_profile_Button.setText(_translate("saleman", " .. پروفایل .."))
        self.rate_Button.setText(_translate("saleman", " ⭐⭐  مشاهده امتیازات  ⭐⭐"))
        self.history_saleman_Button.setText(_translate("saleman", " 💲 آمار فروش 💲"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    saleman = QtWidgets.QWidget()
    ui = Ui_saleman()
    ui.setupUi(saleman)
    saleman.show()
    sys.exit(app.exec_())
