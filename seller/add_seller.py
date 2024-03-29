# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2019/11/30  15:28 
# 文件  add_seller
import time
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import requests

# 实例化object，建立窗口window
window = tk.Tk()
# 窗口名称
window.title("商家小工具")
# 设置窗口大小
window.geometry("800x600")
# 禁止最大窗口
window.resizable(0, 0)

def set_text(position):
    text = tk.Text(window, width=32, font=('黑体', 12))
    text.place(height=280, width=150, x=position, y=90)
    return text

def set_label(text,position):
    tk.Label(window, text=text, font="华文新魏 15", height=2).place(height=21, width=150, x=position, y=30)

# 设置Button按钮，点击时执行一个动作
def Button(text,command,position):
    tk.Button(window, text=text, command=command, width=10, font="华文中宋 12").\
        place(height=42, width=147, x=position, y=420)


seller_content = set_text(50)
phone_content = set_text(300)
result_content = set_text(550)
set_label('商家名字',50)
set_label('手机号',300)
set_label('执行结果',550)

# 在界面上设定label1标签，（Label标签用于显示一个文本或图像）

def add_seller():
    seller_name = seller_content.get(0.0, END).strip()
    phone = phone_content.get(0.0, END).strip()
    json = {
                    "id": "",
                    "area": {"areaId": 89},
                    "city": {"cityId": 1},
                    "sellerGroupId": 3,
                    "title": seller_name,
                    "phone": phone,
                    "operators": [{
                        "name": "xiaoxiao",
                        "mobile": phone,
                        "certId": "",
                        "bankName": "",
                        "bankCard": "",
                        "branchBankOne": "",
                        "branchBankTwo": "",
                        "status": "VALID",
                        "userName": "xiaoxiao"
                    }],
                    "address": '锦秋国际',
                    "longitude": "116.34873",
                    "latitude": "39.97584",
                    "license": "",
                    "food_license": "",
                    "saleMan": "张三",
                    "inputPerson": "lisi",
                    "checkPerson": "",
                    "pic": "",
                    "pictures": [],
                    "templateId": 89
                }

    if seller_name == "":
        messagebox.showinfo('提示', '请输入商家名称！')
    elif phone == "":
        messagebox.showinfo('提示', '请输入手机号！')
    else:
        response = requests.post("http://qa-admin.xiaoxin.tech/admin_management/seller/add",
                                 json=json).json()
        if response["data"] == True:
            translate = '创建成功,商家为' + seller_name
        else:
            translate = '创建失败'
        # #
        result_content.insert(INSERT, translate)



def clean():
    seller_name = seller_content.get(0.0, END).strip()
    phone = phone_content.get(0.0, END).strip()
    result = result_content.get(0.0, END).strip()
    """清空多行文本框以及弹出提示框"""
    if seller_name =="" and phone =="" and result=="":
        messagebox.showinfo('提示', '已经清空啦')
    seller_content.delete(0.0, END)
    phone_content.delete(0.0, END)
    result_content.delete(0.0, END)

def window_quit():
    """在退出软件时弹出提示框"""
    messagebox.showinfo('退出出商家工具')
    window.quit()
Button('创建sku',add_seller,50)
Button('清空数据', clean, 300)
Button('退出', window_quit, 550)


window.mainloop()