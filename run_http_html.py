import os,datetime,time
from common.py_Html import createHtml
from case.test_api import Test_api
from run import RunTest
import os
from common.get_data import GetData
from conf.send_email import SendEmail


'''执行测试的主要文件'''
def start_interface_html_http():
    starttime=datetime.datetime.now()
    day= time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    basdir=os.path.abspath(os.path.dirname(__file__))
    rows_count = GetData().get_case_lines()
    run = RunTest()
    listid = []
    listname = []
    listfangshi = []
    listurl ,listconeent,listqiwang,listrelust,list_exption,list_json=[],[],[],[],[],[]
    for i in range(1,rows_count):
        result = run.go_on_run(i)
        if result:
            listid.append(str(result[0]))
            listname.append(result[1])
            listfangshi.append(result[2])
            listurl.append(result[3])
            listconeent.append(result[4])
            listqiwang.append(result[5])
            if result[5] in result[6]:
                listrelust.append('pass')
            else:
                listrelust.append('fail')
            list_exption.append((result[5]))
            list_json.append(result[6])
    listkey = [i for i in range(80)]
    list_weizhi=1
    list_pass=4
    list_fail=5
    filepath =os.path.join(basdir+'\\report\\result.html')
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    endtime=datetime.datetime.now()
    createHtml(titles=u'http接口自动化测试报告',filepath=filepath,starttime=starttime,
               endtime=endtime,passge=list_pass,fail=list_fail,
               id=listid,name=listname,key=listkey,coneent=listconeent,url=listurl,meth=listfangshi,
               yuqi=listqiwang,json=list_json,relusts=listrelust,weizhi=list_weizhi,exceptions=list_exption)
    SendEmail().send_main()
    # contec = u'http接口自动化测试完成，测试通过:%s,测试失败：%s，异常:%s,未知错误：%s,详情见：%s' % (
    # list_pass, list_fail, list_exption, list_weizhi, filepath)
if __name__ == '__main__':
    start_interface_html_http()