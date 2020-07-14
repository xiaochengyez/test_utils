# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2020/7/14  14:06 
# 文件  distance_tool
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import math
import rad


EARTH_REDIUS = 6378.137

def rad(d):
    return d * math.pi / 180.0

def getDistance(lat1, lng1, lat2, lng2):
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(
        math.sin(b / 2), 2)))
    s = s * EARTH_REDIUS
    return str(round(s, 3)) + '千米'

def messages():
    lat1_text = text1.get(0.0, END)
    lat1_text = lat1_text.strip()
    lng1_text = text2.get(0.0, END)
    lng1_text = lng1_text.strip()
    lat2_text = text3.get(0.0, END)
    lat2_text = lat2_text.strip()
    lng2_text = text4.get(0.0, END)
    lng2_text = lng2_text.strip()

    if lat1_text == "":
        messagebox.showinfo('提示', '点什么点，沙雕！')
    elif lng1_text == "":
        messagebox.showinfo('提示', '点什么点，沙雕！')
    elif lat2_text == "":
        messagebox.showinfo('提示', '点什么点，沙雕！')
    elif lng2_text == "":
        messagebox.showinfo('提示', '点什么点，沙雕！')
    else:
        try:
            distance = getDistance(float(lat1_text),float(lng1_text),float(lat2_text),float(lng2_text))
            text5.insert(INSERT, distance)
        except:
            text5.insert(INSERT, '沙雕')





def clean():
    """清空多行文本框以及弹出提示框"""
    lat1_text = text1.get(0.0, END)
    lat1_text = lat1_text.strip()
    lng1_text = text2.get(0.0, END)
    lng1_text = lng1_text.strip()
    lat2_text = text3.get(0.0, END)
    lat2_text = lat2_text.strip()
    lng2_text = text4.get(0.0, END)
    lng2_text = lng2_text.strip()
    distance = text5.get(0.0, END)
    distance = distance.strip()
    if lat1_text == ""and lng1_text == "" and lat2_text == "" and lng2_text == "" and distance == "":
        messagebox.showinfo('提示', '沙雕！！！')
    text1.delete(0.0, END)
    text2.delete(0.0, END)
    text3.delete(0.0, END)
    text4.delete(0.0, END)
    text5.delete(0.0, END)


def window_quit():
    """在退出软件时弹出提示框"""
    messagebox.showinfo('小提示', '每查询一次请清空数据再进行查询')
    window.quit()


if __name__ == '__main__':
    # 翻译工具界面设计
    # 实例化object，建立窗口window
    window = tk.Tk()
    # 窗口名称
    window.title("计算距离")
    # 设置窗口大小
    window.geometry("500x200")
    # 禁止最大窗口
    window.resizable(0, 0)
    # 在界面上设定label1标签，（Label标签用于显示一个文本或图像）
    lat1 = tk.Label(window, text="经度：", font="宋体 10", height=2)
    lat1.place(height=30, width=80, x=0, y=20)

    lng1 = tk.Label(window, text="纬度：", font="宋体 10", height=2)
    lng1.place(height=30, width=80, x=200, y=20)

    lat2 = tk.Label(window, text="经度：", font="宋体 10", height=2)
    lat2.place(height=30, width=80, x=0, y=80)

    lng2 = tk.Label(window, text="纬度：", font="宋体 10", height=2)
    lng2.place(height=30, width=80, x=200, y=80)

    result = tk.Label(window, text="距离：", font="宋体 10", height=2)
    result.place(height=30, width=80, x=200, y=150)
    # 接收翻译后的内容（设置Text标签，多行文本框，可用来收集或显示多行文本）

    text1 = tk.Text(window, width=50, font=('黑体', 12))
    text1.place(height=30, width=100, x=60, y=20)

    text2 = tk.Text(window, width=50, font=('黑体', 12))
    text2.place(height=30, width=100, x=260, y=20)

    text3 = tk.Text(window, width=50, font=('黑体', 12))
    text3.place(height=30, width=100, x=60, y=80)

    text4 = tk.Text(window, width=50, font=('黑体', 12))
    text4.place(height=30, width=100, x=260, y=80)

    text5 = tk.Text(window, width=50, font=('黑体', 12))
    text5.place(height=30, width=100, x=260, y=150)

    # 设置Button按钮，点击时执行一个动作
    button1 = tk.Button(window, text="查询", command=messages, width=10, font="华文中宋 12",fg='green')
    button1.place(height=30, width=80, x=20, y=150)
    button3 = tk.Button(window, text="清除", command=clean, width=10, font="华文中宋 12", fg='red')
    button3.place(height=30, width=80, x=100, y=150)
    # 主窗口循环显示
    window.mainloop()