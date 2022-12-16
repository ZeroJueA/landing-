from ddt import ddt, file_data

from base.base_page import BasePage
from base.base_util import BaseUtil
from page.apply_page import ApplyPage
from page.landing_page import LandingPage

@ddt
class Apply(BaseUtil):
    @file_data('../data/apply.yaml')
    def test_01_apply(self,**args):
        """申请试用"""
        # 点击'联系我们'
        lp = LandingPage(self.driver)
        lp.contact_click()
        bp = BasePage(self.driver)
        bp.switch_window_by_url('https://192.168.1.243/apply?referer=landing_contact')
        bp.wait(3)
        # 提交申请试用
        ap = ApplyPage(self.driver)
        ap.input_name(args['name'])
        ap.input_phone(args['phone'])
        ap.input_company(args['company'])
        ap.input_question(args['question'])
        ap.submit_click()
        bp.wait(5)
        # 断言
        self.assertEqual(ap.get_except_result(),'提交成功!')

if __name__ == '__main__':
    unittest.main()
