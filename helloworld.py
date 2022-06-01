# s="user_name"
# print(s.title().replace("_",""))
# tuple1=("china","sichuan","chengdu","shuangliu","天府新区")
# list1=list(tuple1)
# list1[4]="tianfu"
# tuple1=tuple(list1)
# print(tuple1)
# list1=[1,2,3,4,"hellp","world"]
# for i in list1:
#     print(i)
# dict1={"xiaowang":"小王","laowang":"老王"}
# print(dict1)
# b={}.fromkeys(dict1)
# print(b)
# dict2={"laowang":"老张"}
# print(dict2)
# dict1.update(dict2)
# print(dict1)
# dict1={"admin":123456,"user1":654321,"user2":67890}
# list1=dict1.keys()
# username=input("please input your user name")
# if username in list1:
#  password1 = int(input("please input your password"))
#       for j in dict1.values():
#     if password1 == j:
#         print("验证成功")
#     else:
#         print("密码错误")
# else:
#    print("账号错误")
# list1=dict1.keys()
# print(list1)
# l = [1, 2, 3, 4, 5, "hello"]
# p = (1, 2, 3, 4, 5, "hello")
# q = {1, 2, 3, 4, 5, "hello"}
# print(l)
# print(p)
# print(q)
# a=0
# s=0
# while a<100:
#     s = a + s
#     a=a+1
# print(s)
# for i in range(0, 100, 2):
#     print(i)
# a = 0
# s = 0
# while (a in range(0, 100, 2)) < 100:
#     s = a + s
# print(s)
# 1、求出1 / 1 + 1 / 3 + 1 / 5......+1 / 99的和
# 2、用循环语句，计算2 - 10之间整数的循环相乘的值。
# 3、用for循环打印九九乘法表
# 4、求每个字符串中字符出现的个数如：helloworld
# 5、实现把字符串str = "duoceshi"中任意字母变为大写、在输入函数中输入DCE输出结果为：DuoCEshi
# 6、求出1900 - 2017年的闰年？
# 普通闰年:能被4整除但不能被100整除的年份为普通闰年。（如2004年就是闰年，1999年不是闰年）
# 世纪闰年:能被400整除的为世纪闰年。（如2000年是世纪闰年，1900年不是世纪闰年）
# 7、分别打印100以内的所有偶数和奇数并存入不同的列表当中
# 8、请写一段Python代码用for循环实现对list = [1, 3, 6, 9, 1, 8]里面的元素进行去重 (不能用集合)
# 9、利用for循环把字符串user_controller转换为驼峰命名UserController
# 10、选择排序
# 给一组无规律的数据从大到小或从小到大进行排序如：list = [2, 6, 9, 10, 18, 15, 1]

# 第一题
# a = 1
# b = 1
# s=0
# while b < 100:
#     if b%2==1:
#         s=s+a/b
#     b=b+1
# print(s)

# 第三题
# b=0
# if b <10:
#     b=b+1
#     a=0
#     if a < 10 and a <= b:
#         a = a + 1
#         print(a * b, end="  ")
#         print(b)
#     print("\n")

# 第三题
# for i in range(1,10):
#     for m in range(1,i+1):
#         print(m,'*',i,'=',m*i,end='  ')
#     print('\r')

# 4、求每个字符串中字符出现的个数如：helloworld
# str=input("输串")
# resoult={}
# for i in str:
#     resoult[i]=str.count(i)
# print(resoult)

# s=input("请输入")
# a=list(s)
# b=(len(s))
# for i in range(b):
#     print(a[i],"出现的次数为",a.count(a[i]))

# 5、实现把字符串str = "duoceshi"中任意字母变为大写、在输入函数中输入DCE输出结果为：DuoCEshi
# a = input("输入串")
# b = list(a)
# c = input("变大的字母")
# h = list(c)
# d = len(a)
# e = len(c)
# g = a.upper()
# for i in range(d):
#     for j in range(e):
#         if b[i] == h[j]:
#             b[i] = g[i]
# print("".join(b))

# 6、求出1900 - 2017年的闰年？
# 普通闰年:能被4整除但不能被100整除的年份为普通闰年。（如2004年就是闰年，1999年不是闰年）
# 世纪闰年:能被400整除的为世纪闰年。（如2000年是世纪闰年，1900年不是世纪闰年）

# for i in range(1900,2018):
#     if i%4==0 and i%100!=0 and i%400!=0:
#         print(i,"是闰年")
#     elif i%400==0:
#         print(i,"世纪闰年")


# 7、分别打印100以内的所有偶数和奇数并存入不同的列表当中
# a = []
# b = []
# for i in range(99):
#     i = i + 1
#     if i % 2 == 0:
#         a.append(i)
#     else:
#         b.append(i)
# print("偶数串", a)
# print("奇数串", b)

# 8、请写一段Python代码用for循环实现对list = [1, 3, 6, 9, 1, 8]里面的元素进行去重 (不能用集合)
# a = [1, 3, 6, 9, 1,1,1, 8]
# b = len(a)
# for i in range(b):
#     if a.count(a[i]) > 1:
#         print(i)
# print(a)

# a = [1, 2, 2, 4, 4, 6, 7,7,7,7,7,7,7,7]
# b = list()
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

# s=input("请输入")
# a=list(s)
# b=(len(s))
# for i in range(b):
#     print(a[i],"出现的次数为",a.count(a[i]))

# a = [1, 3, 6, 9, 6, 8]
# b = len(a)
# for i in range(b):
#     for j in range(i + 1, b):
#         if a[i] == a[j]:
#             c = i
# del a[c]
# print(a)

# 9、利用for循环把字符串user_controller转换为驼峰命名UserController


# 10、选择排序
# 给一组无规律的数据从大到小或从小到大进行排序如：list = [9, 6, 7, 10, 18, 15, 1]
# for i in range(5):
#     print("hello world")

# import random;
# random. randint(1,99)
# while int(input('Press 1 to roll the dice or 0 to exit:\n')): print( random. randint(1,99))
# 1
# a = input("输入串,用空格隔开")
# b = a.split(" ")
# d = len(b)
# c = a.split(" ")
# print("你的串是", b)
# for e in range(d):
#     if e + 1 < d:
#         for h in range(e + 1, d):
#             if b[e] < b[h]:
#                 c[e] = b[h]
#         if c[e] < b[h-1]:
#             c[e] = b[h]
# print(c)
# c=[1,2]
# c[1]=3
# print(c)
#


# if c.append(b[d])<c.append(b[e]):
#     c.append(b[d])=c.append(b[e])
#

# a = input("输入串,用空格隔开")
# ss = a.split(" ")
# def s(ss):
#     for i in range(1, len(ss)):
#         for j in range(0, len(ss) - i):
#             if ss[j] > ss[j + 1]:
#                 ss[j], ss[j + 1] = ss[j + 1], ss[j]
#     return ss
#
#
# # if __name__ == '__main__':
# a = input("输入串,用,隔开")
# ss = a.split(",")
# # ss = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
# print(s(ss))
# def ave(total):
#     a = total / 6
#     if a > 90:
#         print("优秀学生")
#     elif 80 <= a <= 90:
#         print("良好学生")
#     else:
#         print("同志还需努力")
# s=int(input("好多分"))
# ave(s)

# 12、分析以下数字的规律， 1 1 2 3 5 8 13 21 34用Python语言编程实现输出。  （斐波那契数列）
# def c(f):
#     for e in range(2, f):
#         a.append(a[e - 1] + a[e - 2])
# a = [1, 1]
# d = int((input("大于两个的数列")))
# c(d)
# print(a)


# 13、先定义一个字典来存放用户名和密码如dic = {'admin': '123456', 'dcs46': '654321'}
# 要求如下：
# 1）、从字典中获取用户完成登入，登入时判断用户是否存在
# 存在直接登入
# 2）、如果输入的登入用户判断不存在字典，则调用注册方法，完成该用户的注册，注册成功后写入字典
# 定义登录函数

# def b(e):
#     f = dict(e)
#     c.setdefault(f)
#
#
# def a(s):
#     if s in dict1.keys():  # dictI.__ contains_ (username)
#         password = int(input("请输入您的密码:"))
#         if password == dict1[s]:
#             print("登成功")
#         else:
#             print("密码错")
#     else:
#         print("账号不存在请注册")
#         e = input("请输入你的账号密码完成注册,用空格隔开")
#         b(e)
#
#
# c = {}
# s = input("账号")
# dict1 = {"admin": 123456, "user1": 654321, "user2": 67890}
# a(s)

# 14、用字符串aabbcdbaaabc，用你熟悉的语言实现去除"ab"子串

# def d(b):
#     for e in range(c):
#         x.append(b[e])
#         if a[e]==a and a[e+1]==b:
# a = input("输入串")
# b = list(a.split("ab"))
# print("去ab子串后的串", "".join(b))

# 15、水仙花数：一个三位数，其按位立方之和等于该数本身，该数称为水仙花数。求出100 - 1000之间的水仙花数。
# 其实，水仙花数是“自幂数”中的一种；自幂数：一个n位数，其按位数字的n次方之和，等于该数本身。
# 百位数的立方+十位数的立方+个位数的立方=这个数本身  ==》 水仙花数
# for i in range(100, 1000):
#     a = int(i / 100)
#     b = int(i / 10)
#     c = int(i % 10)
#     d = int(b % 10)
#     if a ** 3 + c ** 3 + d ** 3 == i:
#         print(i)

# 16、用递归的方法求出n的阶乘？4的阶乘结果为?   （ 递归： 自己调用自己）   4 ==》 4*3*2*1


# 17、有如下url地址, 要求实现截取出"?"号后面的参数, 并将参数以"key value"的键值形式保存起来, 并最终通过#get(key)的方式取出对应的value值。
# url地址如下：-


# 18、存在一个文件, 文件名test.txt
# 内容如下：
# 01 success
# 02 fail
# 03 fail
# 04 success
# ....请使用Python语言编写程序实现统计该文件中
# 有多少个success
# 多少个fail的功能？


# 19、一个txt文件中已知数据为：
# C4D
# C4D/maya
# C4D
# C4D/su
# C4D/max/AE
# 统计每个字段出现的次数，比如C4D,maya,su,max,AE 请用最熟悉的语言或者伪代码实
# 现该需求


# 20、统计一个文件的行数，以e:\\write.txt文件为例(内容自己建)
# import  hashlib
# hashlib.md5()
# md5=hashlib.md5()
# md5.update("i love you".encode("utf-8"))
# print(md5.hexdigest())


# 用random模块生成手机号码   （）   不能用random.randint(x,y)函数
# import random
#
# a = [1]
# for i in range(1, 11):
#     a.append(random.randint(10))
# # print("".join(a))
# print("".join(map(str, a)))


# 2. 用random模块生成六位数的验证码（大小写字符+数字）
# import hashlib
# import random
# import string
# a = []
# d = int(input("几位验证码"))
# for i in range(d):
#     b = random.randint(0, 2)
#     if b == 0:
#         a.append(random.randint(0, 9))
#     elif b == 1:
#         c = list(string.ascii_lowercase)
#         x = random.randint(0,25)
#         a.append(c[x])
#     elif b == 2:
#         e = list(string.ascii_uppercase)
#         y = random.randint(0, 25)
#         a.append(e[y])
# print("".join(map(str, a)))

# 3. 将生成验证码通过md5加密，输出16进制32位字符串
# import random
# import string
import hashlib
# a = []
# d = int(input("几位验证码"))
# for i in range(d):
#     b = random.randint(0, 2)
#     if b == 0:
#         a.append(random.randint(0, 9))
#     elif b == 1:
#         c = list(string.ascii_lowercase)
#         x = random.randint(0, 25)
#         a.append(c[x])
#     elif b == 2:
#         e = list(string.ascii_uppercase)
#         y = random.randint(0, 25)
#         a.append(e[y])
# print("您的验证码是", "".join(map(str, a)))
# u = str("".join(map(str, a)))
# w = hashlib.md5()
# w.update("我爱你".encode())
# print("md5加密：", w.hexdigest())
# print("md5解密网站：https://www.cmd5.com/")

# a="dasda"
# b="gas"
# c=a+b
# print(c)
#

# 21、使用os模块写一个递归调用打印出e:\\home下的所有文件名的绝对路径？
# import os
#
# print(os.listdir(r'H:\kassadinovo\venv'))


# 22、用正则方法实现统计e:\\python文件中指定字符如"python"的行数?（文件中的python字符）
# 假设里面的数据为：
# pythonelloerrorpythonpythonpython
# warnipythonngerror
# warning
# errorwapythonrning

# 23、使用正则完成市面上手机规则的编写、随机生成11位数然后通过正则匹配出
# 符合规则的11位数手机号码？（手机号：11位）

# 24、用正则实现写一段代码统计e:\\log文件中error和warning单词出现的次数分别为几次?
# 文件内容如下：
# warningabchelloerrorwarningwarning
# warningerror
# warning
# errorwarningwarning


#
# 25、
# str1='{"name":"xiaowang","age":"18岁"}'
# # 要求从从str1中，匹配出每一个值： "xiaowang" 和"18岁"
# import random
#
# import string
#
# import re

# J defget_ phone():
# while True:
# str1=string. digits
# str2="
# for i in range(11):
# str2=str2+random. choice(str1) #以上都是在生成11位的数字
# # print(str2)
# a=re. findal1l("^1[3-9]\d{9}",str2) # 用手机号的规则去匹配生成的内容
#
# # print(a)
# if len(a)!=0:
# print(a[0])
# break
# get_phone()
# n = 11

#
# def phone(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
import xlrd
book = xlrd.open_workbook(r"H:\kassadinovo\evo\工作簿.xls")
sheet = book.sheet_by_name('Sheet1')
a = sheet.cell_value(0, 1)
print(a)
b = sheet.row_values(4, 1)
print(b)
c = sheet.nrows
print(c)
d = sheet.ncols
print(d)
a=[]
for i in range(1, c):
    for j in range(d):
        a.append(sheet.cell_value(i, j))
    print(a)
