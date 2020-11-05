# # -*- coding by utf-8
# # Email   : tiangan_529@163.com
# # Author  : 田干
# # Time    : 2020/8/26 16:59
# # File    : test.py
import unittest
import ddt
import json
from middleware.handler import Handler
from common.requests_handler import visit

hd = Handler()
logger = hd.logger
test_data = hd.excel.read_file('data')



@ddt.ddt
class TestHT(unittest.TestCase):
    '''passwordLogin'''

    @ddt.data(*test_data)
    def test_login(self,test_info):

        logger.debug('用户参数：{}'.format(test_info))

        headers = {'usertoken': 'e310b8e28f7cad52803cd836211cae65'}
        data = {
            'orderSn': test_info['orderSn'],
            'realName': test_info['realName'],
            'idNumber': test_info['idNumber']
        }
        # 访问接口
        res = visit(
            url= 'http://s.inglemirepharmmall.com/order/updateCustoms',
            method= 'post',
            headers= headers,
            data= data
        )
        logger.info('第{}条的响应是：{}'.format(test_info['case_id'], res['msg']))

if __name__ == '__main__':
    unittest.main()
