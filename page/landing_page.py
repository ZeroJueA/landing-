from base.base_page import *
from selenium.webdriver.common.by import By
from selenium import webdriver
class LandingPage(BasePage):
     # 定位元素
     contact=(By.XPATH,"//a[@class='u-align-left u-btn u-btn-round u-button-style u-custom-color-1 u-radius-6 u-btn-1']")
     free=(By.XPATH,"//div[@class='tt']")
     # 基于元素操作行为
     def contact_click(self):
          self.click(LandingPage.contact)
     # 获取文本内容
     def get_except_result(self):
          return self.get_text(LandingPage.free)