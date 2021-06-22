# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2021/5/27  21:56 
# 文件  small_link

import time

import requests
from tkinter import *
from tkinter import messagebox
import tkinter as tk


def update_link(turl):
    data={'turl':turl}
    params={'ajaxtimestamp':str(int(time.time()*1000))}
    r = str(requests.post('https://duanwangzhihuanyuan.bmcx.com/web_system/bmcx_com_www/system/file/duanwangzhihuanyuan/get/',
                     params=params,data=data).text)

    if('亲' not in r):

        return r.split("\"")[3]
    else:
        return '亲！不是短网址或暂不支持还原。'


def get_messages():
    content = text.get(0.0, END)
    content = content.strip()
    if content == "" or content is None:
        messagebox.showinfo('提示', '点什么点，沙雕！')
    else:
        text2.insert(INSERT, update_link(content))





def clean():
    """清空多行文本框以及弹出提示框"""
    content = text.get(0.0, END)
    content = content.strip()
    content2 = text2.get(0.0, END)
    content2 = content2.strip()
    if content == "" and content2 =="":
        messagebox.showinfo('提示', '沙雕！！！')
    text.delete(0.0, END)
    text2.delete(0.0, END)


def window_quit():
    """在退出软件时弹出提示框"""
    messagebox.showinfo('小提示', '只支持短链转长链')
    window.quit()







if __name__ == '__main__':
    # 工具界面设计
    # 实例化object，建立窗口window
    window = tk.Tk()
    # 窗口名称
    window.title("短链转换工具")
    # 设置窗口大小
    window.geometry("500x250")
    # 禁止最大窗口
    window.resizable(0, 0)
    label1 = tk.Label(window, text="请输入要转换的短链：", font="宋体 10", height=2)
    # 放置label标签
    label1.place(height=30, width=130, x=20, y=10)

    label2 = tk.Label(window, text="转换后的长链：", font="宋体 10", height=2)
    # 放置label标签
    label2.place(height=30, width=100, x=20, y=120)

    # 接收结果
    text = tk.Text(window, width=50, font=('黑体', 12))
    text.place(height=30, width=450, x=20, y=50)
    text2 = tk.Text(window, width=50, font=('黑体', 12))
    text2.place(height=60, width=450, x=20, y=150)

    # 设置Button按钮，点击时执行一个动作
    button1 = tk.Button(window, text="转换链接", command=get_messages, width=10, font="华文中宋 12",fg='green')
    button1.place(height=30, width=80, x=20, y=90)
    button2 = tk.Button(window, text="退出程序", command=window_quit, width=10, font="华文中宋 12")
    button2.place(height=30, width=80, x=210, y=90)
    button3 = tk.Button(window, text="清除数据", command=clean, width=10, font="华文中宋 12", fg='red')
    button3.place(height=30, width=80, x=390, y=90)
    # 主窗口循环显示
    window.mainloop()