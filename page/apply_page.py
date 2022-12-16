from base.base_page import *
from selenium.webdriver.common.by import By
class ApplyPage(BasePage):
    # 页面元素
    name=(By.XPATH,"//input[@name='cname']")
    phone=(By.XPATH,"//input[@name='phone']")
    company=(By.XPATH,"//input[@name='company']")
    question=(By.XPATH,"//textarea[@id='describe']")
    submit=(By.XPATH,"//div[@class='jgsbbtn']")
    submit_success=(By.XPATH,"//*[contains(text(),'提交成功!')]")
    # 页面动作
    def input_name(self,name):
        self.send_keys(ApplyPage.name,name)
    def input_phone(self,phone):
        self.send_keys(ApplyPage.phone,phone)
    def input_company(self,company):
        self.send_keys(ApplyPage.company,company)
    def input_question(self,question):
        self.send_keys(ApplyPage.question,question)
    def submit_click(self):
        self.click(ApplyPage.submit)
    # 获取文本值断言
    def get_except_result(self):
        return self.get_text(ApplyPage.submit_success)