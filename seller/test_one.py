# -*- coding: utf-8 -*-
# 作者  gongxc   
# 日期 2019/12/9  15:57 
# 文件  test_one
import requests

def test_one():
    r = requests.post("http://qa-sellercenter-web.xiaoxin.tech/seller/getSellerCenterInfo")
    print(r.text)