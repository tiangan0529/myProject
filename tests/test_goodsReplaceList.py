import unittest
import ddt
import json
from common.requests_handler import visit
from middleware.handler import Handler


hd = Handler()
test_data = hd.excel.read_file('goodsReplaceList')
logger = hd.logger

@ddt.ddt
class TestGoodsReplaceList(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.L3_token = hd.L3_token['token']

    def setUp(self) -> None:
        self.db = hd.db_class()

    def tearDown(self) -> None:
        self.db.close()

    @ddt.data(*test_data)
    def test_GoodsReplaceList(self,test_info):
        '''
        加入购物车接口
        :param test_info:用例数据
        '''
        # 替换token
        if '#token#' in test_info['headers']:
            test_info['headers'] = test_info['headers'].replace('#token#', self.L3_token)

        headers = json.loads(test_info['headers'])
        data = eval(test_info['data'])

        logger.debug('请求参数：{}'.format(data))
        logger.info("==================================开始执行第{}条测试用例==================================".format(test_info['case_id']))
        logger.info('开始访问接口：{}'.format(test_info['url']))
        # 访问接口
        res = visit(
            url= hd.yaml['http']['base_url1']+test_info['url'],
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

            if res['code'] == 0:
                if test_info['type'] == 2:
                    sql = '''
                    SELECT
                        count(*) 
                    FROM
                        db_yshu_life.ys_goods_price y
                        LEFT JOIN db_yshu_life.ys_goods g ON y.price_goods_id = g.goods_id 
                    WHERE
                        y.`status` = 2 
                        AND y.is_hide = 0 
                        AND g.goods_type = 1
                        AND y.price_supplier_id = 1
                    '''
                elif test_info['type'] == 3:
                    sql = '''
                    SELECT
                        count(*) 
                    FROM
                        db_yshu_life.ys_goods_price y
                        LEFT JOIN db_yshu_life.ys_goods g ON y.price_goods_id = g.goods_id 
                    WHERE
                        y.`status` = 2 
                        AND y.is_hide = 0 
                        AND g.goods_type = 1
                        AND y.price_supplier_id != 1
                    '''
                else:
                    sql = '''
                    SELECT
                        count(*) 
                    FROM
                        db_yshu_life.ys_goods_price y
                        LEFT JOIN db_yshu_life.ys_goods g ON y.price_goods_id = g.goods_id 
                    WHERE
                        y.`status` = 2 
                        AND y.is_hide = 0 
                        AND g.goods_type = 9
                    '''
                self.goods_count = self.db.query_db(sql)['count(*)']
                logger.debug('预期商品数量：{}'.format(self.goods_count))
                logger.debug('实际商品数量：{}'.format(res['data']['total']))
                self.assertEqual(self.goods_count, res['data']['total'])
            logger.info('用例执行通过')
            self.result = 'Pass'
        except AssertionError as e:
            logger.error('用例执行失败：{}'.format(e))
            self.result = 'Fail'
            raise e
        # finally:
        #     hd.excel.write('goodsReplaceList',test_info['case_id']+1, 10, self.result)
