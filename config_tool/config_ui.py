# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_frmCytrillConfig(object):
    def setupUi(self, frmCytrillConfig):
        frmCytrillConfig.setObjectName(_fromUtf8("frmCytrillConfig"))
        frmCytrillConfig.resize(400, 190)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmCytrillConfig.sizePolicy().hasHeightForWidth())
        frmCytrillConfig.setSizePolicy(sizePolicy)
        frmCytrillConfig.setMinimumSize(QtCore.QSize(400, 190))
        frmCytrillConfig.setMaximumSize(QtCore.QSize(400, 190))
        frmCytrillConfig.setBaseSize(QtCore.QSize(400, 190))
        self.verticalLayout = QtGui.QVBoxLayout(frmCytrillConfig)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblInfo = QtGui.QLabel(frmCytrillConfig)
        self.lblInfo.setMinimumSize(QtCore.QSize(0, 65))
        self.lblInfo.setMaximumSize(QtCore.QSize(16777215, 65))
        self.lblInfo.setBaseSize(QtCore.QSize(0, 65))
        self.lblInfo.setLineWidth(1)
        self.lblInfo.setMidLineWidth(0)
        self.lblInfo.setWordWrap(True)
        self.lblInfo.setObjectName(_fromUtf8("lblInfo"))
        self.verticalLayout.addWidget(self.lblInfo)
        self.grdLayout = QtGui.QGridLayout()
        self.grdLayout.setObjectName(_fromUtf8("grdLayout"))
        self.lblESSID = QtGui.QLabel(frmCytrillConfig)
        self.lblESSID.setObjectName(_fromUtf8("lblESSID"))
        self.grdLayout.addWidget(self.lblESSID, 0, 0, 1, 1)
        self.lblPassword = QtGui.QLabel(frmCytrillConfig)
        self.lblPassword.setObjectName(_fromUtf8("lblPassword"))
        self.grdLayout.addWidget(self.lblPassword, 1, 0, 1, 1)
        self.lePassword = QtGui.QLineEdit(frmCytrillConfig)
        self.lePassword.setObjectName(_fromUtf8("lePassword"))
        self.grdLayout.addWidget(self.lePassword, 1, 1, 1, 1)
        self.leESSID = QtGui.QLineEdit(frmCytrillConfig)
        self.leESSID.setObjectName(_fromUtf8("leESSID"))
        self.grdLayout.addWidget(self.leESSID, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.grdLayout)
        self.btnWriteConfig = QtGui.QPushButton(frmCytrillConfig)
        self.btnWriteConfig.setObjectName(_fromUtf8("btnWriteConfig"))
        self.verticalLayout.addWidget(self.btnWriteConfig)
        self.lblStatus = QtGui.QLabel(frmCytrillConfig)
        self.lblStatus.setFrameShape(QtGui.QFrame.NoFrame)
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        self.verticalLayout.addWidget(self.lblStatus)

        self.retranslateUi(frmCytrillConfig)
        QtCore.QMetaObject.connectSlotsByName(frmCytrillConfig)
        frmCytrillConfig.setTabOrder(self.leESSID, self.lePassword)
        frmCytrillConfig.setTabOrder(self.lePassword, self.btnWriteConfig)

    def retranslateUi(self, frmCytrillConfig):
        frmCytrillConfig.setWindowTitle(_translate("frmCytrillConfig", "Cytrill Configuration Tool", None))
        self.lblInfo.setText(_translate("frmCytrillConfig", "Hold the down button in the left button area of your Cytrill controller and press \"Write config\", then release the button again. The config will now be written and the controller will automatically restart with the new config.", None))
        self.lblESSID.setText(_translate("frmCytrillConfig", "ESSID:", None))
        self.lblPassword.setText(_translate("frmCytrillConfig", "Password:", None))
        self.btnWriteConfig.setText(_translate("frmCytrillConfig", "Write config", None))
        self.lblStatus.setText(_translate("frmCytrillConfig", "Press \"Write config\"", None))

