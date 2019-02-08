# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lista_email.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ListaEmail(object):
    def setupUiEmail(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(10, 30, 370, 561))
        self.listView.setAlternatingRowColors(True)
        self.listView.setProperty("isWrapping", False)
        self.listView.setGridSize(QtCore.QSize(2, 5))
        self.listView.setUniformItemSizes(True)
        self.listView.setObjectName("listView")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(420, 30, 370, 281))
        self.groupBox.setObjectName("groupBox")
        self.label_nome_e = QtWidgets.QLabel(self.groupBox)
        self.label_nome_e.setGeometry(QtCore.QRect(10, 30, 41, 16))
        self.label_nome_e.setObjectName("label_nome_e")
        self.label_matricula_e = QtWidgets.QLabel(self.groupBox)
        self.label_matricula_e.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_matricula_e.setObjectName("label_matricula_e")
        self.label_cargo_e = QtWidgets.QLabel(self.groupBox)
        self.label_cargo_e.setGeometry(QtCore.QRect(10, 90, 41, 16))
        self.label_cargo_e.setObjectName("label_cargo_e")
        self.label_cargo_e_2 = QtWidgets.QLabel(self.groupBox)
        self.label_cargo_e_2.setGeometry(QtCore.QRect(10, 120, 41, 16))
        self.label_cargo_e_2.setObjectName("label_cargo_e_2")
        self.txt_nome_e = QtWidgets.QLabel(self.groupBox)
        self.txt_nome_e.setGeometry(QtCore.QRect(80, 30, 281, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.txt_nome_e.setFont(font)
        self.txt_nome_e.setText("")
        self.txt_nome_e.setObjectName("txt_nome_e")
        self.txt_matricula_e = QtWidgets.QLabel(self.groupBox)
        self.txt_matricula_e.setGeometry(QtCore.QRect(80, 60, 281, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.txt_matricula_e.setFont(font)
        self.txt_matricula_e.setText("")
        self.txt_matricula_e.setObjectName("txt_matricula_e")
        self.txt_cargo_e = QtWidgets.QLabel(self.groupBox)
        self.txt_cargo_e.setGeometry(QtCore.QRect(80, 90, 281, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.txt_cargo_e.setFont(font)
        self.txt_cargo_e.setText("")
        self.txt_cargo_e.setObjectName("txt_cargo_e")
        self.txt_email_e = QtWidgets.QLabel(self.groupBox)
        self.txt_email_e.setGeometry(QtCore.QRect(80, 120, 281, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.txt_email_e.setFont(font)
        self.txt_email_e.setText("")
        self.txt_email_e.setObjectName("txt_email_e")
        self.btn_add_e = QtWidgets.QPushButton(Dialog)
        self.btn_add_e.setGeometry(QtCore.QRect(385, 30, 31, 31))
        self.btn_add_e.setStyleSheet("font: 15pt Arial;margin: 1px; border-color: #0c457e; border-style: outset; border-radius: 3px;border-width: 1px;color: white;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);}QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);")
        self.btn_add_e.setObjectName("btn_add_e")
        self.btn_remove_e = QtWidgets.QPushButton(Dialog)
        self.btn_remove_e.setGeometry(QtCore.QRect(385, 70, 31, 31))
        self.btn_remove_e.setStyleSheet("font: 15pt Arial;margin: 1px; border-color: #0c457e; border-style: outset; border-radius: 3px;border-width: 1px;color: white;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);}QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);")
        self.btn_remove_e.setObjectName("btn_remove_e")
        self.btn_edit_e = QtWidgets.QPushButton(Dialog)
        self.btn_edit_e.setGeometry(QtCore.QRect(385, 110, 31, 31))
        self.btn_edit_e.setStyleSheet("font: 15pt Arial;margin: 1px; border-color: #0c457e; border-style: outset; border-radius: 3px;border-width: 1px;color: white;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);}QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);")
        self.btn_edit_e.setObjectName("btn_edit_e")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lista de email"))
        self.groupBox.setTitle(_translate("Dialog", "Informações do usuário"))
        self.label_nome_e.setText(_translate("Dialog", "Nome:"))
        self.label_matricula_e.setText(_translate("Dialog", "Matricula:"))
        self.label_cargo_e.setText(_translate("Dialog", "Cargo:"))
        self.label_cargo_e_2.setText(_translate("Dialog", "Email: "))
        self.btn_add_e.setText(_translate("Dialog", "+"))
        self.btn_remove_e.setText(_translate("Dialog", "-"))
        self.btn_edit_e.setText(_translate("Dialog", "E"))







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ListaEmail()
    ui.setupUiEmail(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

