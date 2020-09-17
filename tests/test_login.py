# -*- coding：utf-8 -*-
# @Time   : 2020/6/13 15:36
# @Author : 田干
# @Email  : tiangan_529@163.com
# @File   : test_login.py
import unittest
import ddt
import json
from middleware.handler import Handler
from common.requests_handler import visit

hd = Handler()
logger = hd.logger
test_data = hd.excel.read_file('Login')

@ddt.ddt
class TestLogin(unittest.TestCase):
    '''passwordLogin'''

    @ddt.data(*test_data)
    def test_login(self,test_info):

        # 访问接口
        logger.info("==================================开始执行第{}条测试用例==================================".format(test_info['case_id']))

        res = visit(
            url= hd.yaml['http']['base_url1']+test_info['url'],
            method= test_info['method'],
            headers= json.loads(test_info['headers']),
            data= json.loads(test_info['data'])
        )

        expected = json.loads(test_info['expected'])
        logger.info('预期结果是：{}'.format(expected))
        logger.info('实际结果是：{}'.format(res))

        try:
            for k,v in expected.items():
                self.assertEqual(res[k],v)

            logger.info('用例执行通过')
            self.result = 'PASS'
        except AssertionError as e:
            logger.error('用例执行失败')
            self.result = 'Fail'
            raise e
        finally:
            hd.excel.write('Login',test_info['case_id']+1,9,self.result)

