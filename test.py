# -*- coding by utf-8
# Email   : tiangan_529@163.com
# Author  : 田干
# Time    : 2020/8/26 16:59
# File    : test.py
# import json
#
# print(int(9/2))
#
# print(round((99*0.08)*0.75))
#
#
# a =1
# b = 2
# a,b = b,a
#
# print(a,b)
#
#
# data = '''{
#  "priceId": 716,
#  "quantity": 2,
#  "addrId": 950252,
#  "memberCouponId":'{"user_id":"tg","age":18}'
# }'''
# # 先转化成json
# all = eval(data)
# # 再将第二层转换成json
# a = json.loads(all['memberCouponId'])
# # 转换后的json再赋值进去
# all['memberCouponId'] =  a
# print(all)
#
#
#
# info = '''{
#       "devId": "6cb27196d876b821d7o9nl",
#       "resetFactory": True,
#       "options": '{
#                  'clearDp': true,
#                  'pushToApp': true
#                 }'
# }'''
#
# a = 142.020202
#
# print(int(a))
#

from selenium import webdriver


url = 'https://wenku.baidu.com/view/f4ab0502ff4733687e21af45b307e87100f6f853.html'

