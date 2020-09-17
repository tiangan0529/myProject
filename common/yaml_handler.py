# -*- coding：utf-8 -*-
# @Time   : 2020/5/30 15:32
# @Author : 田干
# @Email  : tiangan_529@163.com
# @File   : yaml_handler.py
import yaml

def read_yaml(file):
    with open(file,'r',encoding='utf-8') as f:
        conf = yaml.load(f,Loader=yaml.SafeLoader)  # 指定一个loader，否则会发生warning
        return conf
