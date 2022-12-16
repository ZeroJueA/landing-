from base.base_util import BaseUtil
from page.landing_page import *

class Landing(BaseUtil):
    def test_01_click(self):
        """点击'联系我们'"""
        lp = LandingPage(self.driver)
        lp.contact_click()
        bp = BasePage(self.driver)
        bp.switch_window_by_url('https://192.168.1.243/apply?referer=landing_contact')
        bp.wait(3)
        # 断言
        self.assertEqual(lp.get_except_result(),'免费咨询')


if __name__ == '__main__':
    unittest.main()
