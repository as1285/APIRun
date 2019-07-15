#查看数据库，后期扩展重点，数据来源
from conf.settings import *
import pymysql

class MySQLOperate():
    '''
        mysql执行器
    '''
    def __init__(self,DB):

        self.db = pymysql.Connect(
            host=DB_IP,
            user=DB_NAME,
            password=DB_PASSWORD,
            database=DB,
            port=PORT
        )

    def execute_sql(self,sql):
        '''
        执行sql
        :param sql: 增删改查
        :return:
        '''
        cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)#取数据库表的字段
        result = cursor.execute(sql)
        if sql.lower().startswith("select"):
            return cursor.fetchone()#从结果中取第一条数据
        else:
            self.db.commit()
            return result



if __name__ == '__main__':
    print(MySQLOperate("retail_uc").execute_sql("select * from member_info where mobile=13267166832" ))