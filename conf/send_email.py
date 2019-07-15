# 结果发邮件
import smtplib
from email.mime.text import MIMEText
import email
from conf.settings import *
from email.mime.multipart import MIMEMultipart
from email.utils import *
from email.header import Header


email.mime.multipart.MIMEMultipart(_subtype='mixed', boundary=None, _subparts=None)


def _format_addr(s):
# 这个函数的作用是把一个标头的用户名编码成utf-8格式的，如果不编码原标头中文用户名，用户名将无法被邮件解码
    name, addr = parseaddr(s)
    return formataddr((Header(name, "utf-8").encode(), addr))
    # Header().encode(splitchars=';, \t', maxlinelen=None, linesep='\n')
        # 功能：编码一个邮件标头，使之变成一个RFC兼容的格式



class SendEmail:
    def __init__(self):
        self.email_host = email_host
        self.send_user = send_user
        self.password = password
        self.user_list = user_list

    def send_email(self, user_list, sub, content):
        user = '唐冬' + '<' + send_user + '>'
        message = MIMEMultipart()
        message['Subject'] = sub
        message['From'] = user
        message['to'] = ';'.join(user_list)
        message.attach(MIMEText(content, 'html', 'utf-8'))
        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open(os.path.join(BASE_PATH,'report/result.html'), 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="result.html"'
        message.attach(att1)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()

    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        print(pass_num)
        count_num = pass_num + fail_num
        pass_result = '%.2f%%' % (pass_num / count_num * 100)
        fail_result = '%.2f%%' % (fail_num / count_num * 100)
        user_list = self.user_list
        # 邮件正文内容
        sub = '这是一封测试邮件'
        content ='此次接口测试个数为%d，通过数为%d,通过率为%s,失败率为%s'%(count_num, pass_num, pass_result, fail_result)
        self.send_email(user_list, sub, content)
