from time import sleep

import pymysql
from tkinter import *
from tkinter import messagebox
import tkinter as tk
# 需要拷贝的表名

db = pymysql.connect(host="test.kakahui.net", user="testuser", passwd="test@cdELk3", db="scrm_balance", port=3306)
cursor = db.cursor()
message=''

def copy_table(table_name):
    global message
    try:

        cursor.execute("""DELETE FROM wechat_platform.%s""" % table_name)

        cursor.execute("""insert into wechat_platform.%s select * from  knowledge.%s )""" % (table_name, table_name))
        db.commit()
        message = '同步表： %s 成功\n' % table_name
    except Exception as e:
        message = '同步表： %s 失败\n '
        db.rollback()



def get_messages():
    content = text.get(0.0, END)
    content = content.strip()
    if content == "":
        messagebox.showinfo('提示', '点什么点，沙雕！')
    else:
        tables = content.split(',')
        for tb_name in tables:
            copy_table(tb_name)
            text2.insert(INSERT, message)






def clean():
    """清空多行文本框以及弹出提示框"""
    content = text.get(0.0, END)
    content = content.strip()
    content2 = text2.get(0.0, END)
    content2 = content2.strip()
    if content == "" and content2 == "":
        messagebox.showinfo('提示', '沙雕！！！')
    text.delete(0.0, END)
    text2.delete(0.0, END)


def window_quit():
    """在退出软件时弹出提示框"""
    messagebox.showinfo('小提示', '只有表存在的情况下才能同步')
    window.quit()
    balance_cursor.close()
    balance.close()






if __name__ == '__main__':
    # 工具界面设计
    # 实例化object，建立窗口window
    window = tk.Tk()
    # 窗口名称
    window.title("同步表数据")
    # 设置窗口大小
    window.geometry("500x200")
    # 禁止最大窗口
    window.resizable(0, 0)



    text = tk.Text(window, width=50, font=('黑体', 12))
    text.place(height=50, width=250, x=120, y=30)
    text2 = tk.Text(window, width=50, font=('黑体', 12))
    text2.place(height=50, width=250, x=120, y=120)

    # 设置Button按钮，点击时执行一个动作
    button1 = tk.Button(window, text="同步表", command=get_messages, width=10, font="华文中宋 12",fg='green')
    button1.place(height=60, width=80, x=30, y=70)
    button2 = tk.Button(window, text="退出程序", command=window_quit, width=10, font="华文中宋 12")
    button2.place(height=30, width=80, x=380, y=120)
    button3 = tk.Button(window, text="清除数据", command=clean, width=10, font="华文中宋 12", fg='red')
    button3.place(height=30, width=80, x=380, y=60)
    # 主窗口循环显示
    window.mainloop()