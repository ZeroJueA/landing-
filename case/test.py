import unittest
from time import sleep

from selenium import webdriver

class Test(unittest.TestCase):
    def test_01(self):
        # 去除浏览器隐私设置
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        # 打开浏览器
        self.driver = webdriver.Chrome(chrome_options=options)
        # 加载网页
        self.driver.get('https://192.168.1.243/landing/')
        # 定位并点击元素'联系我们'
        self.driver.find_element_by_xpath("//a[@class='u-align-left u-btn u-btn-round u-button-style u-custom-color-1 u-radius-6 u-btn-1']").click()
        sleep(3)
        # 获取所有句柄
        handles=self.driver.window_handles
        # 获取最新句柄
        self.driver.switch_to.window((handles[1]))
        sleep(3)
        #获取元素'免费咨询'文本内容
        loc_free = self.driver.find_element_by_xpath("//div[@class='tt']").text
        print(loc_free)
        self.assertEqual(loc_free,'免费咨询')

if __name__ == '__main__':
    unittest.main