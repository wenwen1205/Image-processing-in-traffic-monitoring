# -*- coding: utf-8 -*-
# @Time : 2020-08-03 16:09
# @Author : zcw
# @Site : 
# @File : MonitorApp.py

from PyQt5.QtWidgets import QApplication, QDialog
from monitor.forms.MonitorMainForm import MonotorMainForm
import sys


class MonitorApp(QApplication):
    def __init__(self):
        super(MonitorApp, self).__init__(sys.argv)
        self.dlg = MonotorMainForm()
        self.dlg.show()
