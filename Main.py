# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created: Fri Oct 02 13:25:35 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(830, 636)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Titol = QtGui.QLabel(self.centralwidget)
        self.Titol.setGeometry(QtCore.QRect(230, 40, 361, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.Titol.setFont(font)
        self.Titol.setIndent(-1)
        self.Titol.setObjectName(_fromUtf8("Titol"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 140, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(200, 200, 421, 291))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArxiu = QtGui.QMenu(self.menubar)
        self.menuArxiu.setObjectName(_fromUtf8("menuArxiu"))
        self.menuSobre_QtPhotoArxiver = QtGui.QMenu(self.menubar)
        self.menuSobre_QtPhotoArxiver.setObjectName(_fromUtf8("menuSobre_QtPhotoArxiver"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNova_Imatge = QtGui.QAction(MainWindow)
        self.actionNova_Imatge.setObjectName(_fromUtf8("actionNova_Imatge"))
        self.actionCerca_Imatge = QtGui.QAction(MainWindow)
        self.actionCerca_Imatge.setObjectName(_fromUtf8("actionCerca_Imatge"))
        self.actionQui_som = QtGui.QAction(MainWindow)
        self.actionQui_som.setObjectName(_fromUtf8("actionQui_som"))
        self.menuArxiu.addAction(self.actionNova_Imatge)
        self.menuArxiu.addAction(self.actionCerca_Imatge)
        self.menuSobre_QtPhotoArxiver.addAction(self.actionQui_som)
        self.menubar.addAction(self.menuArxiu.menuAction())
        self.menubar.addAction(self.menuSobre_QtPhotoArxiver.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Titol.setText(_translate("MainWindow", "Aula S.V.C.", None))
        self.label.setText(_translate("MainWindow", "Programa d\'Arxiu Fotogràfic", None))
        self.menuArxiu.setTitle(_translate("MainWindow", "Arxiu", None))
        self.menuSobre_QtPhotoArxiver.setTitle(_translate("MainWindow", "Mes...", None))
        self.actionNova_Imatge.setText(_translate("MainWindow", "Nova Imatge", None))
        self.actionCerca_Imatge.setText(_translate("MainWindow", "Cerca Imatge", None))
        self.actionQui_som.setText(_translate("MainWindow", "Guia d\'ús", None))

