# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2020/4/16  11:52 
# 文件  add_printer
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import requests

def messages():
    sellerId_text = text1.get(0.0, END)
    sellerId_text = sellerId_text.strip()
    sn_text = text2.get(0.0, END)
    sn_text = sn_text.strip()
    token_text = text3.get(0.0, END)
    token_text = token_text.strip()

    if sellerId_text == "":
        messagebox.showinfo('提示', '点什么点，沙雕！')
    elif sn_text == "":
        messagebox.showinfo('提示', '点什么点，沙雕！')
    elif token_text == "":
        messagebox.showinfo('提示', '点什么点，沙雕！')
    else:
        json = {
                   "imgUrl": "https://fanxiaoxin.oss-cn-beijing.aliyuncs.com/crm-seller-pic/qa/9784000381992212.jpg",
                   "merchantName": '11',
                   "sn": sn_text,
                   "sellerId": sellerId_text
               }
        headers = {'content-type': 'application/json; charset=utf-8','client-name':'app',
                             'token': token_text}
        response = requests.post("http://qa-crm.xiaoxin.tech/crm/customer/app/merchantOnline/addSellerPrint",
                                 json=json,headers=headers
                                 ).json()
        print(response)
        result_text = response['success'] # 获取结果
        if result_text == True:
            text4.insert(INSERT, "绑定申请成功")
        else:
            text4.insert(INSERT, "绑定失败")




def clean():
    """清空多行文本框以及弹出提示框"""
    sellerId_text = text1.get(0.0, END)
    sellerId_text = sellerId_text.strip()
    sn_text = text2.get(0.0, END)
    sn_text = sn_text.strip()
    token_text = text3.get(0.0, END)
    token_text = token_text.strip()
    content = text4.get(0.0, END)
    content = content.strip()
    if sellerId_text == ""and sn_text == "" and token_text == "" and content == "":
        messagebox.showinfo('提示', '沙雕！！！')
    text1.delete(0.0, END)
    text2.delete(0.0, END)
    text3.delete(0.0, END)
    text4.delete(0.0, END)


def window_quit():
    """在退出软件时弹出提示框"""
    messagebox.showinfo('小提示', '每绑定一次请清空数据在进行绑定')
    window.quit()


if __name__ == '__main__':
    # 翻译工具界面设计
    # 实例化object，建立窗口window
    window = tk.Tk()
    # 窗口名称
    window.title("绑定打印机")
    # 设置窗口大小
    window.geometry("500x200")
    # 禁止最大窗口
    window.resizable(0, 0)
    # 在界面上设定label1标签，（Label标签用于显示一个文本或图像）
    sellerId = tk.Label(window, text="sellerId：", font="宋体 10", height=2)
    sellerId.place(height=30, width=200, x=0, y=20)

    sn = tk.Label(window, text="打印机编号：", font="宋体 10", height=2)
    sn.place(height=30, width=200, x=0, y=80)

    token = tk.Label(window, text="crm_token：", font="宋体 10", height=2)
    token.place(height=30, width=200, x=0, y=140)

    result = tk.Label(window, text="结果：", font="宋体 10", height=2)
    result.place(height=30, width=200, x=300, y=60)
    # 接收翻译后的内容（设置Text标签，多行文本框，可用来收集或显示多行文本）

    text1 = tk.Text(window, width=50, font=('黑体', 12))
    text1.place(height=30, width=150, x=140, y=20)

    text2 = tk.Text(window, width=50, font=('黑体', 12))
    text2.place(height=30, width=150, x=140, y=80)

    text3 = tk.Text(window, width=50, font=('黑体', 12))
    text3.place(height=30, width=150, x=140, y=140)

    text4 = tk.Text(window, width=50, font=('黑体', 12))
    text4.place(height=50, width=180, x=300, y=100)

    # 设置Button按钮，点击时执行一个动作
    button1 = tk.Button(window, text="绑定", command=messages, width=10, font="华文中宋 12",fg='green')
    button1.place(height=30, width=80, x=300, y=20)
    # button2 = tk.Button(window, text="退出程序", command=window_quit, width=10, font="华文中宋 12")
    # button2.place(height=30, width=100, x=100, y=100)
    button3 = tk.Button(window, text="清除", command=clean, width=10, font="华文中宋 12", fg='red')
    button3.place(height=30, width=80, x=400, y=20)
    # 主窗口循环显示
    window.mainloop()