# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addDialog.ui'
#
# Created: Mon Sep 21 10:35:22 2015
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(794, 412)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(420, 370, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(410, 10, 171, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(340, 20, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboAlbums = QtGui.QComboBox(Dialog)
        self.comboAlbums.setGeometry(QtCore.QRect(410, 40, 171, 27))
        self.comboAlbums.setObjectName(_fromUtf8("comboAlbums"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(330, 50, 66, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(320, 130, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.listMetadataP = QtGui.QListWidget(Dialog)
        self.listMetadataP.setGeometry(QtCore.QRect(330, 200, 121, 161))
        self.listMetadataP.setObjectName(_fromUtf8("listMetadataP"))
        self.delMetadataBtn = QtGui.QPushButton(Dialog)
        self.delMetadataBtn.setGeometry(QtCore.QRect(640, 130, 51, 27))
        self.delMetadataBtn.setObjectName(_fromUtf8("delMetadataBtn"))
        self.addMetaDataBtn = QtGui.QPushButton(Dialog)
        self.addMetaDataBtn.setGeometry(QtCore.QRect(580, 130, 61, 27))
        self.addMetaDataBtn.setObjectName(_fromUtf8("addMetaDataBtn"))
        self.Data = QtGui.QDateEdit(Dialog)
        self.Data.setGeometry(QtCore.QRect(410, 80, 110, 27))
        self.Data.setObjectName(_fromUtf8("Data"))
        self.lineEditMetadata = QtGui.QLineEdit(Dialog)
        self.lineEditMetadata.setGeometry(QtCore.QRect(410, 130, 171, 27))
        self.lineEditMetadata.setObjectName(_fromUtf8("lineEditMetadata"))
        self.addAlbumBtn = QtGui.QPushButton(Dialog)
        self.addAlbumBtn.setGeometry(QtCore.QRect(590, 40, 98, 27))
        self.addAlbumBtn.setObjectName(_fromUtf8("addAlbumBtn"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(340, 90, 66, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.graphicsView = QtGui.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 301, 271))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.uploadFileBtn = QtGui.QPushButton(Dialog)
        self.uploadFileBtn.setGeometry(QtCore.QRect(210, 290, 98, 27))
        self.uploadFileBtn.setObjectName(_fromUtf8("uploadFileBtn"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 300, 66, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.radioPersonaBtn = QtGui.QRadioButton(Dialog)
        self.radioPersonaBtn.setGeometry(QtCore.QRect(330, 170, 116, 22))
        self.radioPersonaBtn.setChecked(True)
        self.radioPersonaBtn.setObjectName(_fromUtf8("radioPersonaBtn"))
        self.radioLlocsBtn = QtGui.QRadioButton(Dialog)
        self.radioLlocsBtn.setGeometry(QtCore.QRect(480, 170, 116, 22))
        self.radioLlocsBtn.setObjectName(_fromUtf8("radioLlocsBtn"))
        self.radioAltresBtn = QtGui.QRadioButton(Dialog)
        self.radioAltresBtn.setGeometry(QtCore.QRect(610, 170, 116, 22))
        self.radioAltresBtn.setObjectName(_fromUtf8("radioAltresBtn"))
        self.listMetadataL = QtGui.QListWidget(Dialog)
        self.listMetadataL.setGeometry(QtCore.QRect(470, 200, 121, 161))
        self.listMetadataL.setObjectName(_fromUtf8("listMetadataL"))
        self.listMetadataA = QtGui.QListWidget(Dialog)
        self.listMetadataA.setGeometry(QtCore.QRect(610, 200, 121, 161))
        self.listMetadataA.setObjectName(_fromUtf8("listMetadataA"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Titol:", None))
        self.label_2.setText(_translate("Dialog", "Album:", None))
        self.label_4.setText(_translate("Dialog", "Metadates:", None))
        self.delMetadataBtn.setText(_translate("Dialog", "Treure", None))
        self.addMetaDataBtn.setText(_translate("Dialog", "Afeixir", None))
        self.addAlbumBtn.setText(_translate("Dialog", "Nou Album", None))
        self.label_3.setText(_translate("Dialog", "Data:", None))
        self.uploadFileBtn.setText(_translate("Dialog", "Fitxer", None))
        self.label_5.setText(_translate("Dialog", "TextLabel", None))
        self.radioPersonaBtn.setText(_translate("Dialog", "Persones", None))
        self.radioLlocsBtn.setText(_translate("Dialog", "Llocs", None))
        self.radioAltresBtn.setText(_translate("Dialog", "Altres", None))

