import unittest

from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # 使用unittest默认测试用例加载器发现case目录下.py文件
    suite=unittest.defaultTestLoader.discover("../case","*.py")
    # 生成html报告文件
    report_file=open("../report/reports.html","wb")
    # 生成HTMLTestRunner运行器对象
    runner = HTMLTestRunner(stream=report_file,title="landing自动化测试报告",description="报告详情如下：")
    # 通过运行期运行测试用例
    runner.run(suite)