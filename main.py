# -*- coding: utf-8 -*-
# @Time : 2020-08-03 16:09
# @Author : zcw
# @Site : 
# @File : main.py

from monitor.app.MonitorApp import MonitorApp
import sys


if __name__ == '__main__':
    app_monitor = MonitorApp()
    status = app_monitor.exec()
    sys.exit(status)

