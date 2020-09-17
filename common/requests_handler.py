# -*- coding：utf-8 -*-
# @Time   : 2020/6/10 23:21
# @Author : 田干
# @Email  : tiangan_529@163.com
# @File   : requests_handler.py
import requests

'''函数封装'''
def visit(url, method, params=None, data=None, json=None, **kwargs):
    '''
    访问接口，返回响应结果类型为 json 格式
    :param url: 需要访问的接口地址
    :param method: get、post
    :param params: 需要用到就传
    :param data: 需要用到就传
    :param json: 需要用到就传
    :param kwargs: 还有参数，直接用关键字参数传进去
    :return: res.json()
    '''
    res = requests.request(
        method,
        url,
        params=params,
        data=data,
        json=json,
        **kwargs
    )
    try:
        return res.json()
    except Exception as e:
        raise e
