# -*- coding: utf-8 -*-
# @Time : 2020-08-03 16:10
# @Author : zcw
# @Site : 
# @File : MonitorMainForm.py

from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSignal
from monitor.uis.UIMonitor import Ui_dlg_monitor
from monitor.devs.VideoPlay import CameraPlay
import sys


class MonotorMainForm(QDialog):
    # 构造器
    sign_type = pyqtSignal(int)

    def __init__(self):
        super(MonotorMainForm, self).__init__()
        # 2. 创建Ui_dlg_monitor对象
        self.ui = Ui_dlg_monitor()
        # 3. 设置Ui_dlg_monitor对象的容器
        self.ui.setupUi(self)
        # 启动视频设备，并抓取视频图像
        # self.th_dev = CameraPlay(0)
        self.th_dev = CameraPlay("./data/testvideo.mp4")
        # 绑定一个函数同来处理抓取的视频
        self.th_dev.sign_show.connect(self.show_video)
        self.th_dev.start()  # 开始视频抓取工作

        self.ui.bgp_imgprocess.buttonClicked['int'].connect(self.selectType)
        self.sign_type.connect(self.th_dev.changeType)

    def selectType(self, btn_id):
        # 根据不同的选项案例，确定不同的图像处理方式
        self.sign_type.emit(btn_id)

    def show_video(self, h, w, d, bytes_video):
        if d == 3:
            image = QImage(bytes_video, w, h, d * w, QImage.Format_RGB888)

        if d == 1:
            image = QImage(bytes_video, w, h, d * w, QImage.Format_Grayscale8)

        pixmap = QPixmap.fromImage(image)

        self.ui.lbl_video.setPixmap(pixmap)
        self.ui.lbl_video.setScaledContents(True)

    def closeEvent(self, e):
        # 窗体关闭前的释放工作,条件不满足可以阻止窗体关闭
        sys.exit(0)

    def keyPressEvent(self, e):
        # 阻止按照ESC键关闭窗体
        pass

