# -*- coding:utf-8 -*-
# Author : CXC
# Data : 2019/8/16 10:52

import tkinter as tk
from tkinter import *
from tkinter import messagebox

import requests


def messages():
    content = text1.get(0.0, END)
    content = content.strip()
    if content == "":
        messagebox.showinfo('提示', '点什么点，沙雕！')
    else:
        data = {
            "i": content,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTIME",
            "typoResult": "false"

        }
        response = requests.post("http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule",
                                 data=data).json()
        # print(response)
        translate = response["translateResult"][0][0]["tgt"]  # 获取译文
        # 译文多行显示
        text2.insert(INSERT, translate)


def clean():
    """清空多行文本框以及弹出提示框"""
    content = text1.get(0.0, END)
    content = content.strip()
    content2 = text2.get(0.0, END)
    content2 = content2.strip()
    if content == ""and content2=="":
        messagebox.showinfo('提示', '沙雕！！！')
    text2.delete(0.0, END)
    text1.delete(0.0, END)


def window_quit():
    """在退出软件时弹出提示框"""
    messagebox.showinfo('小提示', '每翻译一次请清空数据在进行翻译')
    window.quit()


if __name__ == '__main__':
    # 翻译工具界面设计
    # 实例化object，建立窗口window
    window = tk.Tk()
    # 窗口名称
    window.title("晓成翻译")
    # 设置窗口大小
    window.geometry("500x200")
    # 禁止最大窗口
    window.resizable(0, 0)
    # 在界面上设定label1标签，（Label标签用于显示一个文本或图像）
    label1 = tk.Label(window, text="请输入要翻译的内容：", font="宋体 10", height=2)
    # 放置label标签
    label1.place(height=30, width=200, x=0, y=10)
    label2 = tk.Label(window, text="结果：", font="宋体 10", height=2)
    label2.place(height=30, width=60, x=300, y=10)
    # 接收翻译后的内容（设置Text标签，多行文本框，可用来收集或显示多行文本）
    text1 = tk.Text(window, width=50, font=('黑体', 12))
    text1.place(height=100, width=170, x=30, y=50)
    text2 = tk.Text(window, width=50, font=('黑体', 12))
    text2.place(height=100, width=170, x=300, y=50)
    # 设置Button按钮，点击时执行一个动作
    button1 = tk.Button(window, text="翻译", command=messages, width=10, font="华文中宋 12",fg='green')
    button1.place(height=30, width=80, x=210, y=50)
    # button2 = tk.Button(window, text="退出程序", command=window_quit, width=10, font="华文中宋 12")
    # button2.place(height=30, width=100, x=100, y=100)
    button3 = tk.Button(window, text="清除", command=clean, width=10, font="华文中宋 12", fg='red')
    button3.place(height=30, width=80, x=210, y=120)
    # 主窗口循环显示
    window.mainloop()
