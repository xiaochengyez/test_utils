# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2020/8/21  16:46 
# 文件  update_user

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql
class MysqlUtil:
    @staticmethod
    def _connect_mysql():
        try:
            load_dict = {
                          "host": "xiaoxinqa.mysql.polardb.rds.aliyuncs.com",
                          "user": "xiaoxin_qa_devep",
                          "password": "!1qaz@2wsx",
                          "db": "c_user_center",
                          "charset": "utf8",
                          "port": 3306
                        }
            return pymysql.connect(cursorclass=pymysql.cursors.DictCursor, **load_dict)
        except Exception as e:
            raise e

    @classmethod
    def queryone(cls,sql, param=None):
        """
        返回结果集的第一条数据
        :param sql: sql语句
        :param param: string|tuple|list
        :return: 字典列表 [{}]
        """
        con = cls._connect_mysql()
        cur = con.cursor()

        row = None
        try:
            cur.execute(sql, param)
            row = cur.fetchone()
        except Exception as e:
            con.rollback()

        cur.close()
        con.close()
        return cls._simple_value(row)

    @classmethod
    def queryall(cls,sql, param=None):
        """
        返回所有查询到的内容 (分页要在sql里写好)
        :param sql: sql语句
        :param param: tuple|list
        :return: 字典列表 [{},{},{}...] or [,,,]
        """
        con = cls._connect_mysql()
        cur = con.cursor()

        rows = None
        try:
            cur.execute(sql, param)
            rows = cur.fetchall()
        except Exception as e:
            con.rollback()


        cur.close()
        con.close()
        return cls._simple_list(rows)

    @classmethod
    def insertmany(cls,sql, arrays=None):
        """
        批量插入数据
        :param sql: sql语句
        :param arrays: list|tuple [(),(),()...]
        :return: 入库数量
        """
        con = cls._connect_mysql()
        cur = con.cursor()

        cnt = 0
        try:
            cnt = cur.executemany(sql, arrays)
            con.commit()
        except Exception as e:
            con.rollback()


        cur.close()
        con.close()
        return cnt

    @classmethod
    def execute(cls,sql, param=None):
        """
        执行sql语句:修改或删除
        :param sql: sql语句
        :param param: string|list
        :return: 影响数量
        """
        con = cls._connect_mysql()
        cur = con.cursor()

        cnt = 0
        try:
            cnt = cur.execute(sql, param)
            con.commit()
        except Exception as e:
            con.rollback()


        cur.close()
        con.close()
        return cnt

    @staticmethod
    def _simple_list(rows):
        """
        结果集只有一列的情况, 直接使用数据返回
        :param rows: [{'id': 1}, {'id': 2}, {'id': 3}]
        :return: [1, 2, 3]
        """
        if not rows:
            return rows

        if len(rows[0].keys()) == 1:
            simple_list = []
            # print(rows[0].keys())
            key = list(rows[0].keys())[0]
            for row in rows:
                simple_list.append(row[key])
            return simple_list
        return rows

    @staticmethod
    def _simple_value(row):
        """
        结果集只有一行, 一列的情况, 直接返回数据
        :param row: {'count(*)': 3}
        :return: 3
        """
        if not row:
            return None

        if len(row.keys()) == 1:
            # print(row.keys())
            key = list(row.keys())[0]
            return row[key]
        return row



def messages():
    mobile = mobile_text.get(0.0, END)
    mobile = mobile.strip()
    if mobile == "":
        messagebox.showinfo('提示', '点什么点，沙雕！')
    else:
        result = MysqlUtil.execute("update biz_user set mobile = %s,open_id = %s,union_id=%s where mobile = %s", ('','','', mobile))
        if result==1:
            result_text.insert(INSERT, '更新成功')
        else:
            result_text.insert(INSERT, '未授权手机号')


def clean():
    """清空多行文本框以及弹出提示框"""
    mobile = mobile_text.get(0.0, END)
    mobile = mobile.strip()
    result = result_text.get(0.0, END)
    result = result.strip()
    if mobile == ""and result=="":
        messagebox.showinfo('提示', '沙雕！！！')
    result_text.delete(0.0, END)
    mobile_text.delete(0.0, END)


def window_quit():
    """在退出软件时弹出提示框"""
    messagebox.showinfo('小提示', '每更新用户一次请清空数据再进行更新')
    window.quit()


if __name__ == '__main__':
    # 翻译工具界面设计
    # 实例化object，建立窗口window
    window = tk.Tk()
    # 窗口名称
    window.title("更新用户")
    # 设置窗口大小
    window.geometry("500x150")
    # 禁止最大窗口
    window.resizable(0, 0)
    # 在界面上设定label1标签，（Label标签用于显示一个文本或图像）
    phone_label = tk.Label(window, text="请输入手机号：", font="宋体 10", height=2)
    # 放置label标签
    phone_label.place(height=30, width=150, x=0, y=10)
    result_label = tk.Label(window, text="结果：", font="宋体 10", height=2)
    result_label.place(height=30, width=50, x=300, y=10)


    mobile_text = tk.Text(window, width=50, font=('黑体', 12))
    mobile_text.place(height=30, width=150, x=30, y=50)

    result_text = tk.Text(window, width=50, font=('黑体', 12))
    result_text.place(height=30, width=150, x=300, y=50)

    # 设置Button按钮，点击时执行一个动作
    update_button = tk.Button(window, text="更新用户", command=messages, width=10, font="华文中宋 12",fg='green')
    update_button.place(height=30, width=100, x=50, y=100)

    quit_button = tk.Button(window, text="退出程序", command=window_quit, width=10, font="华文中宋 12")
    quit_button.place(height=30, width=100, x=350, y=100)

    clean_button = tk.Button(window, text="清空数据", command=clean, width=10, font="华文中宋 12", fg='red')
    clean_button.place(height=30, width=100, x=200, y=100)
    # 主窗口循环显示
    window.mainloop()