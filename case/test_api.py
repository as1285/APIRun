import unittest
import ddt
import os
import requests
import  run
from common import readexcel


# 获取demo_api.xlsx路径
curpath = os.path.dirname(os.path.realpath(__file__))
testxlsx = os.path.join(curpath, "case.xls")

# 复制demo_api.xlsx文件到report下
report_path = os.path.join(os.path.dirname(curpath), "report")
reportxlsx = os.path.join(report_path, "result.xls")

testdata = readexcel.ExcelUtil(testxlsx).dict_data()
@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()
        # 如果有登录的话，就在这里先登录了


    @ddt.data(*testdata)
    def test_api(self, data):
        run.RunTest




if __name__ == "__main__":
    unittest.main()