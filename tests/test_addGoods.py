import unittest
import ddt
import json
from common.requests_handler import visit
from middleware.handler import Handler


hd = Handler()
test_data = hd.excel.read_file('AddGoods')
logger = hd.logger

@ddt.ddt
class TestAddGoods(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.token = hd.L0_token

    @ddt.data(*test_data)
    def test_addGoods(self,test_info):
        '''
        加入购物车接口
        :param test_info:用例数据
        '''
        # 替换参数化数据
        if '#token#' in test_info['headers']:
            test_info['headers'] = test_info['headers'].replace('#token#',self.token)

        headers = json.loads(test_info['headers'])
        data = json.loads(test_info['data'])

        logger.info("==================================开始执行第{}条测试用例==================================".format(test_info['case_id']))

        # 访问接口
        res = visit(
            url= hd.yaml['http']['base_url2']+test_info['url'],
            method= test_info['method'],
            headers= headers,
            data= data
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
        # finally:
        #     hd.excel.write('AddGoods',test_info['case_id']+1,9,self.result)



