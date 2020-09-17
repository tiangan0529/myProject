# -*- coding：utf-8 -*-
# @Time   : 2020/6/11 21:42
# @Author : 田干
# @Email  : tiangan_529@163.com
# @File   : mysql_handler.py
import pymysql
from pymysql.cursors import DictCursor


class MysqlHandler:

    def __init__(
            self,
            host=None,
            port=3306,
            user=None,
            password=None,
            database=None,
            charset='utf8',
            cursorclass=DictCursor
         ):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database =database,
            charset=charset,
            cursorclass=cursorclass
        )
        self.cursor = self.conn.cursor()


    def query_db(self,sql,one=True):
        self.conn.commit() # 提交事务
        self.cursor.execute(sql)
        if one :
            return  self.cursor.fetchone()
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
