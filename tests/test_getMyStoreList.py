import unittest
import ddt
import json

from jsonpath import jsonpath

from common.requests_handler import visit
from middleware.handler import Handler


hd = Handler()
test_data = hd.excel.read_file('getMyStoreList')
logger = hd.logger

@ddt.ddt
class TestGetMyStoreList(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.L3_token = hd.L3_token['token']

    def setUp(self) -> None:
        self.db = hd.db_class()

    def tearDown(self) -> None:
        self.db.close()

    @ddt.data(*test_data)
    def test_getMyStoreList(self,test_info):
        '''
        获取门店列表
        :param test_info:用例数据
        '''
        # 替换参数化数据

        logger.debug('L3_token:{}'.format(self.L3_token))
        if '#token#' in test_info['headers']:
            test_info['headers'] = test_info['headers'].replace('#token#', self.L3_token)

        headers = json.loads(test_info['headers'])

        logger.info("==================================开始执行第{}条测试用例==================================".format(test_info['case_id']))

        # 访问接口
        res = visit(
            url= hd.yaml['http']['base_url1']+test_info['url'],
            method= test_info['method'],
            headers= headers
        )
        expected = json.loads(test_info['expected'])

        logger.info('预期结果是：{}'.format(expected))
        logger.info('实际结果是：{}'.format(res))

        store_id_list = jsonpath(res,'$..storeId')
        store_id_str = ''
        for i in store_id_list:
            store_id_str += str(i) + ','
        store_id_str = store_id_str.strip(',')

        if res['code'] == 0:
            sql = 'SELECT count(*) from db_yshu_life.ys_local_warehouse where store_id in {}'.format(eval(store_id_str))
            store_count = self.db.query_db(sql)['count(*)']

            try:
                self.assertEqual(store_count, len(store_id_list))
                logger.info('用例执行通过')
                self.result = 'Pass'
            except AssertionError as e :
                logger.error('用例执行失败：{}'.format(e))
                self.result = 'Fail'
                raise e
            finally:
                hd.excel.write('AddGoods',test_info['case_id']+1,9,self.result)
