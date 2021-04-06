import time
import datetime
import random

#print(datetime.datetime.now()) #返回 2016-08-19 12:47:03.941925
#print(datetime.date.fromtimestamp(time.time()) )  # 时间戳直接转成日期格式 2016-08-19
# print(datetime.datetime.now() )
# print(datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
# print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
# print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
# print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分



#c_time  = datetime.datetime.now()
#print(c_time.replace(minute=3,hour=2)) #时间替换

#print(time.time())
#print(time.strftime("%Y-%m-%d %H:%M:%S %p %A"))
#print(time.localtime())
print(random.random())# 生成一个0-1之间的数，函数没有参数
print(random.randint(1,10)) #生成指定范围内的随机数
def make_code(n):
    res=''
    for i in range(n):
        s1=chr(random.randint(65,90))
        s2=str(random.randint(0,9))
        res+=random.choice([s1,s2])
    return res

print(make_code(4))
