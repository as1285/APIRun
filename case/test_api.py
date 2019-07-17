import unittest
import ddt
import os
import requests
import  run
import ddt
from common import readexcel
from common import writeexcel
from conf.send_email import SendEmail


# 获取case.xls路径
curpath = os.path.dirname(os.path.realpath(__file__))
testxlsx = os.path.join(curpath, "case.xls")

# 复制case.xls文件到report下
report_path = os.path.join(os.path.dirname(curpath), "report")
reportxlsx = os.path.join(report_path, "result.xls")
testdata = readexcel.ExcelUtil(testxlsx).dict_data()
@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        writeexcel.copy_excel(testxlsx, reportxlsx) # 复制xlsx

    @ddt.data(*testdata)
    def test_api(self,data):
        if data['run(是否运行接口)']:
            run.RunTest().go_on_run(data['rowNum'])






if __name__ == "__main__":
    unittest.main()
    SendEmail().send_main()