# -*- coding：utf-8 -*-
# @Time   : 2020/6/9 20:33
# @Author : 田干
# @Email  : tiangan_529@163.com
# @File   : run.py

'''运行所有的用例'''
import os
import unittest
from common.email_handler import send_mail
from libs.HTMLTestRunnerNew import HTMLTestRunner
from config import config
from middleware.handler import Handler
from datetime import datetime
from BeautifulReport import BeautifulReport

logger = Handler().logger
# 加载用例收集器，搜集用例
loader = unittest.TestLoader()
suites = loader.discover(config.CASE_PATH)

# 测试报告的路径
ts = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
reports_filename = 'reports-{}.html'.format(ts)
reports_path = os.path.join(config.REPORTS_PATH, reports_filename)

# with open(reports_path,mode='wb') as f:
#     runner = HTMLTestRunner(
#         f,
#         title='英树项目接口测试报告',
#         description='测试报告',
#         tester='田干'
#     )
#     runner.run(suites)


BeautifulReport(suites).report(
    filename="测试报告",
    description='创建订单接口',
    report_dir=reports_path,
    theme="theme_cyan")

# 发送邮件
logger.debug('=================================开始发送邮件=================================')
mail = send_mail(reports_path,'英树生活')
if mail:
    logger.info('邮件发送成功')
else:
    logger.info('邮件发送失败')

