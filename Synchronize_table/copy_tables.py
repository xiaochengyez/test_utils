import pymysql
from tkinter import *
from tkinter import messagebox
import tkinter as tk
# 需要拷贝的表名

tables = (
    'pay_order_line',
    't_camp',
    't_camp_date',
    't_class',
    't_course',
    't_customer',
    't_customer_pay_order',
    't_customer_source',
    't_order',
    't_package_course',
    't_teacher'
)
balance = pymysql.connect(host="test.kakahui.net", user="testuser", passwd="test@cdELk3", db="scrm_balance", port=3306)
balance_cursor = balance.cursor()
message=''

def copy_table(table_name):
    global message
    try:
        balance_cursor.execute("""show create table knowledge.%s""" % table_name)
        create_sql = balance_cursor.fetchall()[0][1]

        balance_cursor.execute("""drop table if exists scrm_balance.%s""" % table_name)
        balance_cursor.execute(create_sql)
        balance_cursor.execute("""insert into scrm_balance.%s select * from  knowledge.%s""" % (table_name, table_name))
        balance.commit()
        message = '同步表： %s 成功\n' % table_name
    except Exception as e:
        message = '同步表： %s 失败\n '
        balance.rollback()



def get_messages():
    content = text.get(0.0, END)
    content = content.strip()
    if content != "":
        messagebox.showinfo('提示', '点什么点，沙雕！')
    else:
        for tb_name in tables:
            copy_table(tb_name)
            text.insert(INSERT, message)






def clean():
    """清空多行文本框以及弹出提示框"""
    content = text.get(0.0, END)
    content = content.strip()
    if content == "":
        messagebox.showinfo('提示', '沙雕！！！')
    text.delete(0.0, END)


def window_quit():
    """在退出软件时弹出提示框"""
    messagebox.showinfo('小提示', '同步完成才能再次同步')
    window.quit()
    balance_cursor.close()
    balance.close()






if __name__ == '__main__':
    # 工具界面设计
    # 实例化object，建立窗口window
    window = tk.Tk()
    # 窗口名称
    window.title("同步订单")
    # 设置窗口大小
    window.geometry("500x200")
    # 禁止最大窗口
    window.resizable(0, 0)


    # 接收翻译后的内容（设置Text标签，多行文本框，可用来收集或显示多行文本）
    text = tk.Text(window, width=50, font=('黑体', 12))
    text.place(height=150, width=250, x=120, y=30)

    # 设置Button按钮，点击时执行一个动作
    button1 = tk.Button(window, text="同步订单", command=get_messages, width=10, font="华文中宋 12",fg='green')
    button1.place(height=60, width=80, x=30, y=70)
    button2 = tk.Button(window, text="退出程序", command=window_quit, width=10, font="华文中宋 12")
    button2.place(height=30, width=80, x=380, y=120)
    button3 = tk.Button(window, text="清除数据", command=clean, width=10, font="华文中宋 12", fg='red')
    button3.place(height=30, width=80, x=380, y=60)
    # 主窗口循环显示
    window.mainloop()