# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QKeyEvent, QKeySequence
from PyQt5.QtWidgets import QTableWidgetItem, QListWidget, QStyledItemDelegate, QStyleOptionViewItem, QMessageBox,\
    QComboBox, QShortcut
from PyQt5.QtCore import QTimer
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import dados
import style
import threading
import sqlite3
import datetime

conn = sqlite3.connect('bd/cadastros.db')
c = conn.cursor()


data = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%d/%m/%Y - %H:%M:%S'))

conn = sqlite3.connect('bd/cadastros.db')
c = conn.cursor()




class Login(object):
    def setupUiLogin(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        Dialog.setAutoFillBackground(True)
        Dialog.setStyleSheet("")
        self.label_bg = QtWidgets.QLabel(Dialog)
        self.label_bg.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label_bg.setStyleSheet("background-color: rgb(64, 131, 203)")
        self.label_bg.setText("")
        self.label_bg.setObjectName("label_bg")
        self.label_2_bg = QtWidgets.QLabel(Dialog)
        self.label_2_bg.setGeometry(QtCore.QRect(240, 130, 341, 341))
        self.label_2_bg.setStyleSheet("background-color: white")
        self.label_2_bg.setText("")
        self.label_2_bg.setObjectName("label_2_bg")
        self.label_login = QtWidgets.QLabel(Dialog)
        self.label_login.setGeometry(QtCore.QRect(350, 100, 280, 150))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet("color: rgb(100, 101, 102)")
        self.label_login.setObjectName("label_err")

        self.label_err = QtWidgets.QLabel(Dialog)
        self.label_err.setGeometry(QtCore.QRect(340, 160, 280, 150))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_err.setFont(font)
        self.label_err.setStyleSheet("color: red")
        self.label_err.hide()
        self.label_err.setObjectName("label_err")

        self.textEdit_user = QtWidgets.QLineEdit(Dialog)
        self.textEdit_user.setGeometry(QtCore.QRect(280, 260, 271, 41))
        self.textEdit_user.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_user.setStyleSheet("background-color: rgb(233, 237, 238);\n"
"border: 2px solid rgb(233, 237, 238); padding: 1px; border-style: solid; border-radius: 8px")
        self.textEdit_user.setObjectName("textEdit_user")
        self.textEdit_passwd = QtWidgets.QLineEdit(Dialog)
        self.textEdit_passwd.setGeometry(QtCore.QRect(280, 310, 271, 41))
        self.textEdit_passwd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit_passwd.setStyleSheet("background-color: rgb(233, 237, 238);\n"
"border: 2px solid rgb(233, 237, 238); padding: 1px; border-style: solid; border-radius: 8px")
        self.textEdit_passwd.setObjectName("textEdit_passwd")
        self.pushButton_login = QtWidgets.QPushButton(Dialog)
        self.pushButton_login.setGeometry(QtCore.QRect(275, 360, 282, 56))
        self.pushButton_login.setStyleSheet(style.styleBtn)
        self.pushButton_login.setObjectName("pushButton_login")
        self.textEdit_user.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_passwd.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_passwd.setEchoMode(QtWidgets.QLineEdit.Password)



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Log In"))
        self.label_login.setText(_translate("Dialog", "Login"))
        self.label_err.setText(_translate("Dialog", "Credenciais inválidas!"))
        self.textEdit_user.setPlaceholderText(_translate("Dialog", "username"))
        self.textEdit_passwd.setPlaceholderText(_translate("Dialog", "password"))
        self.pushButton_login.setText(_translate("Dialog", "Log In"))



        self.pushButton_login.clicked.connect(self.login)


    def login(self):

        with sqlite3.connect("bd/cadastros.db") as con_l:
            c_l = con_l.cursor()
            users = []
            senhas = []
            busca = c_l.execute("SELECT * FROM usuarios")
            for row in busca:
                users.append(row[1])
                senhas.append(row[2])

            userCampo = self.textEdit_user.text()
            senhaCampo = self.textEdit_passwd.text()

            for i in range(len(users)):



                if (userCampo == users[i] and senhaCampo == senhas[i]):
                    print('Logado com sucesso!')
                    print('Login: ' + users[i] + '\nSenha: ' + senhas[i])
                    logado = True
                    print('View atual: main view')
                    l.hide()
                    l.close()
                    w.showMaximized()


                else:

                    print('Não logou com: ' + users[i] + ' e ' + senhas[i])
                    self.textEdit_passwd.clear()
                    self.textEdit_user.clear()
                    self.label_err.show()



class Ui_MainWindow(object):
    def setupUiMain(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#MainWindow { border-image: url(img/logo.jpg) 0 0 0 0 stretch stretch; }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 75, 191, 61))
        self.pushButton.setStyleSheet(style.styleBtn)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 75, 191, 61))
        self.pushButton_2.setStyleSheet(style.styleBtn)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(730, 75, 191, 61))
        self.pushButton_3.setStyleSheet(style.styleBtn)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(960, 75, 191, 61))
        self.pushButton_4.setStyleSheet(style.styleBtn)
        self.pushButton_4.setObjectName("pushButton_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuSobre = QtWidgets.QMenu(self.menubar)
        self.menuSobre.setObjectName("menuSobre")
        self.menuSobre_2 = QtWidgets.QMenu(self.menubar)
        self.menuSobre_2.setObjectName("menuSobre_2")
        self.menuSobre_3 = QtWidgets.QMenu(self.menubar)
        self.menuSobre_3.setObjectName("menuSobre_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRelatorio_Simples = QtWidgets.QAction(MainWindow)
        self.actionRelatorio_Simples.setObjectName("actionRelatorio_Simples")
        self.actionDetalhado = QtWidgets.QAction(MainWindow)
        self.actionDetalhado.setObjectName("actionDetalhado")
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionEditar_valores = QtWidgets.QAction(MainWindow)
        self.actionEditar_valores.setObjectName("actionEditar_valores")
        self.actionFeito_por = QtWidgets.QAction(MainWindow)
        self.actionFeito_por.setObjectName("actionFeito_por")
        self.menuSobre.addAction(self.actionRelatorio_Simples)
        self.menuSobre.addAction(self.actionDetalhado)
        self.menuSobre.addSeparator()
        self.menuSobre.addAction(self.actionSair)
        self.menuSobre_2.addAction(self.actionEditar_valores)
        self.menuSobre_3.addAction(self.actionFeito_por)
        self.menubar.addAction(self.menuSobre.menuAction())
        self.menubar.addAction(self.menuSobre_2.menuAction())
        self.menubar.addAction(self.menuSobre_3.menuAction())



        self.pushButton.clicked.connect(self.mostra_simples)
        self.pushButton_3.clicked.connect(self.mostra_param)
        self.pushButton_4.clicked.connect(self.mostra_email)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Evolution Vilatec - Controle "))
        self.pushButton.setText(_translate("MainWindow", "RELATÓRIO SIMPLES"))
        self.pushButton_2.setText(_translate("MainWindow", "RELATÓRIO DETALHADO"))
        self.pushButton_3.setText(_translate("MainWindow", "PARÂMETROS"))
        self.pushButton_4.setText(_translate("MainWindow", "LISTA DE EMAILS"))
        self.menuSobre.setTitle(_translate("MainWindow", "Relatórios"))
        self.menuSobre_2.setTitle(_translate("MainWindow", "Parâmetros"))
        self.menuSobre_3.setTitle(_translate("MainWindow", "Sobre"))
        self.actionRelatorio_Simples.setText(_translate("MainWindow", "Simples"))
        self.actionDetalhado.setText(_translate("MainWindow", "Detalhado"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionEditar_valores.setText(_translate("MainWindow", "Editar valores"))
        self.actionFeito_por.setText(_translate("MainWindow", "Feito por: Evolution Vilatec"))



    def mostra_simples(self):
        print('View atual: relatório simples')
        w.hide()
        w.close()
        s.showMaximized()



    def mostra_param(self):
        print('View atual: parâmetros')
        w.hide()
        w.close()
        p.showMaximized()


    def mostra_email(self):
        print('View atual: lista de emails')
        w.hide()
        w.close()
        e.showMaximized()




class Simples(object):
    def setupUiSim(self, Dialog):

        Dialog.setObjectName("Dialog")
        #Dialog.resize(800, 600)
        Dialog.setSizeGripEnabled(False)
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(640, 0, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.btn1 = QtWidgets.QPushButton(Dialog)
        self.btn1.setGeometry(QtCore.QRect(640, 60, 121, 31))
        self.btn1.setStyleSheet(style.styleBtn)
        self.btn1.setObjectName("btn1")
        self.cb = QtWidgets.QComboBox(Dialog)
        self.cb.setGeometry(QtCore.QRect(630, 30, 141, 22))
        self.cb.setObjectName("cb")
        self.cb.addItem("")
        self.cb.addItem("")
        self.cb.addItem("")
        self.cb.setItemText(2, "")
        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(630, 90, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(630, 120, 171, 22))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label3 = QtWidgets.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(950, 20, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.textEdit = QtWidgets.QLineEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(920, 50, 141, 25))
        self.textEdit.setObjectName("textEdit")
        self.btn2 = QtWidgets.QPushButton(Dialog)
        self.btn2.setGeometry(QtCore.QRect(930, 80, 121, 31))
        self.btn2.setStyleSheet(style.styleBtn)
        self.btn2.setObjectName("btn2")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(280, 160, 781, 821))
        stylesheet = "::section{Background-color:rgb(33, 152, 192);border-radius:14px;}"
        self.tableWidget.horizontalHeader().setStyleSheet(stylesheet)
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(15)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setFont(QtGui.QFont("Helvetica", 12, QtGui.QFont.Normal, italic=False))
        self.tableWidget.setStyleSheet("alternate-background-color: rgb(211,211,211);background-color: white;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(152)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(46)
        self.tableWidget.verticalHeader().setMinimumSectionSize(21)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)

        self.btn3 = QtWidgets.QPushButton(Dialog)
        self.btn3.setGeometry(QtCore.QRect(310, 20, 41, 32))
        self.btn3.setStyleSheet(style.styleBtn)
        self.btn3.setObjectName("btn3")
        self.btn3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/backing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn3.setIcon(icon)
        self.btn3.setObjectName("btn3")
        self.retranslateUiSim(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        #############  @SIGNALS  ##############

        self.btn1.clicked.connect(self.geraRelatorio)
        self.btn2.clicked.connect(self.buttonFunction)
        self.btn3.clicked.connect(self.voltar)




        #############  THREAD FUNCTION  ##############

    def buttonFunction(self):
        t = threading.Thread(target=self.EmailComDados)
        t.start()

        #############  BUTTON FUNCTIONS ##############

    def retranslateUiSim(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MCC - Relatório"))
        self.label1.setText(_translate("Dialog", "Selecione a data abaixo"))
        self.btn1.setText(_translate("Dialog", "Gerar"))
        self.cb.setItemText(0, _translate("Dialog", "GERAL"))
        self.label3.setText(_translate("Dialog", "Enviar por email"))
        self.textEdit.setPlaceholderText(_translate("Dialog", "Email"))
        self.btn2.setText(_translate("Dialog", "Enviar"))



    def EmailComDados(self):
        import email_template
        self.btn2.setDisabled(True)
        self.btn2.setText('Enviando...')
        dest = self.textEdit.text()
        print('Enviando email para {}'.format(dest))
        self.label3.setText('Enviando email...')

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "MCC - RELATÓRIO"
        msg['From'] = dest
        msg['To'] = dest
        part2 = MIMEText(email_template.html, 'html')
        msg.attach(part2)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login('<email>', '<password>')
            server.sendmail(dest, dest, msg.as_string())
            server.close()
            print('Email enviado!')
            self.label3.setText('Email enviado!')
            self.label3.setStyleSheet('color: green')
            self.btn2.setDisabled(False)
            self.btn2.setText('ENVIAR')
            time.sleep(5)
            self.label3.setText('Enviar novo email')
            self.label3.setStyleSheet('color: black')

        except:

            print('Falha no envio...')
            self.label3.setStyleSheet('color: red')
            self.label3.setText('Email inválido')
            self.btn2.setDisabled(False)
            self.btn2.setText('ENVIAR')
            time.sleep(5)
            self.label3.setText('Enviar email')
            self.label3.setStyleSheet('color: black')


    def voltar(self):
        s.hide()
        s.close()
        w.showMaximized()
        print('View atual: main page')


    def geraRelatorio(self):

        columns = ['Data', 'Hora', 'Pressão Máxima', 'Pressão Mínima', 'Pressão Média']
        self.tableWidget.setHorizontalHeaderLabels(columns)
        self.label2.setText('Relatório gerado sem erros')
        self.label2.setStyleSheet('color: green')
        self.label2.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.label2.setAlignment(QtCore.Qt.AlignCenter)






        for i in range(11):
            self.tableWidget.setRowCount(i)
            self.tableWidget.setItem((i-1), 0, QTableWidgetItem(dados.datas[i-1]))
            self.tableWidget.setItem((i-1), 1, QTableWidgetItem(dados.horas[i-1]))



            self.tableWidget.setItem(0, 2, QTableWidgetItem(dados.max1))
            self.tableWidget.setItem(0, 3, QTableWidgetItem(dados.min1))
            self.tableWidget.setItem(0, 4, QTableWidgetItem(dados.med1))

            newitem1 = QTableWidgetItem(dados.max2)
            newitem1.setBackground(QtGui.QColor(220, 0, 0))

            newitem2 = QTableWidgetItem(dados.min2)
            newitem2.setBackground(QtGui.QColor(220, 0, 0))

            newitem3 = QTableWidgetItem(dados.med2)
            newitem3.setBackground(QtGui.QColor(220, 0, 0))


            self.tableWidget.setItem(1, 2, QTableWidgetItem(newitem1))
            self.tableWidget.setItem(1, 3, QTableWidgetItem(newitem2))
            self.tableWidget.setItem(1, 4, QTableWidgetItem(newitem3))

            self.tableWidget.setItem(2, 2, QTableWidgetItem(dados.max3))
            self.tableWidget.setItem(2, 3, QTableWidgetItem(dados.min3))
            self.tableWidget.setItem(2, 4, QTableWidgetItem(dados.med3))

            self.tableWidget.setItem(3, 2, QTableWidgetItem(dados.max4))
            self.tableWidget.setItem(3, 3, QTableWidgetItem(dados.min4))
            self.tableWidget.setItem(3, 4, QTableWidgetItem(dados.med4))

            self.tableWidget.setItem(4, 2, QTableWidgetItem(dados.max5))
            self.tableWidget.setItem(4, 3, QTableWidgetItem(dados.min5))
            self.tableWidget.setItem(4, 4, QTableWidgetItem(dados.med5))

            self.tableWidget.setItem(5, 2, QTableWidgetItem(dados.max6))
            self.tableWidget.setItem(5, 3, QTableWidgetItem(dados.min6))
            self.tableWidget.setItem(5, 4, QTableWidgetItem(dados.med6))

            self.tableWidget.setItem(6, 2, QTableWidgetItem(dados.max7))
            self.tableWidget.setItem(6, 3, QTableWidgetItem(dados.min7))
            self.tableWidget.setItem(6, 4, QTableWidgetItem(dados.med7))

            self.tableWidget.setItem(7, 2, QTableWidgetItem(dados.max8))
            self.tableWidget.setItem(7, 3, QTableWidgetItem(dados.min8))
            self.tableWidget.setItem(7, 4, QTableWidgetItem(dados.med8))

            self.tableWidget.setItem(8, 2, QTableWidgetItem(dados.max9))
            self.tableWidget.setItem(8, 3, QTableWidgetItem(dados.min9))
            self.tableWidget.setItem(8, 4, QTableWidgetItem(dados.med9))

            self.tableWidget.setItem(9, 2, QTableWidgetItem(dados.max10))
            self.tableWidget.setItem(9, 3, QTableWidgetItem(dados.min10))
            self.tableWidget.setItem(9, 4, QTableWidgetItem(dados.med10))

            self.tableWidget.setItem(10, 2, QTableWidgetItem(dados.max11))
            self.tableWidget.setItem(10, 3, QTableWidgetItem(dados.min11))
            self.tableWidget.setItem(10, 4, QTableWidgetItem(dados.med11))

            self.tableWidget.setItem(11, 2, QTableWidgetItem(dados.max12))
            self.tableWidget.setItem(11, 3, QTableWidgetItem(dados.min12))
            self.tableWidget.setItem(11, 4, QTableWidgetItem(dados.med12))

            self.tableWidget.setItem(12, 2, QTableWidgetItem(dados.max13))
            self.tableWidget.setItem(12, 3, QTableWidgetItem(dados.min13))
            self.tableWidget.setItem(12, 4, QTableWidgetItem(dados.med13))



class Ui_Dialog_Param(object):


    def setupUiP(self, Dialog_Param):
        Dialog_Param.setObjectName("Dialog_Param")
        Dialog_Param.resize(800, 600)
        self.text_pressao_max = QtWidgets.QLineEdit(Dialog_Param)
        self.text_pressao_max.setGeometry(QtCore.QRect(370, 130, 104, 78))
        self.text_pressao_max.setObjectName("text_pressao_max")
        self.text_temp_max = QtWidgets.QLineEdit(Dialog_Param)
        self.text_temp_max.setGeometry(QtCore.QRect(510, 130, 104, 78))
        self.text_temp_max.setObjectName("text_temp_max")
        self.text_umi_max = QtWidgets.QLineEdit(Dialog_Param)
        self.text_umi_max.setGeometry(QtCore.QRect(650, 130, 104, 78))
        self.text_umi_max.setObjectName("text_umi_max")
        self.text_fluxo_max = QtWidgets.QLineEdit(Dialog_Param)
        self.text_fluxo_max.setGeometry(QtCore.QRect(790, 130, 104, 78))
        self.text_fluxo_max.setObjectName("text_fluxo_max")
        self.text_xxxxx_max = QtWidgets.QLineEdit(Dialog_Param)
        self.text_xxxxx_max.setGeometry(QtCore.QRect(930, 130, 104, 78))
        self.text_xxxxx_max.setObjectName("text_xxxxx_max")
        self.label_pressao_max = QtWidgets.QLabel(Dialog_Param)
        self.label_pressao_max.setGeometry(QtCore.QRect(395, 90, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_pressao_max.setFont(font)
        self.label_pressao_max.setObjectName("label_pressao_max")
        self.label_temp_max = QtWidgets.QLabel(Dialog_Param)
        self.label_temp_max.setGeometry(QtCore.QRect(515, 90, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_temp_max.setFont(font)
        self.label_temp_max.setObjectName("label_temp_max")
        self.label_umi_max = QtWidgets.QLabel(Dialog_Param)
        self.label_umi_max.setGeometry(QtCore.QRect(670, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_umi_max.setFont(font)
        self.label_umi_max.setObjectName("label_umi_max")
        self.label_fluxo_max = QtWidgets.QLabel(Dialog_Param)
        self.label_fluxo_max.setGeometry(QtCore.QRect(800, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_fluxo_max.setFont(font)
        self.label_fluxo_max.setObjectName("label_fluxo_max")
        self.label_xx_max = QtWidgets.QLabel(Dialog_Param)
        self.label_xx_max.setGeometry(QtCore.QRect(945, 90, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_xx_max.setFont(font)
        self.label_xx_max.setObjectName("label_xx_max")
        self.label_superior = QtWidgets.QLabel(Dialog_Param)
        self.label_superior.setEnabled(False)
        self.label_superior.setGeometry(QtCore.QRect(370, 20, 661, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_superior.setFont(font)
        self.label_superior.setObjectName("label_superior")
        self.pushButton = QtWidgets.QPushButton(Dialog_Param)
        self.pushButton.setGeometry(QtCore.QRect(370, 210, 106, 32))
        self.pushButton.setStyleSheet(style.styleBtn)
        self.pushButton.setObjectName("pushButton")
        self.label_pressao_max2 = QtWidgets.QLabel(Dialog_Param)
        self.label_pressao_max2.setGeometry(QtCore.QRect(405, 110, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_pressao_max2.setFont(font)
        self.label_pressao_max2.setObjectName("label_pressao_max2")
        self.label_temp_max2 = QtWidgets.QLabel(Dialog_Param)
        self.label_temp_max2.setGeometry(QtCore.QRect(545, 110, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_temp_max2.setFont(font)
        self.label_temp_max2.setObjectName("label_temp_max2")
        self.label_umi_max2 = QtWidgets.QLabel(Dialog_Param)
        self.label_umi_max2.setGeometry(QtCore.QRect(685, 110, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_umi_max2.setFont(font)
        self.label_umi_max2.setObjectName("label_umi_max2")
        self.label_fluxo_max2 = QtWidgets.QLabel(Dialog_Param)
        self.label_fluxo_max2.setGeometry(QtCore.QRect(825, 110, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_fluxo_max2.setFont(font)
        self.label_fluxo_max2.setObjectName("label_fluxo_max2")
        self.label_xx_max2 = QtWidgets.QLabel(Dialog_Param)
        self.label_xx_max2.setGeometry(QtCore.QRect(965, 110, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_xx_max2.setFont(font)
        self.label_xx_max2.setObjectName("label_xx_max2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog_Param)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 210, 106, 32))
        self.pushButton_2.setStyleSheet(style.styleBtn)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog_Param)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 210, 106, 32))
        self.pushButton_3.setStyleSheet(style.styleBtn)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog_Param)
        self.pushButton_4.setGeometry(QtCore.QRect(790, 210, 106, 32))
        self.pushButton_4.setStyleSheet(style.styleBtn)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog_Param)
        self.pushButton_5.setGeometry(QtCore.QRect(930, 210, 106, 32))
        self.pushButton_5.setStyleSheet(style.styleBtn)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog_Param)
        self.pushButton_6.setGeometry(QtCore.QRect(925, 550, 106, 32))
        self.pushButton_6.setStyleSheet(style.styleBtn)
        self.pushButton_6.setObjectName("pushButton_6")
        self.text_fluxo_min = QtWidgets.QLineEdit(Dialog_Param)
        self.text_fluxo_min.setGeometry(QtCore.QRect(785, 470, 104, 78))
        self.text_fluxo_min.setObjectName("text_fluxo_min")
        self.label_xx_min = QtWidgets.QLabel(Dialog_Param)
        self.label_xx_min.setGeometry(QtCore.QRect(940, 430, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_xx_min.setFont(font)
        self.label_xx_min.setObjectName("label_xx_min")
        self.label_temp_min2 = QtWidgets.QLabel(Dialog_Param)
        self.label_temp_min2.setGeometry(QtCore.QRect(540, 450, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_temp_min2.setFont(font)
        self.label_temp_min2.setObjectName("label_temp_min2")
        self.label_umi_min2 = QtWidgets.QLabel(Dialog_Param)
        self.label_umi_min2.setGeometry(QtCore.QRect(680, 450, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_umi_min2.setFont(font)
        self.label_umi_min2.setObjectName("label_umi_min2")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog_Param)
        self.pushButton_7.setGeometry(QtCore.QRect(365, 550, 106, 32))
        self.pushButton_7.setStyleSheet(style.styleBtn)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog_Param)
        self.pushButton_8.setGeometry(QtCore.QRect(785, 550, 106, 32))
        self.pushButton_8.setStyleSheet(style.styleBtn)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_fluxo_min = QtWidgets.QLabel(Dialog_Param)
        self.label_fluxo_min.setGeometry(QtCore.QRect(795, 430, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_fluxo_min.setFont(font)
        self.label_fluxo_min.setObjectName("label_fluxo_min")
        self.label_pressao_min = QtWidgets.QLabel(Dialog_Param)
        self.label_pressao_min.setGeometry(QtCore.QRect(390, 430, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_pressao_min.setFont(font)
        self.label_pressao_min.setObjectName("label_pressao_min")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog_Param)
        self.pushButton_9.setGeometry(QtCore.QRect(645, 550, 106, 32))
        self.pushButton_9.setStyleSheet(style.styleBtn)
        self.pushButton_9.setObjectName("pushButton_9")
        self.text_pressao_min = QtWidgets.QLineEdit(Dialog_Param)
        self.text_pressao_min.setGeometry(QtCore.QRect(365, 470, 104, 78))
        self.text_pressao_min.setObjectName("text_pressao_min")
        self.label_pressao_min2 = QtWidgets.QLabel(Dialog_Param)
        self.label_pressao_min2.setGeometry(QtCore.QRect(400, 450, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_pressao_min2.setFont(font)
        self.label_pressao_min2.setObjectName("label_pressao_min2")
        self.text_umi_min = QtWidgets.QLineEdit(Dialog_Param)
        self.text_umi_min.setGeometry(QtCore.QRect(645, 470, 104, 78))
        self.text_umi_min.setObjectName("text_umi_min")
        self.text_xxxxx_min = QtWidgets.QLineEdit(Dialog_Param)
        self.text_xxxxx_min.setGeometry(QtCore.QRect(925, 470, 104, 78))
        self.text_xxxxx_min.setObjectName("text_xxxxx_min")
        self.label_umi_min = QtWidgets.QLabel(Dialog_Param)
        self.label_umi_min.setGeometry(QtCore.QRect(665, 430, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_umi_min.setFont(font)
        self.label_umi_min.setObjectName("label_umi_min")
        self.label_temp_min = QtWidgets.QLabel(Dialog_Param)
        self.label_temp_min.setGeometry(QtCore.QRect(510, 430, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_temp_min.setFont(font)
        self.label_temp_min.setObjectName("label_temp_min")
        self.pushButton_10 = QtWidgets.QPushButton(Dialog_Param)
        self.pushButton_10.setGeometry(QtCore.QRect(505, 550, 106, 32))
        self.pushButton_10.setStyleSheet(style.styleBtn)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_xx_min_2 = QtWidgets.QLabel(Dialog_Param)
        self.label_xx_min_2.setGeometry(QtCore.QRect(960, 450, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_xx_min_2.setFont(font)
        self.label_xx_min_2.setObjectName("label_xx_min_2")
        self.text_temp_min = QtWidgets.QLineEdit(Dialog_Param)
        self.text_temp_min.setGeometry(QtCore.QRect(505, 470, 104, 78))
        self.text_temp_min.setObjectName("text_temp_min")
        self.label_fluxo_min2 = QtWidgets.QLabel(Dialog_Param)
        self.label_fluxo_min2.setGeometry(QtCore.QRect(820, 450, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_fluxo_min2.setFont(font)
        self.label_fluxo_min2.setObjectName("label_fluxo_min2")
        self.btn_voltar = QtWidgets.QPushButton(Dialog_Param)
        self.btn_voltar.setGeometry(QtCore.QRect(310, 20, 41, 32))
        self.btn_voltar.setStyleSheet(style.styleBtn)
        self.btn_voltar.setObjectName("btn_voltar")
        self.label_alt_1 = QtWidgets.QLabel(Dialog_Param)
        self.label_alt_1.setEnabled(True)
        self.label_alt_1.setGeometry(QtCore.QRect(375, 320, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_alt_1.setFont(font)
        self.label_alt_1.setText("")
        self.label_alt_1.setObjectName("label_alt_1")
        self.label_alt_2 = QtWidgets.QLabel(Dialog_Param)
        self.label_alt_2.setGeometry(QtCore.QRect(515, 320, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_alt_2.setFont(font)
        self.label_alt_2.setText("")
        self.label_alt_2.setObjectName("label_alt_2")
        self.label_alt_4 = QtWidgets.QLabel(Dialog_Param)
        self.label_alt_4.setGeometry(QtCore.QRect(795, 320, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_alt_4.setFont(font)
        self.label_alt_4.setText("")
        self.label_alt_4.setObjectName("label_alt_4")
        self.label_alt_3 = QtWidgets.QLabel(Dialog_Param)
        self.label_alt_3.setGeometry(QtCore.QRect(655, 320, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_alt_3.setFont(font)
        self.label_alt_3.setText("")
        self.label_alt_3.setObjectName("label_alt_3")
        self.label_alt_5 = QtWidgets.QLabel(Dialog_Param)
        self.label_alt_5.setGeometry(QtCore.QRect(940, 320, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_alt_5.setFont(font)
        self.label_alt_5.setText("")
        self.label_alt_5.setObjectName("label_alt_5")
        self.label_alt_6 = QtWidgets.QLabel(Dialog_Param)
        self.label_alt_6.setGeometry(QtCore.QRect(370, 590, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_alt_6.setFont(font)
        self.label_alt_6.setText("")
        self.label_alt_6.setObjectName("label_alt_6")
        self.label_alt_7 = QtWidgets.QLabel(Dialog_Param)
        self.label_alt_7.setGeometry(QtCore.QRect(510, 590, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_alt_7.setFont(font)
        self.label_alt_7.setText("")
        self.label_alt_7.setObjectName("label_alt_7")
        self.label_alt_8 = QtWidgets.QLabel(Dialog_Param)
        self.label_alt_8.setGeometry(QtCore.QRect(650, 590, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_alt_8.setFont(font)
        self.label_alt_8.setText("")
        self.label_alt_8.setObjectName("label_alt_8")
        self.label_alt_9 = QtWidgets.QLabel(Dialog_Param)
        self.label_alt_9.setGeometry(QtCore.QRect(790, 590, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_alt_9.setFont(font)
        self.label_alt_9.setText("")
        self.label_alt_9.setObjectName("label_alt_9")
        self.label_alt_10 = QtWidgets.QLabel(Dialog_Param)
        self.label_alt_10.setGeometry(QtCore.QRect(935, 590, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_alt_10.setFont(font)
        self.label_alt_10.setText("")
        self.label_alt_10.setObjectName("label_alt_10")




        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)


        self.text_pressao_max.setFont(font)
        self.text_pressao_min.setFont(font)
        self.text_temp_max.setFont(font)
        self.text_temp_min.setFont(font)
        self.text_umi_max.setFont(font)
        self.text_umi_min.setFont(font)
        self.text_fluxo_max.setFont(font)
        self.text_fluxo_min.setFont(font)
        self.text_xxxxx_max.setFont(font)
        self.text_xxxxx_min.setFont(font)

        busca_p = c.execute("SELECT * FROM parametros")
        for row in busca_p:
            pressMax = str(row[0])
            pressMin = str(row[1])
            tempMax = str(row[2])
            tempMin = str(row[3])
            umiMax = str(row[4])
            umiMin = str(row[5])
            fluxoMax = str(row[6])
            fluxoMin = str(row[7])
            nullMax = str(row[8])
            nullMin = str(row[9])



        self.text_pressao_max.setText(pressMax)
        self.text_pressao_max.setText(pressMax)
        self.text_pressao_min.setText(pressMin)
        self.text_temp_max.setText(tempMax)
        self.text_temp_min.setText(tempMin)
        self.text_umi_max.setText(umiMax)
        self.text_umi_min.setText(umiMin)
        self.text_fluxo_max.setText(fluxoMax)
        self.text_fluxo_min.setText(fluxoMin)
        self.text_xxxxx_max.setText(nullMax)
        self.text_xxxxx_min.setText(nullMin)

        self.text_pressao_max.setAlignment(QtCore.Qt.AlignHCenter)
        self.text_pressao_min.setAlignment(QtCore.Qt.AlignHCenter)
        self.text_temp_max.setAlignment(QtCore.Qt.AlignHCenter)
        self.text_temp_min.setAlignment(QtCore.Qt.AlignHCenter)
        self.text_umi_max.setAlignment(QtCore.Qt.AlignHCenter)
        self.text_umi_min.setAlignment(QtCore.Qt.AlignHCenter)
        self.text_fluxo_max.setAlignment(QtCore.Qt.AlignHCenter)
        self.text_fluxo_min.setAlignment(QtCore.Qt.AlignHCenter)
        self.text_xxxxx_max.setAlignment(QtCore.Qt.AlignHCenter)
        self.text_fluxo_min.setAlignment(QtCore.Qt.AlignHCenter)
        self.text_xxxxx_max.setAlignment(QtCore.Qt.AlignHCenter)
        self.text_xxxxx_min.setAlignment(QtCore.Qt.AlignHCenter)

        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.label_cp = QtWidgets.QLabel(Dialog_Param)
        self.label_cp.setGeometry(QtCore.QRect(387, 250, 71, 16))
        self.label_cp.setFont(font)
        self.label_cp.setObjectName("label_cp")

        self.label_ep = QtWidgets.QLabel(Dialog_Param)
        self.label_ep.setGeometry(QtCore.QRect(437, 250, 71, 16))
        self.label_ep.setFont(font)
        self.label_ep.setObjectName("label_ep")



        self.checkBoxPC = QtWidgets.QCheckBox(Dialog_Param)
        self.checkBoxPC.setGeometry(QtCore.QRect(375, 265, 50, 50))
        self.checkBoxPC.setStyleSheet(style.styleCheckGreen)
        self.checkBoxPC.setText("")
        self.checkBoxPC.setObjectName("checkBoxPAZ")
        self.checkBoxPE = QtWidgets.QCheckBox(Dialog_Param)
        self.checkBoxPE.setGeometry(QtCore.QRect(435, 265, 50, 50))
        self.checkBoxPE.setStyleSheet(style.styleCheckGreen)
        self.checkBoxPE.setText("")
        self.checkBoxPE.setObjectName("checkBoxPVE")

        self.label_ct = QtWidgets.QLabel(Dialog_Param)
        self.label_ct.setGeometry(QtCore.QRect(525, 250, 71, 16))
        self.label_ct.setFont(font)
        self.label_ct.setObjectName("label_ct")

        self.label_et = QtWidgets.QLabel(Dialog_Param)
        self.label_et.setGeometry(QtCore.QRect(575, 250, 71, 16))
        self.label_et.setFont(font)
        self.label_et.setObjectName("label_et")


        self.checkBoxTC = QtWidgets.QCheckBox(Dialog_Param)
        self.checkBoxTC.setGeometry(QtCore.QRect(515, 265, 50, 50))
        self.checkBoxTC.setStyleSheet(style.styleCheckGreen)
        self.checkBoxTC.setText("")
        self.checkBoxTC.setObjectName("checkBoxTAZ")
        self.checkBoxTE = QtWidgets.QCheckBox(Dialog_Param)
        self.checkBoxTE.setGeometry(QtCore.QRect(575, 265, 50, 50))
        self.checkBoxTE.setStyleSheet(style.styleCheckGreen)
        self.checkBoxTC.setText("")
        self.checkBoxTE.setObjectName("checkBoxTVE")


        self.checkBoxUAZ = QtWidgets.QCheckBox(Dialog_Param)
        self.checkBoxUAZ.setGeometry(QtCore.QRect(695, 250, 50, 50))
        self.checkBoxUAZ.setStyleSheet(style.styleCheckBlue)
        self.checkBoxUAZ.setText("")
        self.checkBoxUAZ.setObjectName("checkBoxUAZ")
        self.checkBoxUVE = QtWidgets.QCheckBox(Dialog_Param)
        self.checkBoxUVE.setGeometry(QtCore.QRect(725, 250, 50, 50))
        self.checkBoxUVE.setStyleSheet(style.styleCheckGreen)
        self.checkBoxUVE.setText("")
        self.checkBoxUVE.setObjectName("checkBoxUVE")



        busca_em_c = c.execute("SELECT * FROM emailsClientes")
        for row in busca_em_c:
            status_press_max = row[4]

        if (status_press_max == 1):
            self.checkBoxPC.setChecked(True)

        busca_em_e = c.execute("SELECT * FROM emailsEvo")
        for row in busca_em_e:
            status_press_max = row[4]

        if (status_press_max == 1):
            self.checkBoxPE.setChecked(True)



        self.retranslateUi(Dialog_Param)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Param)

    def retranslateUi(self, Dialog_Param):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Param.setWindowTitle(_translate("Dialog_Param", "Dialog"))
        self.label_pressao_max.setText(_translate("Dialog_Param", "Pressão"))
        self.label_temp_max.setText(_translate("Dialog_Param", "Temperatura"))
        self.label_umi_max.setText(_translate("Dialog_Param", "Umidade"))
        self.label_fluxo_max.setText(_translate("Dialog_Param", "Fluxo de ar"))
        self.label_xx_max.setText(_translate("Dialog_Param", "XXXXXXX"))
        self.label_superior.setText(_translate("Dialog_Param", "Para alterar os parâmetros, basta escolher o valor desejado e clicar no botão MODIFICAR"))
        self.pushButton.setText(_translate("Dialog_Param", "MODIFICAR"))
        self.label_pressao_max2.setText(_translate("Dialog_Param", "MÁX"))
        self.label_temp_max2.setText(_translate("Dialog_Param", "MÁX"))
        self.label_umi_max2.setText(_translate("Dialog_Param", "MÁX"))
        self.label_fluxo_max2.setText(_translate("Dialog_Param", "MÁX"))
        self.label_xx_max2.setText(_translate("Dialog_Param", "MÁX"))
        self.pushButton_2.setText(_translate("Dialog_Param", "MODIFICAR"))
        self.pushButton_3.setText(_translate("Dialog_Param", "MODIFICAR"))
        self.pushButton_4.setText(_translate("Dialog_Param", "MODIFICAR"))
        self.pushButton_5.setText(_translate("Dialog_Param", "MODIFICAR"))
        self.pushButton_6.setText(_translate("Dialog_Param", "MODIFICAR"))
        self.label_xx_min.setText(_translate("Dialog_Param", "XXXXXXX"))
        self.label_temp_min2.setText(_translate("Dialog_Param", "MÍN"))
        self.label_umi_min2.setText(_translate("Dialog_Param", "MÍN"))
        self.pushButton_7.setText(_translate("Dialog_Param", "MODIFICAR"))
        self.pushButton_8.setText(_translate("Dialog_Param", "MODIFICAR"))
        self.label_fluxo_min.setText(_translate("Dialog_Param", "Fluxo de ar"))
        self.label_pressao_min.setText(_translate("Dialog_Param", "Pressão"))
        self.pushButton_9.setText(_translate("Dialog_Param", "MODIFICAR"))
        self.label_pressao_min2.setText(_translate("Dialog_Param", "MÍN"))
        self.label_umi_min.setText(_translate("Dialog_Param", "Umidade"))
        self.label_temp_min.setText(_translate("Dialog_Param", "Temperatura"))
        self.pushButton_10.setText(_translate("Dialog_Param", "MODIFICAR"))
        self.label_xx_min_2.setText(_translate("Dialog_Param", "MÍN"))
        self.label_fluxo_min2.setText(_translate("Dialog_Param", "MÍN"))
        self.btn_voltar.setText(_translate("Dialog_Param", ""))

        self.pushButton_5.setStyleSheet(style.styleBtnDisabled)
        self.pushButton_6.setStyleSheet(style.styleBtnDisabled)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/backing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_voltar.setIcon(icon)
        self.label_cp.setText(_translate("Dialog_Param", "C"))
        self.label_ep.setText(_translate("Dialog_Param", "EVO"))
        self.label_ct.setText(_translate("Dialog_Param", "C"))
        self.label_et.setText(_translate("Dialog_Param", "EVO"))



        self.pushButton.clicked.connect(self.td_btn1)
        self.pushButton_7.clicked.connect(self.td_btn2)
        self.pushButton_2.clicked.connect(self.td_btn3)
        self.pushButton_10.clicked.connect(self.td_btn4)
        self.pushButton_3.clicked.connect(self.td_btn5)
        self.pushButton_9.clicked.connect(self.td_btn6)
        self.pushButton_4.clicked.connect(self.td_btn7)
        self.pushButton_8.clicked.connect(self.td_btn8)
        self.btn_voltar.clicked.connect(self.voltar_p)



    def voltar_p(self):
        p.hide()
        p.close()
        w.showMaximized()
        print('View atual: main page')


    def td_btn1(self):
        t1 = threading.Thread(target=self.mod_press_max)
        t1.start()

    def mod_press_max(self):
        pressMax = int(self.text_pressao_max.text())
        with sqlite3.connect("bd/cadastros.db") as con_p:
            c_p = con_p.cursor()
            c_p.execute("UPDATE parametros SET pressaoMax = (?)", (pressMax,))
            con_p.commit()

            if (self.checkBoxPC.isChecked()):
                enviar_pressao_max = 1
            else:
                enviar_pressao_max = 0
            c_p.execute("UPDATE emailsClientes SET pressaoMax = ?", (enviar_pressao_max,))
            con_p.commit()

            if (self.checkBoxPE.isChecked()):
                enviar_pressao_max = 1
            else:
                enviar_pressao_max = 0
            c_p.execute("UPDATE emailsEvo SET pressaoMax = ?", (enviar_pressao_max,))
            con_p.commit()

        self.label_alt_1.setStyleSheet('color: green')
        self.label_alt_1.setText('Valor alterado!')
        self.pushButton.setDisabled(True)
        self.pushButton.setStyleSheet(style.styleBtnDisabled)
        time.sleep(4)
        self.pushButton.setStyleSheet(style.styleBtn)
        self.pushButton.setDisabled(False)
        self.label_alt_1.setText('')



    def td_btn2(self):
        t2 = threading.Thread(target=self.mod_press_min)
        t2.start()

    def mod_press_min(self):
        pressMin = int(self.text_pressao_min.text())
        with sqlite3.connect("bd/cadastros.db") as con_p:
            c_p = con_p.cursor()
            c_p.execute("UPDATE parametros SET pressaoMin = (?)", (pressMin,))
            con_p.commit()

        self.label_alt_6.setStyleSheet('color: green')
        self.label_alt_6.setText('Valor alterado!')
        self.pushButton_7.setDisabled(True)
        self.pushButton_7.setStyleSheet(style.styleBtnDisabled)
        time.sleep(4)
        self.pushButton_7.setStyleSheet(style.styleBtn)
        self.pushButton_7.setDisabled(False)
        self.label_alt_6.setText('')


    def td_btn3(self):
        t3 = threading.Thread(target=self.mod_temp_max)
        t3.start()

    def mod_temp_max(self):
        tempMax = int(self.text_temp_max.text())
        with sqlite3.connect("bd/cadastros.db") as con_p:
            c_p = con_p.cursor()
            c_p.execute("UPDATE parametros SET tempMax = (?)", (tempMax,))
            con_p.commit()

        self.label_alt_2.setStyleSheet('color: green')
        self.label_alt_2.setText('Valor alterado!')
        self.pushButton_2.setDisabled(True)
        self.pushButton_2.setStyleSheet(style.styleBtnDisabled)
        time.sleep(4)
        self.pushButton_2.setStyleSheet(
            style.styleBtn)
        self.pushButton_2.setDisabled(False)
        self.label_alt_2.setText('')



    def td_btn4(self):
        t4 = threading.Thread(target=self.mod_temp_min)
        t4.start()

    def mod_temp_min(self):
        tempMin = int(self.text_temp_min.text())
        with sqlite3.connect("bd/cadastros.db") as con_p:
            c_p = con_p.cursor()
            c_p.execute("UPDATE parametros SET tempMin = (?)", (tempMin,))
            con_p.commit()

        self.label_alt_7.setStyleSheet('color: green')
        self.label_alt_7.setText('Valor alterado!')
        self.pushButton_10.setDisabled(True)
        self.pushButton_10.setStyleSheet(
            style.styleBtnDisabled)
        time.sleep(4)
        self.pushButton_10.setStyleSheet(
            style.styleBtn)
        self.pushButton_10.setDisabled(False)
        self.label_alt_7.setText('')


    def td_btn5(self):
        t5 = threading.Thread(target=self.mod_umi_max)
        t5.start()

    def mod_umi_max(self):
        umiMax = int(self.text_umi_max.text())
        with sqlite3.connect("bd/cadastros.db") as con_p:
            c_p = con_p.cursor()
            c_p.execute("UPDATE parametros SET umidadeMax = (?)", (umiMax,))
            con_p.commit()

        self.label_alt_3.setStyleSheet('color: green')
        self.label_alt_3.setText('Valor alterado!')
        self.pushButton_3.setDisabled(True)
        self.pushButton_3.setStyleSheet(
            style.styleBtnDisabled)
        time.sleep(4)
        self.pushButton_3.setStyleSheet(
            style.styleBtn)
        self.pushButton_3.setDisabled(False)
        self.label_alt_3.setText('')

    def td_btn6(self):
        t6 = threading.Thread(target=self.mod_umi_min)
        t6.start()

    def mod_umi_min(self):
        umiMin = int(self.text_umi_min.text())
        with sqlite3.connect("bd/cadastros.db") as con_p:
            c_p = con_p.cursor()
            c_p.execute("UPDATE parametros SET umidadeMin = (?)", (umiMin,))
            con_p.commit()

        self.label_alt_8.setStyleSheet('color: green')
        self.label_alt_8.setText('Valor alterado!')
        self.pushButton_9.setDisabled(True)
        self.pushButton_9.setStyleSheet(
            style.styleBtnDisabled)
        time.sleep(4)
        self.pushButton_9.setStyleSheet(
            style.styleBtn)
        self.pushButton_9.setDisabled(False)
        self.label_alt_8.setText('')




    def td_btn7(self):
        t7 = threading.Thread(target=self.mod_fluxo_max)
        t7.start()

    def mod_fluxo_max(self):
        fluxoMax = int(self.text_fluxo_max.text())
        with sqlite3.connect("bd/cadastros.db") as con_p:
            c_p = con_p.cursor()
            c_p.execute("UPDATE parametros SET fluxoMax = (?)", (fluxoMax,))
            con_p.commit()

        self.label_alt_4.setStyleSheet('color: green')
        self.label_alt_4.setText('Valor alterado!')
        self.pushButton_4.setDisabled(True)
        self.pushButton_4.setStyleSheet(
            style.styleBtnDisabled)
        time.sleep(4)
        self.pushButton_4.setStyleSheet(
            style.styleBtn)
        self.pushButton_4.setDisabled(False)
        self.label_alt_4.setText('')



    def td_btn8(self):
        t8 = threading.Thread(target=self.mod_fluxo_min)
        t8.start()

    def mod_fluxo_min(self):
        fluxoMin = int(self.text_fluxo_min.text())
        with sqlite3.connect("bd/cadastros.db") as con_p:
            c_p = con_p.cursor()
            c_p.execute("UPDATE parametros SET fluxoMin = (?)", (fluxoMin,))
            con_p.commit()

        self.label_alt_9.setStyleSheet('color: green')
        self.label_alt_9.setText('Valor alterado!')
        self.pushButton_8.setDisabled(True)
        self.pushButton_8.setStyleSheet(style.styleBtnDisabled)
        time.sleep(4)
        self.pushButton_8.setStyleSheet(style.styleBtn)
        self.pushButton_8.setDisabled(False)
        self.label_alt_9.setText('')




               ########## LISTA EMAIL GUI ##########


class ListaEmail(object):
    def setupUiEmail(self, Dialog):
        Dialog.setObjectName("Dialog")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(310, 30, 370, 561))
        self.listWidget.setProperty("isWrapping", True)
        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setSpacing(5)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setStyleSheet("alternate-background-color: 	rgb(220,220,220);")

        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(720, 30, 370, 281))
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
        self.label_email_e = QtWidgets.QLabel(self.groupBox)
        self.label_email_e.setGeometry(QtCore.QRect(10, 120, 41, 16))
        self.label_email_e.setObjectName("label_email_e")

        self.label_cliente_e = QtWidgets.QLabel(self.groupBox)
        self.label_cliente_e.setGeometry(QtCore.QRect(10, 150, 71, 16))
        self.label_cliente_e.setObjectName("label_cliente_e")

        self.label_rela_e = QtWidgets.QLabel(self.groupBox)
        self.label_rela_e.setGeometry(QtCore.QRect(10, 180, 71, 16))
        self.label_rela_e.setObjectName("label_rela_e")

        self.label_data_e = QtWidgets.QLabel(self.groupBox)
        self.label_data_e.setGeometry(QtCore.QRect(10, 210, 171, 16))
        self.label_data_e.setObjectName("label_data_e")

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

        self.txt_rest_e = QtWidgets.QLabel(self.groupBox)
        self.txt_rest_e.setGeometry(QtCore.QRect(80, 150, 281, 16))
        self.txt_rest_e.setFont(font)
        self.txt_rest_e.setText("")
        self.txt_rest_e.setObjectName("txt_rest_e")

        self.txt_rela_e = QtWidgets.QLabel(self.groupBox)
        self.txt_rela_e.setGeometry(QtCore.QRect(80, 180, 281, 16))
        self.txt_rela_e.setFont(font)
        self.txt_rela_e.setText("")
        self.txt_rela_e.setObjectName("txt_rela_e")

        self.txt_data_e = QtWidgets.QLabel(self.groupBox)
        self.txt_data_e.setGeometry(QtCore.QRect(110, 210, 281, 16))
        self.txt_data_e.setFont(font)
        self.txt_data_e.setText("")
        self.txt_data_e.setObjectName("txt_data_e")

        self.btn_add_e = QtWidgets.QPushButton(Dialog)
        self.btn_add_e.setGeometry(QtCore.QRect(685, 30, 31, 31))
        self.btn_add_e.setStyleSheet(style.styleBtn)
        self.btn_add_e.setObjectName("btn_add_e")
        self.btn_remove_e = QtWidgets.QPushButton(Dialog)
        self.btn_remove_e.setGeometry(QtCore.QRect(685, 70, 31, 31))
        self.btn_remove_e.setStyleSheet(style.styleBtn)
        self.btn_remove_e.setObjectName("btn_remove_e")
        self.btn_edit_e = QtWidgets.QPushButton(Dialog)
        self.btn_edit_e.setGeometry(QtCore.QRect(685, 110, 31, 31))
        self.btn_edit_e.setStyleSheet("font: 15pt Arial; background-image: 'img/edit.png';margin: 1px; border-color: #0c457e; border-style: outset; border-radius: 3px;border-width: 1px;color: white;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);}QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);")
        self.btn_edit_e.setObjectName("btn_edit_e")

        self.btn_search_e = QtWidgets.QPushButton(Dialog)
        self.btn_search_e.setGeometry(QtCore.QRect(685, 150, 31, 31))
        try:
            self.btn_search_e.setStyleSheet("font: 15pt Arial; background-image: 'img/edit.png';margin: 1px; border-color: #0c457e; border-style: outset; border-radius: 3px;border-width: 1px;color: white;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6);}QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);")

        except:
            print('falha style search')

        self.btn_search_e.setObjectName("btn_search_e")

        self.btn_voltar_e = QtWidgets.QPushButton(Dialog)
        self.btn_voltar_e.setGeometry(QtCore.QRect(230, 20, 41, 32))
        self.btn_voltar_e.setStyleSheet(style.styleBtn)
        self.btn_voltar_e.setObjectName("btn_edit_e")

        self.btn_voltar_e = QtWidgets.QPushButton(Dialog)
        self.btn_voltar_e.setGeometry(QtCore.QRect(230, 20, 41, 32))
        self.btn_voltar_e.setStyleSheet(style.styleBtn)
        self.btn_voltar_e.setObjectName("btn_voltar_e")






        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_edit_e.setIcon(icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_e.setIcon(icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_remove_e.setIcon(icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/backing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_voltar_e.setIcon(icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/s4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_search_e.setIcon(icon)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.btn_voltar_e.clicked.connect(self.voltar_e)
        self.btn_add_e.clicked.connect(self.mostra_add_email)
        self.btn_edit_e.clicked.connect(self.print)
        self.listWidget.itemClicked.connect(self.idx0)
        self.btn_remove_e.clicked.connect(self.del_user)
        self.btn_edit_e.clicked.connect(self.mostra_edt_email)
        self.btn_search_e.clicked.connect(self.mostra_srch_email)



        iconA = QtGui.QIcon()
        iconA.addPixmap(QtGui.QPixmap("img/green_glow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        iconB = QtGui.QIcon()
        iconB.addPixmap(QtGui.QPixmap("img/red_glow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        iconC = QtGui.QIcon()
        iconC.addPixmap(QtGui.QPixmap("img/blue_glow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        iconD = QtGui.QIcon()
        iconD.addPixmap(QtGui.QPixmap("img/yellow_glow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        busca = c.execute("SELECT * FROM dados")
        for row in busca:
            itm = QtWidgets.QListWidgetItem(row[1])

            if (row[5] == 1):                      # VERIFICA SE É CLIENTE
                itm.setIcon(iconA)
                self.listWidget.addItem(itm)

            else:
                itm.setIcon(iconC)
                self.listWidget.addItem(itm)




    def del_user(self):
        model = self.listWidget.model()
        for selectedItem in self.listWidget.selectedItems():
            qIndex = self.listWidget.indexFromItem(selectedItem)
            nome = model.data(qIndex)


            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)

            msg.setText("Tem certeza que quer remover <b>" + nome + "</b>?")
            msg.setWindowTitle("Removendo usuário")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            buttonY = msg.button(QMessageBox.Yes)
            buttonY.setText('Sim')
            buttonN = msg.button(QMessageBox.No)
            buttonN.setText('Não')

            msg.exec_()

            if msg.clickedButton() == buttonY:
                print('removido: %s' % model.data(qIndex))

                nm = str(model.data(qIndex))
                idx = self.listWidget.currentRow()




                ####### REMOVE USER #######
                with sqlite3.connect("bd/cadastros.db") as con_p:
                    c_p = con_p.cursor()
                    c_p.execute("DELETE FROM dados WHERE nome = (?)", (model.data(qIndex),))
                    con_p.commit()
                    c_p.execute("DELETE FROM emailsClientes WHERE nome = (?)", (model.data(qIndex),))
                    con_p.commit()
                    c_p.execute("DELETE FROM emailsEvo WHERE nome = (?)", (model.data(qIndex),))
                    con_p.commit()
                    model.removeRow(qIndex.row())








    def idx0(self, item):


        global idx
        idx = str(item.text())
        print('Clicou em: ' + idx)

        ls = []
        matricula = []
        cargo = []
        email = []
        cliente = []
        rela = []
        data = []

        busca_qtd = c.execute("SELECT * FROM dados")

        for row in busca_qtd:
            matricula.append(str(row[0]))    # ROW[0] = ID AUTO INCREMENT
            cargo.append(row[3])
            email.append(row[4])
            data.append(row[7])

            if row[5] == 1:
                clienteR = 'SIM'
            else:
                clienteR = 'NÃO'

            if row[6] == 1:
                relaR = 'SIM'
            else:
                relaR = 'NÃO'

            cliente.append(clienteR)
            rela.append(relaR)


        for i in range(100):

            busca = c.execute("SELECT nome FROM dados WHERE ID = (?)", (i + 1,))
            for row in busca:
                ls.append(row[0])



        try:

            if (idx == ls[0]):
                self.txt_nome_e.setText(ls[0])
                self.txt_matricula_e.setText(matricula[0])
                self.txt_cargo_e.setText(cargo[0])
                self.txt_email_e.setText(email[0])
                self.txt_rest_e.setText(cliente[0])
                self.txt_rela_e.setText(rela[0])
                self.txt_data_e.setText(data[0])

            if (idx == ls[1]):
                self.txt_nome_e.setText(ls[1])
                self.txt_matricula_e.setText(matricula[1])
                self.txt_cargo_e.setText(cargo[1])
                self.txt_email_e.setText(email[1])
                self.txt_rest_e.setText(cliente[1])
                self.txt_rela_e.setText(rela[1])
                self.txt_data_e.setText(data[1])

            if (idx == ls[2]):
                self.txt_nome_e.setText(ls[2])
                self.txt_matricula_e.setText(matricula[2])
                self.txt_cargo_e.setText(cargo[2])
                self.txt_email_e.setText(email[2])
                self.txt_rest_e.setText(cliente[2])
                self.txt_rela_e.setText(rela[2])
                self.txt_data_e.setText(data[2])

            if (idx == ls[3]):
                self.txt_nome_e.setText(ls[3])
                self.txt_matricula_e.setText(matricula[3])
                self.txt_cargo_e.setText(cargo[3])
                self.txt_email_e.setText(email[3])
                self.txt_rest_e.setText(cliente[3])
                self.txt_rela_e.setText(rela[3])
                self.txt_data_e.setText(data[3])

            if (idx == ls[4]):
                self.txt_nome_e.setText(ls[4])
                self.txt_matricula_e.setText(matricula[4])
                self.txt_cargo_e.setText(cargo[4])
                self.txt_email_e.setText(email[4])
                self.txt_rest_e.setText(cliente[4])
                self.txt_rela_e.setText(rela[4])
                self.txt_data_e.setText(data[4])

            if (idx == ls[5]):
                self.txt_nome_e.setText(ls[5])
                self.txt_matricula_e.setText(matricula[5])
                self.txt_cargo_e.setText(cargo[5])
                self.txt_email_e.setText(email[5])
                self.txt_rest_e.setText(cliente[5])
                self.txt_rela_e.setText(rela[5])
                self.txt_data_e.setText(data[5])

            if (idx == ls[6]):
                self.txt_nome_e.setText(ls[6])
                self.txt_matricula_e.setText(matricula[6])
                self.txt_cargo_e.setText(cargo[6])
                self.txt_email_e.setText(email[6])
                self.txt_rest_e.setText(cliente[6])
                self.txt_rela_e.setText(rela[6])
                self.txt_data_e.setText(data[6])

            if (idx == ls[7]):
                self.txt_nome_e.setText(ls[7])
                self.txt_matricula_e.setText(matricula[7])
                self.txt_cargo_e.setText(cargo[7])
                self.txt_email_e.setText(email[7])
                self.txt_rest_e.setText(cliente[7])
                self.txt_rela_e.setText(rela[7])
                self.txt_data_e.setText(data[7])

        except:
            pass





    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lista de email"))
        self.groupBox.setTitle(_translate("Dialog", "Informações do usuário"))
        self.label_nome_e.setText(_translate("Dialog", "Nome:"))
        self.label_matricula_e.setText(_translate("Dialog", "Matricula:"))
        self.label_cargo_e.setText(_translate("Dialog", "Cargo:"))
        self.label_email_e.setText(_translate("Dialog", "Email: "))
        self.label_cliente_e.setText(_translate("Dialog", "Cliente: "))
        self.label_rela_e.setText(_translate("Dialog", "Relatório: "))
        self.label_data_e.setText(_translate("Dialog", "Adicionado em: "))
        self.btn_add_e.setText(_translate("Dialog", ""))
        self.btn_remove_e.setText(_translate("Dialog", ""))
        self.btn_edit_e.setText(_translate("Dialog", ""))
        self.btn_search_e.setText(_translate("Dialog", ""))
        self.btn_voltar_e.setText(_translate("Dialog", ""))

        #
        # self.i = 0
        # self.qTimer = QTimer()
        # self.qTimer.setInterval(1000)
        # self.qTimer.timeout.connect(self.showList)
        # self.qTimer.start()

    def print(self):
        print(self.listWidget.currentRow())

    def esc_voltar_e(self):
        e.hide()
        e.close()
        w.showMaximized()
        print('View atual: main page')

    def voltar_e(self):
        e.hide()
        e.close()
        w.showMaximized()
        print('View atual: main page')

    def mostra_add_email(self):
        a.show()
        print('View atual: add email')


    def mostra_srch_email(self):
        t.show()
        print('View atual: srch email')


    def mostra_edt_email(self):
        f.show()
        print('View atual: edt email')


class AddEmail(object):
    def setupUiAddEmail(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 350)
        self.nome_add_e = QtWidgets.QLabel(Dialog)
        self.nome_add_e.setGeometry(QtCore.QRect(10, 30, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.nome_add_e.setFont(font)
        self.nome_add_e.setObjectName("nome_add_e")
        self.matricula_add_e = QtWidgets.QLabel(Dialog)
        self.matricula_add_e.setGeometry(QtCore.QRect(10, 80, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.matricula_add_e.setFont(font)
        self.matricula_add_e.setObjectName("matricula_add_e")
        self.cargo_add_e = QtWidgets.QLabel(Dialog)
        self.cargo_add_e.setGeometry(QtCore.QRect(10, 130, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cargo_add_e.setFont(font)
        self.cargo_add_e.setObjectName("cargo_add_e")
        self.email_add_e = QtWidgets.QLabel(Dialog)
        self.email_add_e.setGeometry(QtCore.QRect(10, 182, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.email_add_e.setFont(font)
        self.email_add_e.setObjectName("email_add_e")

        self.txt_label_add = QtWidgets.QLabel(Dialog)
        self.txt_label_add.setGeometry(QtCore.QRect(150, 10, 191, 16))
        self.txt_label_add.setObjectName("txt_label_add")
        self.txt_label_add.setStyleSheet('color: green')
        self.txt_label_add.setText('Usuário adicionado!')
        self.txt_label_add.hide()

        self.txt_nome_add = QtWidgets.QLineEdit(Dialog)
        self.txt_nome_add.setGeometry(QtCore.QRect(110, 30, 261, 21))
        self.txt_nome_add.setObjectName("txt_nome_add")
        self.txt_matricula_add = QtWidgets.QLineEdit(Dialog)
        self.txt_matricula_add.setGeometry(QtCore.QRect(110, 80, 261, 21))
        self.txt_matricula_add.setObjectName("txt_matricula_add")
        self.txt_cargo_add = QtWidgets.QLineEdit(Dialog)
        self.txt_cargo_add.setGeometry(QtCore.QRect(110, 130, 261, 21))
        self.txt_cargo_add.setObjectName("txt_cargo_add")
        self.txt_email_add = QtWidgets.QLineEdit(Dialog)
        self.txt_email_add.setGeometry(QtCore.QRect(110, 180, 261, 21))
        self.txt_email_add.setObjectName("txt_email_add")
        self.btn_add_add_e = QtWidgets.QPushButton(Dialog)
        self.btn_add_add_e.setGeometry(QtCore.QRect(120, 300, 161, 41))
        self.btn_add_add_e.setStyleSheet(style.styleBtn)
        self.btn_add_add_e.setObjectName("btn_add_add_e")
        self.restrito_add_e = QtWidgets.QLabel(Dialog)
        self.restrito_add_e.setGeometry(QtCore.QRect(10, 230, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.restrito_add_e.setFont(font)
        self.restrito_add_e.setObjectName("restrito_add_e")
        self.relatorio_e = QtWidgets.QLabel(Dialog)
        self.relatorio_e.setGeometry(QtCore.QRect(10, 270, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.relatorio_e.setFont(font)
        self.relatorio_e.setObjectName("relatorio_e")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(110, 230, 87, 20))
        self.checkBox.setObjectName("checkBox")

        self.checkBoxRela = QtWidgets.QCheckBox(Dialog)
        self.checkBoxRela.setGeometry(QtCore.QRect(110, 270, 87, 20))
        self.checkBoxRela.setObjectName("checkBoxRela")

        sqls = c.execute("SELECT * FROM dados")
        for row in sqls:
            matri = str(row[0] + 1)
        self.txt_matricula_add.setText(matri)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btn_add_add_e.clicked.connect(self.clica_adicionar)





    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Adicionar novo usuário"))
        self.nome_add_e.setText(_translate("Dialog", "Nome:"))
        self.matricula_add_e.setText(_translate("Dialog", "Matricula: "))
        self.cargo_add_e.setText(_translate("Dialog", "Cargo:"))
        self.email_add_e.setText(_translate("Dialog", "Email:"))
        self.btn_add_add_e.setText(_translate("Dialog", "Adicionar"))
        self.restrito_add_e.setText(_translate("Dialog", "Cliente:"))
        self.relatorio_e.setText(_translate("Dialog", "Relatório:"))
        self.checkBox.setText(_translate("Dialog", "Sim"))
        self.checkBoxRela.setText(_translate("Dialog", "Sim"))



    def voltar_add_e(self):
        a.hide()
        a.close()
        e.showMaximized()
        print('View atual: lista de emails')


    def td_btn8(self):
        t8 = threading.Thread(target=self.clica_adicionar)
        t8.start()


    def clica_adicionar(self):


        if (self.txt_nome_add.text() == ''):
            self.txt_label_add.setStyleSheet('color: red')
            self.txt_label_add.setText('Campo NOME em branco')


        elif (self.txt_cargo_add.text() == ''):
            self.txt_label_add.setStyleSheet('color: red')
            self.txt_label_add.setText('Campo CARGO em branco')


        elif (self.txt_email_add.text() == ''):
            self.txt_label_add.setStyleSheet('color: red')
            self.txt_label_add.setText('Campo EMAIL em branco')



        else:

            nome = self.txt_nome_add.text()
            matricula = self.txt_matricula_add.text()
            cargo = self.txt_cargo_add.text()
            email = self.txt_email_add.text()
            if self.checkBox.isChecked():
                cliente = 1
                c.execute("INSERT INTO emailsClientes (nome, email, data) VALUES (?, ?, ?)", (nome, email, data))
            else:
                cliente = 0
                c.execute("INSERT INTO emailsEvo (nome, email, data) VALUES (?, ?, ?)", (nome, email, data))

            if self.checkBoxRela.isChecked():
                rela = 1
            else:
                rela = 0




            c.execute("INSERT INTO dados (nome, matricula, cargo, email, cliente, relatorio, data) VALUES "
                      "(?, ?, ?, ?, ?, ?, ?)",
                      (nome, matricula, cargo, email, cliente, rela, data))

            conn.commit()

            busca = c.execute("SELECT * FROM dados")
            for row in busca:
                print(row)



        self.txt_label_add.setStyleSheet('color: green')
        self.txt_label_add.setText('Usuário adicionado!')
        self.txt_label_add.show()

        self.txt_nome_add.clear()
        self.txt_matricula_add.clear()
        self.txt_cargo_add.clear()
        self.txt_email_add.clear()




class SearchUser(object):
    def setupUiSearchUser(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 350)
        self.nome_add_e = QtWidgets.QLabel(Dialog)
        self.nome_add_e.setGeometry(QtCore.QRect(10, 30, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.nome_add_e.setFont(font)
        self.nome_add_e.setObjectName("nome_add_e")
        self.matricula_add_e = QtWidgets.QLabel(Dialog)
        self.matricula_add_e.setGeometry(QtCore.QRect(10, 80, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.matricula_add_e.setFont(font)
        self.matricula_add_e.setObjectName("matricula_add_e")
        self.cargo_add_e = QtWidgets.QLabel(Dialog)
        self.cargo_add_e.setGeometry(QtCore.QRect(10, 130, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cargo_add_e.setFont(font)
        self.cargo_add_e.setObjectName("cargo_add_e")
        self.email_add_e = QtWidgets.QLabel(Dialog)
        self.email_add_e.setGeometry(QtCore.QRect(10, 182, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.email_add_e.setFont(font)
        self.email_add_e.setObjectName("email_add_e")

        self.txt_label_add = QtWidgets.QLabel(Dialog)
        self.txt_label_add.setGeometry(QtCore.QRect(120, 10, 191, 16))
        self.txt_label_add.setObjectName("txt_label_add")
        self.txt_label_add.setText('Digite o usuário abaixo')

        self.cb = QtWidgets.QLineEdit(Dialog)
        self.cb.setGeometry(QtCore.QRect(120, 30, 150, 30))
        self.cb.setObjectName("cb")


        self.txt_nome_add = QtWidgets.QLineEdit(Dialog)
        self.txt_nome_add.setGeometry(QtCore.QRect(110, 30, 261, 21))
        self.txt_nome_add.setObjectName("txt_nome_add")
        self.txt_matricula_add = QtWidgets.QLineEdit(Dialog)
        self.txt_matricula_add.setGeometry(QtCore.QRect(110, 80, 261, 21))
        self.txt_matricula_add.setObjectName("txt_matricula_add")
        self.txt_cargo_add = QtWidgets.QLineEdit(Dialog)
        self.txt_cargo_add.setGeometry(QtCore.QRect(110, 130, 261, 21))
        self.txt_cargo_add.setObjectName("txt_cargo_add")
        self.txt_email_add = QtWidgets.QLineEdit(Dialog)
        self.txt_email_add.setGeometry(QtCore.QRect(110, 180, 261, 21))
        self.txt_email_add.setObjectName("txt_email_add")
        self.btn_add_add_e = QtWidgets.QPushButton(Dialog)
        self.btn_add_add_e.setGeometry(QtCore.QRect(120, 300, 161, 41))
        self.btn_add_add_e.setStyleSheet(style.styleBtn)
        self.btn_add_add_e.setObjectName("btn_add_add_e")
        self.btn_add_add_e.hide()

        self.btn_bsc_e = QtWidgets.QPushButton(Dialog)
        self.btn_bsc_e.setGeometry(QtCore.QRect(130, 75, 120, 40))
        self.btn_bsc_e.setStyleSheet(style.styleBtn)
        self.btn_bsc_e.setObjectName("btn_bsc_e")
        self.btn_bsc_e.setText('Buscar')

        self.restrito_add_e = QtWidgets.QLabel(Dialog)
        self.restrito_add_e.setGeometry(QtCore.QRect(10, 230, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.restrito_add_e.setFont(font)
        self.restrito_add_e.setObjectName("restrito_add_e")
        self.relatorio_e = QtWidgets.QLabel(Dialog)
        self.relatorio_e.setGeometry(QtCore.QRect(10, 270, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.relatorio_e.setFont(font)
        self.relatorio_e.setObjectName("relatorio_e")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(110, 230, 87, 20))
        self.checkBox.setObjectName("checkBox")

        self.checkBoxRela = QtWidgets.QCheckBox(Dialog)
        self.checkBoxRela.setGeometry(QtCore.QRect(110, 270, 87, 20))
        self.checkBoxRela.setObjectName("checkBoxRela")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btn_bsc_e.clicked.connect(self.digita_user)
        self.btn_add_add_e.clicked.connect(self.update_user)


        self.txt_nome_add.hide()
        self.txt_email_add.hide()
        self.txt_cargo_add.hide()
        self.txt_matricula_add.hide()
        self.checkBoxRela.hide()
        self.checkBox.hide()
        self.nome_add_e.hide()
        self.matricula_add_e.hide()
        self.cargo_add_e.hide()
        self.email_add_e.hide()
        self.restrito_add_e.hide()
        self.relatorio_e.hide()



    def digita_user(self):

        rowQtd = []
        global nomeBusca
        global nomeBd
        nomeBusca = self.cb.text()

        with sqlite3.connect("bd/cadastros.db") as con_p:
            c_p = con_p.cursor()

            busca_qtd = c_p.execute("SELECT * FROM dados WHERE nome LIKE (?)", ('%' + nomeBusca + '%',))

            for row in busca_qtd:
                rowQtd.append(row)


            if (len(rowQtd) > 1):
                self.txt_label_add.setStyleSheet('color: red')
                self.txt_label_add.setText('Erro! Dois usuários iguais')

            elif (len(rowQtd) < 1):
                self.txt_label_add.setStyleSheet('color: red')
                self.txt_label_add.setText('Nenhum usuário encontrado')
            else:

                self.txt_nome_add.show()
                self.txt_email_add.show()
                self.txt_cargo_add.show()
                self.txt_matricula_add.show()
                self.checkBoxRela.show()
                self.checkBox.show()
                self.nome_add_e.show()
                self.matricula_add_e.show()
                self.cargo_add_e.show()
                self.email_add_e.show()
                self.restrito_add_e.show()
                self.relatorio_e.show()
                self.btn_bsc_e.hide()
                self.txt_label_add.hide()
                self.cb.hide()
                self.btn_add_add_e.show()

                self.txt_label_add.setGeometry(QtCore.QRect(170, 10, 191, 16))


                nomeBd = row[1]
                matricula = str(row[0])  # ROW[0] = ID AUTO INCREMENT
                cargo = row[3]
                email = row[4]
                data = row[7]

                if row[5] == 1:
                    self.checkBox.setChecked(True)
                else:
                    self.checkBox.setChecked(False)

                if row[6] == 1:
                    self.checkBoxRela.setChecked(True)
                else:
                    self.checkBoxRela.setChecked(False)

                self.txt_nome_add.setText(nomeBd)
                self.txt_matricula_add.setText(matricula)
                self.txt_cargo_add.setText(cargo)
                self.txt_email_add.setText(email)


    def update_user(self):

        novoNome = self.txt_nome_add.text()
        novaMatricula = self.txt_matricula_add.text()
        novoCargo = self.txt_cargo_add.text()
        novoEmail = self.txt_email_add.text()

        if self.checkBox.isChecked():
            novoCliente = 1


        else:
            novoCliente = 0

        if self.checkBoxRela.isChecked():
            novoRelatorio = 1

        else:
            novoRelatorio = 0

        with sqlite3.connect("bd/cadastros.db") as con_ps:
            c_ps = con_ps.cursor()
            c_ps.execute("UPDATE dados SET nome = ?, matricula = ?, cargo = ?, email = ?, cliente = ?, relatorio = ?"
          " WHERE nome = ?", (novoNome, novaMatricula, novoCargo, novoEmail, novoCliente, novoRelatorio, nomeBd))
            con_ps.commit()

        self.txt_label_add.show()
        self.txt_label_add.setText('Usuário editado!')
        self.txt_label_add.setStyleSheet('color: green')
        print('atualizado: %s', novoNome)








    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Editar usuário"))
        self.nome_add_e.setText(_translate("Dialog", "Nome:"))
        self.matricula_add_e.setText(_translate("Dialog", "Matricula: "))
        self.cargo_add_e.setText(_translate("Dialog", "Cargo:"))
        self.email_add_e.setText(_translate("Dialog", "Email:"))
        self.btn_add_add_e.setText(_translate("Dialog", "Editar"))
        self.restrito_add_e.setText(_translate("Dialog", "Cliente:"))
        self.relatorio_e.setText(_translate("Dialog", "Relatório:"))
        self.checkBox.setText(_translate("Dialog", "Sim"))
        self.checkBoxRela.setText(_translate("Dialog", "Sim"))




class EditUser(object):
    def setupUiEditUser(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 350)
        self.nome_add_e = QtWidgets.QLabel(Dialog)
        self.nome_add_e.setGeometry(QtCore.QRect(10, 30, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.nome_add_e.setFont(font)
        self.nome_add_e.setObjectName("nome_add_e")
        self.matricula_add_e = QtWidgets.QLabel(Dialog)
        self.matricula_add_e.setGeometry(QtCore.QRect(10, 80, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.matricula_add_e.setFont(font)
        self.matricula_add_e.setObjectName("matricula_add_e")
        self.cargo_add_e = QtWidgets.QLabel(Dialog)
        self.cargo_add_e.setGeometry(QtCore.QRect(10, 130, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cargo_add_e.setFont(font)
        self.cargo_add_e.setObjectName("cargo_add_e")
        self.email_add_e = QtWidgets.QLabel(Dialog)
        self.email_add_e.setGeometry(QtCore.QRect(10, 182, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.email_add_e.setFont(font)
        self.email_add_e.setObjectName("email_add_e")

        self.txt_label_add = QtWidgets.QLabel(Dialog)
        self.txt_label_add.setGeometry(QtCore.QRect(150, 10, 191, 16))
        self.txt_label_add.setObjectName("txt_label_add")
        self.txt_label_add.setStyleSheet('color: green')
        self.txt_label_add.setText('Usuário editado!')
        self.txt_label_add.hide()

        self.txt_nome_add = QtWidgets.QLineEdit(Dialog)
        self.txt_nome_add.setGeometry(QtCore.QRect(110, 30, 261, 21))
        self.txt_nome_add.setObjectName("txt_nome_add")
        self.txt_matricula_add = QtWidgets.QLineEdit(Dialog)
        self.txt_matricula_add.setGeometry(QtCore.QRect(110, 80, 261, 21))
        self.txt_matricula_add.setObjectName("txt_matricula_add")
        self.txt_cargo_add = QtWidgets.QLineEdit(Dialog)
        self.txt_cargo_add.setGeometry(QtCore.QRect(110, 130, 261, 21))
        self.txt_cargo_add.setObjectName("txt_cargo_add")
        self.txt_email_add = QtWidgets.QLineEdit(Dialog)
        self.txt_email_add.setGeometry(QtCore.QRect(110, 180, 261, 21))
        self.txt_email_add.setObjectName("txt_email_add")
        self.btn_add_add_e = QtWidgets.QPushButton(Dialog)
        self.btn_add_add_e.setGeometry(QtCore.QRect(120, 300, 161, 41))
        self.btn_add_add_e.setStyleSheet(style.styleBtn)
        self.btn_add_add_e.setObjectName("btn_add_add_e")

        self.btn_mostrar = QtWidgets.QPushButton(Dialog)
        self.btn_mostrar.setGeometry(QtCore.QRect(120, 100, 161, 60))
        self.btn_mostrar.setStyleSheet(style.styleBtn)
        self.btn_mostrar.setObjectName("btn_mostrar")

        self.restrito_add_e = QtWidgets.QLabel(Dialog)
        self.restrito_add_e.setGeometry(QtCore.QRect(10, 230, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.restrito_add_e.setFont(font)
        self.restrito_add_e.setObjectName("restrito_add_e")
        self.relatorio_e = QtWidgets.QLabel(Dialog)
        self.relatorio_e.setGeometry(QtCore.QRect(10, 270, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.relatorio_e.setFont(font)
        self.relatorio_e.setObjectName("relatorio_e")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(110, 230, 87, 20))
        self.checkBox.setObjectName("checkBox")

        self.checkBoxRela = QtWidgets.QCheckBox(Dialog)
        self.checkBoxRela.setGeometry(QtCore.QRect(110, 270, 87, 20))
        self.checkBoxRela.setObjectName("checkBoxRela")

        sqls = c.execute("SELECT * FROM dados")
        for row in sqls:
            matri = str(row[0] + 1)
        self.txt_matricula_add.setText(matri)



        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        try:
            self.txt_matricula_add.setText(idx)
        except:
            pass



        self.btn_add_add_e.hide()
        self.txt_nome_add.hide()
        self.txt_matricula_add.hide()
        self.txt_label_add.hide()
        self.txt_email_add.hide()
        self.txt_cargo_add.hide()
        self.matricula_add_e.hide()
        self.nome_add_e.hide()
        self.cargo_add_e.hide()
        self.email_add_e.hide()
        self.checkBoxRela.hide()
        self.checkBox.hide()
        self.relatorio_e.hide()
        self.restrito_add_e.hide()




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Editando Usuário"))
        self.nome_add_e.setText(_translate("Dialog", "Nome:"))
        self.matricula_add_e.setText(_translate("Dialog", "Matricula: "))
        self.cargo_add_e.setText(_translate("Dialog", "Cargo:"))
        self.email_add_e.setText(_translate("Dialog", "Email:"))
        self.btn_add_add_e.setText(_translate("Dialog", "Editar"))
        self.restrito_add_e.setText(_translate("Dialog", "Cliente:"))
        self.relatorio_e.setText(_translate("Dialog", "Relatório:"))
        self.checkBox.setText(_translate("Dialog", "Sim"))
        self.checkBoxRela.setText(_translate("Dialog", "Sim"))
        self.btn_mostrar.setText(_translate("Dialog", "EDITAR"))

        self.btn_mostrar.clicked.connect(self.botao_mostrar)
        self.btn_add_add_e.clicked.connect(self.botao_editar)




    def botao_editar(self):

        novoNome = self.txt_nome_add.text()
        novaMatricula = self.txt_matricula_add.text()
        novoCargo = self.txt_cargo_add.text()
        novoEmail = self.txt_email_add.text()

        if self.checkBox.isChecked():
            novoCliente = 1


        else:
            novoCliente = 0

        if self.checkBoxRela.isChecked():
            novoRelatorio = 1

        else:
            novoRelatorio = 0

        with sqlite3.connect("bd/cadastros.db") as con_ps:
            c_ps = con_ps.cursor()
            c_ps.execute("UPDATE dados SET nome = ?, matricula = ?, cargo = ?, email = ?, cliente = ?, relatorio = ?"
                         " WHERE nome = ?",
                         (novoNome, novaMatricula, novoCargo, novoEmail, novoCliente, novoRelatorio, idx))
            con_ps.commit()

        self.txt_label_add.show()
        self.txt_label_add.setText('Usuário editado!')
        self.txt_label_add.setStyleSheet('color: green')
        print('atualizado: %s', novoNome)


    def botao_mostrar(self):
        try:
            idx
            self.txt_label_add.setStyleSheet('color: green')
            self.txt_label_add.setText('Usuário editado!')
            self.txt_label_add.hide()

            sql = c.execute("SELECT * FROM dados WHERE nome = (?)", (idx,))
            for row in sql:
                print(row)
                self.btn_mostrar.hide()
                self.btn_add_add_e.show()
                self.txt_nome_add.show()
                self.txt_matricula_add.show()
                self.txt_email_add.show()
                self.txt_cargo_add.show()
                self.matricula_add_e.show()
                self.nome_add_e.show()
                self.cargo_add_e.show()
                self.email_add_e.show()
                self.checkBoxRela.show()
                self.checkBox.show()
                self.relatorio_e.show()
                self.restrito_add_e.show()

                self.txt_nome_add.setText(row[1])
                self.txt_matricula_add.setText(str(row[0]))
                self.txt_cargo_add.setText(row[3])
                self.txt_email_add.setText(row[4])

                if row[5] == 1:
                    self.checkBox.setChecked(True)

                if row[6] == 1:
                    self.checkBoxRela.setChecked(True)



        except NameError:
            print('idx não definido')
            self.txt_label_add.setStyleSheet('color: red')
            self.txt_label_add.setText('Nenhum usuário selecionado')
            self.txt_label_add.show()






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    l = QtWidgets.QDialog()
    ui_login = Login()
    ui_login.setupUiLogin(l)

    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiMain(w)

    s = QtWidgets.QDialog()
    ui_simples = Simples()
    ui_simples.setupUiSim(s)

    p = QtWidgets.QDialog()
    ui_param = Ui_Dialog_Param()
    ui_param.setupUiP(p)

    e = QtWidgets.QDialog()
    ui_email = ListaEmail()
    ui_email.setupUiEmail(e)

    a = QtWidgets.QDialog()
    ui_add = AddEmail()
    ui_add.setupUiAddEmail(a)

    t = QtWidgets.QDialog()
    ui_srch = SearchUser()
    ui_srch.setupUiSearchUser(t)

    f = QtWidgets.QDialog()
    ui_edt = EditUser()
    ui_edt.setupUiEditUser(f)



    l.show()
    sys.exit(app.exec_())
