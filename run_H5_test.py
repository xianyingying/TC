from H5.test_case.models.test_login import TestLogin
import  unittest
import util.HTMLTestReportCN
import time

suite = unittest.TestSuite()
suite.addTest(TestLogin('test_login'))
report_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
filePath ='D:/pythonLearn/tctestpro/H5/report/htmlReport/'+report_time+'.html'
fp = open(filePath,'wb')
runner = util.HTMLTestReportCN.HTMLTestRunner(stream=fp, title='H5自动化测试报告')
runner.run(suite)



