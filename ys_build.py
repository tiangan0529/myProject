#!/user/bin/python3
# -*- coding: utf-8 -*-
# @Author   : 田干
# @Time     : 2020/7/13 17:32
# @File     : ys_build.py

import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('http://testadmin2.inglemirepharmmall.com/?#/user/login/')
driver.maximize_window()
driver.find_element('id','username').send_keys('admin')
driver.find_element('id','password').send_keys('a123456')
driver.find_element('xpath','//*[@class="ant-form-item-children"]/button').click()
time.sleep(1)


def after_sale():
    '''处理售后订单'''

    # 进入订单中心
    driver.find_element('xpath','//*[@id="root"]/div/section/aside/div/ul/li[4]/div[1]').click()
    ele1 = driver.find_element('xpath','//*[@id="/order$Menu"]/li[2]/div[1]')
    ActionChains(driver).move_to_element(ele1).perform()
    ele1.click()

    # 进入到售后申请单列表
    ele2 = driver.find_element('xpath','//*[@id="/order/afterSaleManage$Menu"]/li[2]/a')
    ActionChains(driver).move_to_element(ele2).perform()
    ele2.click()

    # 点击编辑
    ele3 = '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div/table/tbody/tr[1]/td/a'
    driver.find_element('xpath',ele3).click()

    # 选择生成退款单
    js_code = 'window.scrollTo(0,document.body.scrollHeight);'
    driver.execute_script(js_code)
    time.sleep(0.5)
    xpath = '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div[2]/div/label[2]/span[1]/input'
    driver.find_element('xpath',xpath).click()







if __name__ == '__main__':
    after_sale()


