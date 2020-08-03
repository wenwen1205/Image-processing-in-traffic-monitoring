# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIMonitor.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlg_monitor(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1133, 597)
        self.lbl_video = QtWidgets.QLabel(Dialog)
        self.lbl_video.setGeometry(QtCore.QRect(40, 30, 640, 480))
        self.lbl_video.setStyleSheet("QFrame#frame{\n"
"\n"
"border-radius: 15px;\n"
"\n"
"border-width: 2px;\n"
"\n"
"border-style:solid;\n"
"\n"
"border-bottom-color: #888888;\n"
"\n"
"border-right-color: #888888;\n"
"\n"
"border-left-color: #FFFFFF;\n"
"\n"
"border-top-color: #FFFFFF;\n"
"\n"
"}")
        self.lbl_video.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbl_video.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_video.setObjectName("lbl_video")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(700, 30, 251, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_gray = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.btn_gray.setObjectName("btn_gray")
        self.bgp_imgprocess = QtWidgets.QButtonGroup(Dialog)
        self.bgp_imgprocess.setObjectName("bgp_imgprocess")
        self.bgp_imgprocess.addButton(self.btn_gray)
        self.gridLayout.addWidget(self.btn_gray, 0, 0, 1, 1)
        self.btn_laplace = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.btn_laplace.setObjectName("btn_laplace")
        self.bgp_imgprocess.addButton(self.btn_laplace)
        self.gridLayout.addWidget(self.btn_laplace, 3, 0, 1, 1)
        self.btn_conv = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.btn_conv.setObjectName("btn_conv")
        self.bgp_imgprocess.addButton(self.btn_conv)
        self.gridLayout.addWidget(self.btn_conv, 4, 0, 1, 1)
        self.btn_border = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.btn_border.setObjectName("btn_border")
        self.bgp_imgprocess.addButton(self.btn_border)
        self.gridLayout.addWidget(self.btn_border, 1, 0, 1, 1)
        self.btn_gauss = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.btn_gauss.setObjectName("btn_gauss")
        self.bgp_imgprocess.addButton(self.btn_gauss)
        self.gridLayout.addWidget(self.btn_gauss, 2, 0, 1, 1)
        self.btn_orig = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.btn_orig.setObjectName("btn_orig")
        self.bgp_imgprocess.addButton(self.btn_orig)
        self.gridLayout.addWidget(self.btn_orig, 5, 0, 1, 1)

        self.bgp_imgprocess.addButton(self.btn_orig, 0)
        self.bgp_imgprocess.addButton(self.btn_gray, 1)
        self.bgp_imgprocess.addButton(self.btn_border, 2)
        self.bgp_imgprocess.addButton(self.btn_gauss, 3)
        self.bgp_imgprocess.addButton(self.btn_laplace, 4)
        self.bgp_imgprocess.addButton(self.btn_conv, 5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_video.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#0000ff;\">视频显示区</span></p></body></html>"))
        self.btn_gray.setText(_translate("Dialog", "灰度图像显示"))
        self.btn_laplace.setText(_translate("Dialog", "拉普拉斯锐化显示"))
        self.btn_conv.setText(_translate("Dialog", "卷积特征显示"))
        self.btn_border.setText(_translate("Dialog", "边缘特征显示"))
        self.btn_gauss.setText(_translate("Dialog", "高斯模糊显示"))
        self.btn_orig.setText(_translate("Dialog", "原始图像显示"))

