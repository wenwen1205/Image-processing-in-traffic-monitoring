# -*- coding: utf-8 -*-
# @Time : 2020-08-03 16:10
# @Author : zcw
# @Site : 
# @File : VideoPlay.py


from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from monitor.cores.ImageProcess import *

import cv2


class CameraPlay(QThread):
    sign_show = pyqtSignal(int, int, int, bytes)
    type = 0

    def __init__(self, dev_id):
        super(CameraPlay, self).__init__()
        # 完成摄像头初始化
        self.dev = cv2.VideoCapture(dev_id)  # 避免报一个警告
        self.dev.open(dev_id)
        self.isOver = False

    def changeType(self, type_id):
        self.type = type_id

    def run(self):
        while not self.isOver:
            # 抓取视频
            status, img = self.dev.read()
            if not status:
                print("读取失败, 结束线程！")
                self.dev.release()
                self.exit(0)
                break
            # 发送图像到窗体显示
            if self.type == 0:
                self.sign_show.emit(img.shape[0], img.shape[1], img.shape[2], img.tobytes())
            elif self.type == 1:
                img = toGray(img)
                self.sign_show.emit(img.shape[0], img.shape[1], 1, img.tobytes())
            elif self.type == 2:
                img = toBorder(img)
                self.sign_show.emit(img.shape[0], img.shape[1], 1, img.tobytes())
            elif self.type == 3:
                img = toGauss(img)
                self.sign_show.emit(img.shape[0], img.shape[1], img.shape[2], img.tobytes())
            elif self.type == 4:
                img = toLaplace(img)
                self.sign_show.emit(img.shape[0], img.shape[1], img.shape[2], img.tobytes())
            elif self.type == 5:
                img = toConv(img)
                self.sign_show.emit(img.shape[0], img.shape[1], img.shape[2], img.tobytes())
            else:
                self.sign_show.emit(img.shape[0], img.shape[1], img.shape[2], img.tobytes())
            QThread.usleep(100000)

    def close(self):
        # 用来释放线程与设备
        self.isOver = True
        while self.isRunning():  # 避免提前释放设备导致run函数中的操作报错
            self.isOver = True
        if self.dev.isOpened():
            self.dev.release()
