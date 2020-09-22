# -*- coding by utf-8
# Email   : tiangan_529@163.com
# Author  : 田干
# Time    : 2020/8/26 13:51
# File    : test_buyNowCreateOrder.py

import unittest
import ddt
import json
from decimal import *
from common.requests_handler import visit
from middleware.handler import Handler
from BeautifulReport import BeautifulReport

hd = Handler()
test_data = hd.excel.read_file('buyNowCreateOrder')
logger = hd.logger


@ddt.ddt
class TestBuyNowCreateOrder(unittest.TestCase):
    '''测试创建订单接口'''

    @classmethod
    def setUpClass(cls) -> None:
        cls.L0_token = hd.L0_token
        cls.L1_token = hd.L1_token
        cls.L2_token = hd.L2_token
        cls.L3_token = hd.L3_token
        cls.L0_user_id = hd.L0_user_id
        cls.L1_user_id = hd.L1_user_id
        cls.L2_user_id = hd.L2_user_id
        cls.L3_user_id = hd.L3_user_id
        cls.L0_mobile = hd.L0_mobile
        cls.L1_mobile = hd.L1_mobile
        cls.L2_mobile = hd.L2_mobile
        cls.L3_mobile = hd.L3_mobile
    def setUp(self) -> None:
        self.db = hd.db_class()

    def tearDown(self) -> None:
        self.db.close()

    @BeautifulReport.add_test_img('测试报告.png')
    @ddt.data(*test_data)
    def test_buyNowCreateOrder(self,test_info):
        '''
        创建订单接口
        test_info['title']
        '''
        # 全场商品可用

        if test_info['user_level'] == 'L0':
            # 全场可用优惠券
            if "#mCouponId1#" in test_info['data']:
                # 发送优惠券
                hd.add_coupon(self.L0_mobile, hd.yaml['coupon']['coupon_id1'])
                sql = 'select member_coupon_id from db_yshu_life.ys_member_coupon where member_coupon_user_id = {} and member_coupon_status = 1 and member_coupon_cid = {}'.format(self.L0_user_id, hd.yaml['coupon']['coupon_id1'])
                memberCouponId = self.db.query_db(sql)['member_coupon_id']
                test_info['data'] = test_info['data'].replace('#mCouponId1#', str(memberCouponId))
            # 指定商品可用
            if "#mCouponId2#" in test_info['data']:
                hd.add_coupon(self.L0_mobile, hd.yaml['coupon']['coupon_id2'])
                sql = 'select member_coupon_id from db_yshu_life.ys_member_coupon where member_coupon_user_id = {} and member_coupon_status = 1 and member_coupon_cid = {}'.format(self.L0_user_id, hd.yaml['coupon']['coupon_id2'])
                memberCouponId = self.db.query_db(sql)['member_coupon_id']
                test_info['data'] = test_info['data'].replace('#mCouponId2#', str(memberCouponId))
            # 指定商品不可用
            if "#mCouponId3#" in test_info['data']:
                hd.add_coupon(self.L0_mobile, hd.yaml['coupon']['coupon_id3'])
                sql = 'select member_coupon_id from db_yshu_life.ys_member_coupon where member_coupon_user_id = {} and member_coupon_status = 1 and member_coupon_cid = {}'.format(self.L0_user_id, hd.yaml['coupon']['coupon_id3'])
                memberCouponId = self.db.query_db(sql)['member_coupon_id']
                test_info['data'] = test_info['data'].replace('#mCouponId3#', str(memberCouponId))
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # L1
        elif test_info['user_level'] == 'L1':
            if "#mCouponId1#" in test_info['data']:
                hd.add_coupon(self.L1_mobile, hd.yaml['coupon']['coupon_id1'])
                sql = 'select member_coupon_id from db_yshu_life.ys_member_coupon where member_coupon_user_id = {} and member_coupon_status = 1 and member_coupon_cid = {}'.format(self.L1_user_id, hd.yaml['coupon']['coupon_id1'])
                memberCouponId = self.db.query_db(sql)['member_coupon_id']
                test_info['data'] = test_info['data'].replace('#mCouponId1#', str(memberCouponId))
            # 指定商品可用
            if "#mCouponId2#" in test_info['data']:
                hd.add_coupon(self.L1_mobile, hd.yaml['coupon']['coupon_id2'])
                sql = 'select member_coupon_id from db_yshu_life.ys_member_coupon where member_coupon_user_id = {} and member_coupon_status = 1 and member_coupon_cid = {}'.format(self.L1_user_id,hd.yaml['coupon']['coupon_id2'])
                memberCouponId = self.db.query_db(sql)['member_coupon_id']
                test_info['data'] = test_info['data'].replace('#mCouponId2#', str(memberCouponId))
            # 指定商品不可用
            if "#mCouponId3#" in test_info['data']:
                hd.add_coupon(self.L1_mobile, hd.yaml['coupon']['coupon_id3'])
                sql = 'select member_coupon_id from db_yshu_life.ys_member_coupon where member_coupon_user_id = {} and member_coupon_status = 1 and member_coupon_cid = {}'.format(self.L1_user_id, hd.yaml['coupon']['coupon_id3'])
                memberCouponId = self.db.query_db(sql)['member_coupon_id']
                test_info['data'] = test_info['data'].replace('#mCouponId3#', str(memberCouponId))
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # L2
        elif test_info['user_level'] == 'L2':
            if "#mCouponId1#" in test_info['data']:
                hd.add_coupon(self.L2_mobile, hd.yaml['coupon']['coupon_id1'])
                sql = 'select member_coupon_id from db_yshu_life.ys_member_coupon where member_coupon_user_id = {} and member_coupon_status = 1 and member_coupon_cid = {}'.format(self.L2_user_id, hd.yaml['coupon']['coupon_id1'])
                memberCouponId = self.db.query_db(sql)['member_coupon_id']
                test_info['data'] = test_info['data'].replace('#mCouponId1#', str(memberCouponId))
            # 指定商品可用
            if "#mCouponId2#" in test_info['data']:
                hd.add_coupon(self.L2_mobile, hd.yaml['coupon']['coupon_id2'])
                sql = 'select member_coupon_id from db_yshu_life.ys_member_coupon where member_coupon_user_id = {} and member_coupon_status = 1 and member_coupon_cid = {}'.format(self.L2_user_id, hd.yaml['coupon']['coupon_id2'])
                memberCouponId = self.db.query_db(sql)['member_coupon_id']
                test_info['data'] = test_info['data'].replace('#mCouponId2#', str(memberCouponId))
            # 指定商品不可用
            if "#mCouponId3#" in test_info['data']:
                hd.add_coupon(self.L2_mobile, hd.yaml['coupon']['coupon_id3'])
                sql = 'select member_coupon_id from db_yshu_life.ys_member_coupon where member_coupon_user_id = {} and member_coupon_status = 1 and member_coupon_cid = {}'.format(self.L2_user_id, hd.yaml['coupon']['coupon_id3'])
                memberCouponId = self.db.query_db(sql)['member_coupon_id']
                test_info['data'] = test_info['data'].replace('#mCouponId3#', str(memberCouponId))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # L3
        else:
            if "#mCouponId1#" in test_info['data']:
                hd.add_coupon(self.L3_mobile, hd.yaml['coupon']['coupon_id1'])
                sql = 'select member_coupon_id from db_yshu_life.ys_member_coupon where member_coupon_user_id = {} and member_coupon_status = 1 and member_coupon_cid = {}'.format(self.L3_user_id, hd.yaml['coupon']['coupon_id1'])
                memberCouponId = self.db.query_db(sql)['member_coupon_id']
                test_info['data'] = test_info['data'].replace('#mCouponId1#', str(memberCouponId))
            # 指定商品可用
            if "#mCouponId2#" in test_info['data']:
                hd.add_coupon(self.L3_mobile, hd.yaml['coupon']['coupon_id2'])
                sql = 'select member_coupon_id from db_yshu_life.ys_member_coupon where member_coupon_user_id = {} and member_coupon_status = 1 and member_coupon_cid = {}'.format(self.L3_user_id, hd.yaml['coupon']['coupon_id2'])
                memberCouponId = self.db.query_db(sql)['member_coupon_id']
                test_info['data'] = test_info['data'].replace('#mCouponId2#', str(memberCouponId))
            # 指定商品不可用
            if "#mCouponId3#" in test_info['data']:
                hd.add_coupon(self.L3_mobile, hd.yaml['coupon']['coupon_id3'])
                sql = 'select member_coupon_id from db_yshu_life.ys_member_coupon where member_coupon_user_id = {} and member_coupon_status = 1 and member_coupon_cid = {}'.format(self.L3_user_id, hd.yaml['coupon']['coupon_id3'])
                memberCouponId = self.db.query_db(sql)['member_coupon_id']
                test_info['data'] = test_info['data'].replace('#mCouponId3#', str(memberCouponId))


        headers = hd.replace_data(test_info['headers'])
        headers = json.loads(headers)
        data = json.loads(test_info['data'])


        logger.info("==================================开始执行第{}条测试用例==================================".format(test_info['case_id']))
        logger.info('传参：{}'.format(data))
        logger.info('测试用例名称：{}'.format(test_info['title']))
        res = visit(
            url= hd.yaml['http']['base_url1'] + test_info['url'],
            method= test_info['method'],
            headers= headers,
            params= data
        )

        logger.info('接口响应数据：{}'.format(res))

        expected = json.loads(test_info['expected'])
        try:
            for k, v in expected.items():
                self.assertEqual(res[k], v)

            if res['code'] == 0:
                # 获商品市场价
                sql = 'select og_market_price, og_rebate from db_yshu_life.ys_order_goods where og_price_id ={};'.format(data['priceId'])
                goods_info = self.db.query_db(sql)
                self.price_market = goods_info['og_market_price']
                self.rebate = goods_info['og_rebate']
                # 获取该订单的优惠券金额，积分，实付金额
                sql = 'select order_coupon_money, order_points, order_pay_money from db_yshu_life.ys_order where order_id ={};'.format(
                    res['data']['orderId'])
                order_info = self.db.query_db(sql)

                logger.debug('订单的原价格：{}'.format(self.price_market))

                # 判断商品是否可用优惠券
                if 'memberCouponId' in test_info['data'] and test_info['if_coupon'] == 1:

                    # 查询优惠券的面值
                    sql = 'select member_coupon_worth from db_yshu_life.ys_member_coupon where member_coupon_id ={};' \
                        .format(data['memberCouponId'])
                    # 分摊后优惠券面值
                    coupon_worth = self.db.query_db(sql)['member_coupon_worth'] / data['quantity']
                    logger.debug('订单的优惠券：{}'.format(coupon_worth))

                    # 返利
                    rebate_account = ((Decimal(str(self.price_market)) - Decimal(str(coupon_worth)))) / Decimal(
                        str(self.price_market)) * self.rebate
                    logger.debug('订单的返利：{}'.format(rebate_account))
                    # L0 会员
                    if test_info['user_level'] == 'L0':
                        pay_money = (self.price_market - coupon_worth) * data['quantity']
                        logger.debug('L0用户计算后的订单实付金额为：{}; 优惠券金额{}'.format(pay_money, coupon_worth * data['quantity']))
                        self.assertEqual(Decimal(str(order_info['order_pay_money'])), Decimal(str(pay_money)))
                        logger.info('订单金额校验通过')
                    # L1 会员
                    elif test_info['user_level'] == 'L1':
                        pay_money = (Decimal(str(self.price_market)) - Decimal(str(coupon_worth)) - (rebate_account * Decimal(0.5))) * data['quantity']
                        logger.debug('订单实际金额：{}; 订单预期金额：{}'.format(order_info['order_pay_money'], pay_money))
                        self.assertTrue(
                            abs((Decimal(str(order_info['order_pay_money'])) - Decimal(str(pay_money)).quantize(Decimal('0.0000')))) < 0.1)
                        logger.info('订单金额校验通过')
                    # L2 会员
                    elif test_info['user_level'] == 'L2':
                        pay_money = (Decimal(str(self.price_market)) - Decimal(str(coupon_worth)) - (rebate_account * Decimal(0.75))) * data['quantity']
                        logger.debug('订单实际金额：{}; 订单预期金额：{}'.format(order_info['order_pay_money'], pay_money))
                        self.assertTrue(
                            abs((Decimal(str(order_info['order_pay_money'])) - Decimal(str(pay_money)).quantize(Decimal('0.0000')))) < 0.1)
                        logger.info('订单金额校验通过')                    # L3 会员
                    else:
                        pay_money = (Decimal(str(self.price_market)) - Decimal(str(coupon_worth)) - (rebate_account * Decimal(0.85))) * data['quantity']
                        logger.debug('订单实际金额：{}; 订单预期金额：{}'.format(order_info['order_pay_money'], pay_money))
                        self.assertTrue(
                            abs((Decimal(str(order_info['order_pay_money'])) - Decimal(str(pay_money)).quantize(Decimal('0.0000')))) < 0.1)
                        logger.info('订单金额校验通过')

                    # 区分第三方商品和自营商品, 校验积分
                    if test_info['goods_type'] == 1:
                        logger.info('购买自营商品，预期的积分是：{}'.format(int(pay_money)))
                        self.assertEqual(int(pay_money), order_info['order_points'])
                    else:
                        logger.info('购买第三方商品，预期的积分是：{}'.format(int(pay_money / 2)))
                        self.assertEqual(int(pay_money / 2), order_info['order_points'])
                else:
                    pay_money = order_info['order_pay_money']
                    # 区分第三方商品和自营商品, 校验积分
                    if test_info['goods_type'] == 1:
                        logger.info('购买自营商品，预期的积分是：{}'.format(int(pay_money)))
                        self.assertEqual(int(pay_money), order_info['order_points'])
                    else:
                        logger.info('购买第三方商品，预期的积分是：{}'.format(int(pay_money / 2)))
                        self.assertEqual(int(pay_money / 2), order_info['order_points'])
                logger.info('第{}条用例执行通过'.format(test_info['case_id']))
                self.result = 'PASS'
        except AssertionError as e:
            logger.error('第{}条用例执行失败：{}'.format(test_info['case_id'], e))
            self.result = 'Fail'
            raise e
        # finally:
        #     hd.excel.write('buyNowCreateOrder', test_info['case_id'] + 1, 12, self.result)


