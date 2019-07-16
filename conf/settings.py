import os
# 获取项目路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 定义测试用例的路径
TESTCASE_PATH =  os.path.join(BASE_PATH,'case/case.xls')
# 定义测报告的路径
REPORT_PATH =  os.path.join(BASE_PATH,'report/')
# 定义日志文件的路径
LOG_PATH = os.path.join(BASE_PATH,'logs/logs.txt')

# mysql数据库的连接信息  QA002数据库
DB_NAME = 'app_retail_rw'
DB_PASSWORD = 'l6i6pzLMSqbm7WRLoSRo'
DB_IP = '39.108.4.250'
PORT = 29383

#新零售APP登录
app_phone = '13430664102'
app_host = 'https://rtapi-qa002.blissmall.net/'

#微商城登录
wei_phone='11111111111'
wei_host = 'https://rtapi-qa002.blissmall.net/'

#骑手app
rider_phone='13267166832'
rider_host = 'https://retailadmin-qa002.blissmall.net/'
#电商云后台登录
cloud_host = 'https://retailadmin-qa002.blissmall.net/'

#发送邮件配置
email_host = 'smtp.qq.com'
send_user = '498771018@qq.com'
password = 'ikcwnwolsdzjbicf'#邮箱的smtp验证码,不是 邮箱密码
user_list = ['dong1285@126.com']#收件人列表，后面用;隔开

