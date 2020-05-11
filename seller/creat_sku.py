# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2019/11/29  17:57 
# 文件  creat_sku
import tkinter as tk
class run:
    if __name__ == '__main__':

        # 实例化object，建立窗口window
        window = tk.Tk()
        # 窗口名称
        window.title("商家小工具")
        # 设置窗口大小
        window.geometry("800x600")
        # 禁止最大窗口
        window.resizable(0, 0)
        # 在界面上设定label1标签，（Label标签用于显示一个文本或图像）
        label1 = tk.Label(window, text="sku名字", font="华文新魏 15", height=2)
        # 放置label标签
        label1.place(height=20, width=150, x=50, y=30)
        label2 = tk.Label(window, text="商家id", font="华文新魏 15", height=2)
        label2.place(height=21, width=150, x=300, y=30)

        label3 = tk.Label(window, text="结果", font="华文新魏 15", height=2)
        label3.place(height=21, width=150, x=550, y=30)

        # （设置Text标签，多行文本框，可用来收集或显示多行文本）
        text1 = tk.Text(window, width=32, font=('黑体', 12))
        text1.place(height=280, width=150, x=50, y=90)
        text2 = tk.Text(window, width=32, font=('黑体', 12))
        text2.place(height=280, width=150, x=300, y=90)

        text3 = tk.Text(window, width=32, font=('黑体', 12))
        text3.place(height=280, width=150, x=550, y=90)


        # 设置Button按钮，点击时执行一个动作
        button1 = tk.Button(window, text="新增sku", command=messages, width=10, font="华文中宋 12")
        button1.place(height=41, width=152, x=52, y=420)
        button2 = tk.Button(window, text="退出程序", command=window_quit, width=10, font="华文中宋 12")
        button2.place(height=42, width=147, x=590, y=420)
        button3 = tk.Button(window, text="清空数据", command=clean, width=10, font="华文中宋 12", fg='red')
        button3.place(height=42, width=147, x=320, y=420)
        # 主窗口循环显示
        window.mainloop()
