
class CommonUtil:
    def is_content(self,str_one,str_two):
        #判断一个字符串是否在另外一个字符串里面
        #str_one 查找的字符串
        #str_two 被查找的字符串
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

