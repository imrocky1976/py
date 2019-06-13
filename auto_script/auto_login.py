# -*- coding:utf-8 -*-

import os
import re
import urllib
import logging
import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

#logging.basicConfig(filename=os.path.expanduser('~/auto_login.log'), format='%(asctime)s %(filename)s %(lineno)d %(levelname)s:%(message)s', level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(filename)s %(lineno)d %(levelname)s:%(message)s', level=logging.DEBUG)
def login(driver):
    logging.info('Begin login...')
    login_url = "http://198.87.119.50/a/mobile/wel.html"
    
    try:
        driver.get(login_url)
        time.sleep(5)
        driver.find_element_by_xpath('//a[@class="ui-link"]').click()
        if WebDriverWait(driver, 30).until(lambda dr: dr.find_element_by_xpath('//input[@id="user"]'), 'Error redirect to login page'):
            driver.find_element_by_xpath('//input[@id="user"]').send_keys(os.environ['AUTO_LOGIN_USERNAME'])
            driver.find_element_by_xpath('//input[@id="passw"]').send_keys(os.environ['AUTO_LOGIN_PASSWORD'])
            driver.find_element_by_css_selector('button.submit_btn').click()  
            if WebDriverWait(driver, 30).until(lambda dr: 'http://198.87.119.50/a/mobile/submit.html' == dr.current_url, 'Login timeout'):
                logging.info("Logged in")
            

    except Exception as e:
        logging.exception(e)
        #driver.save_screenshot('./Exception.png')


if '__main__' == __name__:
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.add_argument('--headless')
    #fireFoxOptions.add_argument('--disable-gpu')
    #fireFoxOptions.add_argument('--no-proxy-server') 
    #p = webdriver.common.proxy.Proxy()
    #p.proxy_type = webdriver.common.proxy.ProxyType.load('DIRECT')
    #fireFoxOptions.proxy = p

    
    fireFoxOptions.set_preference('network.proxy.type', 0)
    driver = webdriver.Firefox(firefox_options=fireFoxOptions)

    while True:
        login(driver)
        time.sleep(120) # 2min

    driver.quit()   #退出驱动


