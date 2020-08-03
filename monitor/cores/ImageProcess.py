# -*- coding: utf-8 -*-
# @Time : 2020-08-03 16:10
# @Author : zcw
# @Site : 
# @File : ImageProcess.py

import cv2
import time
import numpy as np


# 灰度图像转换
def getTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def toGray(img_src):
    img_dst = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    cv2.putText(img_dst, getTime(), (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    return img_dst


def toBorder(img_src):
    img_dst = cv2.Canny(img_src, 50, 255, True)
    cv2.putText(img_dst, getTime(), (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    return img_dst


def toGauss(img_src):
    img_dst = cv2.GaussianBlur(img_src, (19, 19),  sigmaX=5, sigmaY=5)
    cv2.putText(img_dst, getTime(), (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    return img_dst


def toLaplace(img_src):
    img_dst = cv2.Laplacian(img_src, -1,  ksize=3)
    cv2.putText(img_dst, getTime(), (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    return img_dst


def toConv(img_src):
    # -----------------------------
    # kernel = np.array([
    #     [-4, -2,  0],
    #     [-2,  1,  2],
    #     [ 0,  2,  4]
    # ])
    # img_dst = cv2.filter2D(img_src, -1, kernel, delta=0)
    # -----------------------------
    #
    kernel = np.array([
        [-1, 1],    # [1, 0, 1]
    ])
    img_dst = cv2.filter2D(img_src, -1, kernel, delta=128)
    # img_dst   = cv2.Sobel(img_src, -1, 1, 1, ksize=3, delta=150)
    cv2.putText(img_dst, getTime(), (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    return img_dst