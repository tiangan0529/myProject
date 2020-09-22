#!/user/bin/python3
# -*- coding: utf-8 -*-
# @Author   : 田干
# @Time     : 2020/7/2 15:36
# @File     : test_getGoodsListByCouponId.py

import unittest
import ddt
import json
from common.requests_handler import visit
from middleware.handler import Handler

hd = Handler()
logger = hd.logger
test_data = hd.excel.read_file('getGoodsListByCouponId')

@ddt.ddt
class TestGetGoodsListByCouponId(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.token = hd.L0_token

    def setUp(self) -> None:
        self.db = hd.db_class()

    def tearDown(self) -> None:
        self.db.close()

    @ddt.data(*test_data)
    def test_getGoodsListByCouponId(self,test_info):
        '''根据优惠券id获取商品'''


        # 替换参数化数据
        if "#invalidCouponId#" in test_info['data']:
            # 查询状态为失效的couponID
            sql = 'select * from db_yshu_lb.ys_coupon where coupon_status = 0'
            coupon_id = self.db.query_db(sql)['coupon_id']
            test_info['data'] = test_info['data'].replace("#invalidCouponId#",str(coupon_id))

        headers = hd.replace_data(test_info['headers'])
        headers = json.loads(headers)

        data = json.loads(test_info['data'])

        logger.info("==================================开始执行第{}条测试用例==================================".format(test_info['case_id']))

        res = visit(
            url= hd.yaml['http']['base_url1']+ test_info['url'],
            method= test_info['method'],
            headers= headers,
            params= data
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
            raise  e
        finally:
            hd.excel.write('getGoodsListByCouponId',test_info['case_id']+1,9,self.result)

