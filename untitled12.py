#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:45:37 2022

@author: ubuntu
"""
from PyQt5.Qt import *
import sys
class MyWin(QWidget):
    def __init__(self):
        super(MyWin, self).__init__()
        self.control=False

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Control):
            self.control=True

    def keyReleaseEvent(self,event):
        if (event.key() == Qt.Key_Control):
            self.control = False

    def mouseMoveEvent(self, event):
        #重载mouseMoveEvent方法，监听鼠标移动,默认情况下只有当鼠标被点击时才会触发鼠标事件，从而被该方法监听到
        print("鼠标位置 ",event.localPos().x(),event.localPos().y())
        ################案例#############
        # label默认位置：(50, 50)
        # label随鼠标指针位置改变而改变
# 利用control键组合鼠标光标控制标签移动
        if self.control == True:
            label.move(event.localPos().x(),event.localPos().y())
        ################案例#############

app=QApplication(sys.argv)
window=MyWin()
window.setWindowTitle("鼠标移动")
window.resize(200,200)
window.setMouseTracking(True)  # 参数为True时，当鼠标进入window控件内便处于跟踪状态，即使不点击鼠标也会发射鼠标事件消息
# 默认情况下，鼠标处于非跟踪状态
print(window.hasMouseTracking())  # 查看鼠标跟踪状态

#################鼠标跟踪应用案例################
label=QLabel(window) # 为窗口增加一个子控件
label.setText("这是一个标签")
label.setStyleSheet("background-color:cyan;")
label.move(50,50)

#################鼠标跟踪应用案例################

window.show()
sys.exit(app.exec_())

