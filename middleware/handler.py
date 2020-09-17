# -*- coding：utf-8 -*-
# @Time   : 2020/6/13 10:25
# @Author : 田干
# @Email  : tiangan_529@163.com
# @File   : handler.py
import json
import os,re
from jsonpath import jsonpath
from pymysql.cursors import DictCursor
from common import logging_handler
from common.excel_handler import ExcelHandler
from common.mysql_handler import MysqlHandler
from common.yaml_handler import read_yaml
from config import config
from common.requests_handler import visit


class MysqlHandlerMiddleware(MysqlHandler):
    '''读取配置文件选项，通过 MysqlHandler类'''

    def __init__(self):

        '''从yaml中初始化所有的数据库配置项'''
        db_config = Handler.yaml['mysql']

        #调用父类的中的构造函数
        super().__init__(
            host=db_config['host'],
            port=db_config['port'],
            user=db_config['user'],
            password=db_config['password'],
            #database=db_config['database'],
            charset=db_config['charset'],
            cursorclass=DictCursor
        )


class Handler:
    '''初始化所有的数据，方便调用'''

    # 加载 python 的配置项
    conf = config

    # yaml 数据
    yaml = read_yaml(os.path.join(config.CONFIG_PATH, 'config.yml'))

    # excel 数据
    __excel_path = conf.DATA_PATH
    __excel_file = yaml['excel']['file']
    excel = ExcelHandler(os.path.join(__excel_path, __excel_file))

    # logger
    __logger_config = yaml['logger']
    logger = logging_handler.get_logger(
        name=__logger_config['name'],
        file=os.path.join(config.LOG_PATH, __logger_config['file']),
        logger_level=__logger_config['logger_level'],
        stream_level=__logger_config['stream_level'],
        file_level=__logger_config['file_level']
    )

    '''
    初始化一个存储数据库的类，方便调用，
    每次都是使用新的游标，使用同一个游标会导致查不到数据
    '''
    db_class = MysqlHandlerMiddleware

    @property
    def L0_token(self):
        return self.login(self.yaml['L0_user_info'])['token']

    @property
    def L0_user_id(self):
        return self.login(self.yaml['L0_user_info'])['user_id']

    @property
    def L0_mobile(self):
        return self.login(self.yaml['L3_user_info'])['mobile']

    @property
    def L1_token(self):
        return self.login(self.yaml['L1_user_info'])['token']

    @property
    def L1_user_id(self):
        return self.login(self.yaml['L1_user_info'])['user_id']

    @property
    def L1_mobile(self):
        return self.login(self.yaml['L3_user_info'])['mobile']

    @property
    def L2_token(self):
        return self.login(self.yaml['L2_user_info'])

    @property
    def L2_user_id(self):
        return self.login(self.yaml['L2_user_info'])['user_id']

    @property
    def L2_mobile(self):
        return self.login(self.yaml['L3_user_info'])['mobile']

    @property
    def L3_token(self):
        return self.login(self.yaml['L3_user_info'])

    @property
    def L3_user_id(self):
        return self.login(self.yaml['L3_user_info'])['user_id']

    @property
    def L3_mobile(self):
        return self.login(self.yaml['L3_user_info'])['mobile']

    @property
    def sys_token(self):
        return self.sys_login()


    def login(self, user_info):
        '''
        账号登录，提取用户的token
        :return:
        '''
        res = visit(
            url= self.yaml['http']['base_url1'] + '/member/passwordLogin',
            method= 'post',
            headers= {"appDevice":"1","deviceNumber":"52836374-4aa3-45fd-9291-45386072224e"},
            data= user_info
        )
        token = jsonpath(res,'$..userToken')[0]
        user_id = jsonpath(res,'$..userId')[0]
        mobile = jsonpath(res, '$..mobile')
        member_info = {'token':token, 'user_id':user_id, 'mobile':mobile}
        return member_info


    #
    # def login1(self):
    #     '''
    #     账号登录，提取用户的token
    #     :return:
    #     '''
    #     users = hd.yaml['users']
    #     for user in users:
    #         print(user)
    #         res = visit(
    #             url= self.yaml['http']['base_url1'] + '/member/passwordLogin',
    #             method= 'post',
    #             headers= {"appDevice":"1","deviceNumber":"52836374-4aa3-45fd-9291-45386072224e"},
    #             data= user
    #         )
    #
    #         print(res)
    #
    #         token = jsonpath(res,'$..userToken')[0]
    #         user_id = jsonpath(res,'$..userId')[0]
    #         member_info = {'token':token, 'user_id':user_id}
    #         print(member_info)

    def sys_login(self):
        '''后台登陆'''
        data = {"username": "admin", "password": "a123456"}
        res = visit(
            url= self.yaml['http']['base_url3'] + '/admin/sys/login',
            method= 'post',
            json= data
        )
        sys_token = jsonpath(res,'$..token')[0]
        return sys_token


    def add_coupon(self, phone, coupon_id):
        '''发送优惠券'''
        data = {
                "userMobile": phone,
                "couponId": coupon_id,
                "couponCnt": 1,
                "memo": ""
                }
        res = visit(
            url= self.yaml['http']['base_url3'] + '/admin/userCoupon/addCouponMember',
            method= 'post',
            headers= {'token':self.sys_token},
            json= data
        )

    def replace_data(self,target):
        '''
        替换测试用例中的数据
        '''
        pattern = r'#(.*?)#'
        while re.search(pattern,target):
            key = re.search(pattern,target).group(1)
            value = getattr(self,key,'')
            target = re.sub(pattern,str(value),target,1)
        return target

    # def sendCode(self):
    #     '''获取验证码'''
    #     data = {
    #         'loginUsername':13348974653,
    #         'skey':8,
    #         'yzmCode':3372,
    #         'intlAreaCode':86
    #     }
    #     res = visit(
    #         url= self.yaml['http']['base_url1'] + 'member/sendCode',
    #         method='post',
    #         data=data
    #     )
    #     print(res)

if __name__ == '__main__':
    # data_path = Handler.conf.DATA_PATH
    # yaml_data = Handler.yaml
    # print(yaml_data['excel']['file'])
    # print(Handler.__excel_path)
    # print(Handler.excel)
    # Handler.logger.info('hello')
    # db = MysqlHandlerMid()
    # data = db.query('select * from member limit 10 ')
    # print(data)
    # print(login())
    hd = Handler()





