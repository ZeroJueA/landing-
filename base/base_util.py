import unittest
from time import sleep

from selenium import webdriver


class BaseUtil(unittest.TestCase):
    def setUp(self) -> None:
        global driver
        # 去除浏览器隐私设置
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        # 打开浏览器
        self.driver = webdriver.Chrome(chrome_options=options)
        driver = self.driver
        # 加载网页
        self.driver.get('https://192.168.1.243/landing/')

    def tearDown(self) -> None:
        # 退出浏览器
        sleep(3)
        self.driver.quit()