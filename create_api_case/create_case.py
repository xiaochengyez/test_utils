import re
import os

import tkinter as tk
from tkinter import messagebox, END, INSERT

from requests import Session
template = """
teststeps:
-
    name: {caseName}
    variables:

    request:
        method: "{method}"
        url: {api}
        headers:
            Content-Type: application/json;charset=UTF-8
        {data_or_params}:
            {data}
                  
    validate:
        - eq: ["status_code", 200]

"""


def auto_gen_cases(swagger_url, project_name):
    """
    根据swagger返回的json数据自动生成yml测试用例模板
    :param swagger_url:
    :param project_name:
    :return:
    """
    try:
        res = Session().request('get', swagger_url).json()
        data = res.get('paths')

        workspace = os.getcwd()

        project_ = os.path.join(workspace, project_name)

        if not os.path.exists(project_):
            os.mkdir(project_)

        for k, v in data.items():
            pa_res = re.split(r'[/]+', k)
            dir, *case_name = pa_res[1:]

            if case_name:
                case_name = ''.join([x.title() for x in case_name]).casefold()
            else:
                case_name = dir

            file =case_name + '_api.yaml'

            dirs = os.path.join(project_, dir)

            if not os.path.exists(dirs):
                os.mkdir(dirs)

            os.chdir(dirs)

            if len(v) > 1:
                v = {'post': v.get('post')}
            for _k, _v in v.items():
                method = _k
                api = k
                data_or_params = 'params' if method == 'get' else 'json'
                parameters = _v.get('parameters')
                data_s = ''
                try:
                    for each in parameters:
                        data_s += each.get('name')
                        data_s += ': \n'
                        data_s += ' ' * 8
                except TypeError:
                    data_s += '{}'

            file_ = os.path.join(dirs, file)

            with open(file_, 'w', encoding='utf-8') as fw:
                fw.write(template.format(
                    method=method,
                    api=api,
                    caseName=case_name,
                    data_or_params=data_or_params,
                    data=data_s
                ))

            os.chdir(project_)
        result_text.insert(INSERT, "生成用例成功")
    except:
        result_text.insert(INSERT, "生成用例失败")

def get_messages():
    url = swagger_url_text.get(0.0, END)
    url = url.strip()
    name = project_name_text.get(0.0, END)
    name = name.strip()
    if url == "" or name == "":
        messagebox.showinfo('提示', '缺少swagger_url或者project_name！')
    else:
        auto_gen_cases(url,name)



def clean():
    """清空多行文本框以及弹出提示框"""
    url = swagger_url_text.get(0.0, END)
    url = url.strip()
    name = project_name_text.get(0.0, END)
    name = name.strip()
    result = result_text.get(0.0, END)
    result = result.strip()

    if url == "" and name == "" and result == "":
        messagebox.showinfo('提示', '沙雕！！！')
    swagger_url_text.delete(0.0, END)
    project_name_text.delete(0.0, END)
    result_text.delete(0.0, END)



def window_quit():
    """在退出软件时弹出提示框"""
    messagebox.showinfo('小提示', '生成类似于httprunner类似的yaml测试用例')
    window.quit()


if __name__ == '__main__':
    # 工具界面设计
    # 实例化object，建立窗口window
    window = tk.Tk()
    # 窗口名称
    window.title("自动生成yaml测试用例")
    # 设置窗口大小
    window.geometry("500x200")
    # 禁止最大窗口
    window.resizable(0, 0)

    swagger_url = tk.Label(window, text="swagger_url：", font="宋体 10", height=2)
    swagger_url.place(height=30, width=100, x=10, y=20)
    project_name = tk.Label(window, text="project_name：", font="宋体 10", height=2)
    project_name.place(height=30, width=100, x=10, y=120)

    result = tk.Label(window, text="执行结果：", font="宋体 10", height=2)
    result.place(height=30, width=100, x=230, y=120)
    # 接收翻译后的内容（设置Text标签，多行文本框，可用来收集或显示多行文本）
    swagger_url_text = tk.Text(window, width=50, font=('黑体', 12))
    swagger_url_text.place(height=40, width=400, x=20, y=60)
    project_name_text = tk.Text(window, width=50, font=('黑体', 12))
    project_name_text.place(height=30, width=100, x=120, y=120)

    result_text = tk.Text(window, width=50, font=('黑体', 12))
    result_text.place(height=30, width=100, x=320, y=120)
    # 设置Button按钮，点击时执行一个动作
    button1 = tk.Button(window, text="生成用例", command=get_messages, width=10, font="华文中宋 12",fg='green')
    button1.place(height=30, width=80, x=30, y=160)
    button2 = tk.Button(window, text="退出程序", command=window_quit, width=10, font="华文中宋 12")
    button2.place(height=30, width=80, x=330, y=160)
    button3 = tk.Button(window, text="清除数据", command=clean, width=10, font="华文中宋 12", fg='red')
    button3.place(height=30, width=80, x=180, y=160)
    # 主窗口循环显示
    window.mainloop()