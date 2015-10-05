# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'albumDialog.ui'
#
# Created: Sun Sep  6 16:30:35 2015
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

class Ui_AlbumDialog(object):
    def setupUi(self, AlbumDialog):
        AlbumDialog.setObjectName(_fromUtf8("AlbumDialog"))
        AlbumDialog.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(AlbumDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(AlbumDialog)
        self.label.setGeometry(QtCore.QRect(80, 60, 66, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(AlbumDialog)
        self.label_2.setGeometry(QtCore.QRect(80, 100, 66, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.titol = QtGui.QLineEdit(AlbumDialog)
        self.titol.setGeometry(QtCore.QRect(130, 50, 201, 27))
        self.titol.setObjectName(_fromUtf8("titol"))
        self.data = QtGui.QDateEdit(AlbumDialog)
        self.data.setGeometry(QtCore.QRect(130, 90, 110, 27))
        self.data.setObjectName(_fromUtf8("data"))

        self.retranslateUi(AlbumDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AlbumDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AlbumDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AlbumDialog)

    def retranslateUi(self, AlbumDialog):
        AlbumDialog.setWindowTitle(_translate("AlbumDialog", "Nou Album", None))
        self.label.setText(_translate("AlbumDialog", "Títol:", None))
        self.label_2.setText(_translate("AlbumDialog", "Data:", None))

