from selenium import webdriver
from time import sleep
# 定义页面基础类
from selenium.webdriver.support.select import Select

class BasePage(object):
    # 初始化基础类
    def __init__(self,driver):
        self.driver=driver
    # 定位元素
    def locator_element(self,loc):
        return self.driver.find_element(*loc)
    # 输入
    def send_keys(self,loc,text):
        self.locator_element(loc).send_keys(text)
    # 点击
    def click(self,loc):
        self.locator_element(loc).click()
    # 获取标题
    def get_title(self):
        return self.driver.title()
    # 获取文本值进行断言
    def get_text(self,*loc):
        return self.locator_element(*loc).text
    # 等待时间
    def wait(self,time_):
        sleep(time_)
    # 退出浏览器
    def quit(self):
        sleep(3)
        self.driver.quit()
    # 进入框架
    def goto_iframe(self,frame_name):
        self.driver.switch_to.frame(frame_name)
    # 退出框架
    def quit_iframe(self):
        self.driver.switch_to.default_content()
    # 下拉选项
    def down_select(self,loc,value):
        sel=Select(self.locator_element(loc))
        sel.select_by_value(value)
    # 切换句柄
    def switch_window_by_url(self,url):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.current_url.__contains__(url):
                break