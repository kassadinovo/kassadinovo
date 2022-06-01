# import random
# from fractions import Fraction
# operation = ['+', '-', '*', '/'] #四则运算的符号
# global f
# def integer_score():
# #rand = operation[random.randint(0,3)]
# number = random.randint(1,4) #随机产⽣的表达式长度
# f = ''
# for i in range(number):
# a = random.randint(1,20) #随机产⽣的表达式中的数
# rand = operation[random.randint(0, 3)] #随机选择⼀个四则运算中的符号
# if rand == '/':
# b = random.randint(a, 20) #随机产⽣的真分数的分母
# f += str(a) + rand + str(b) #数与符号相连
# rand = operation[random.randint(0, 2)] #随机选择⼀个四则运算中的符号
# f += rand
# else:
# f += str(a) + rand
# #print(a,rand,end='')
# b = random.randint(1, 20)
# f += str(b) #得到完整的表达式
# n = eval(f) #得到表达式的结果
# n = Fraction('{}'.format(n)).limit_denominator() #⼩数转化为分数
# if n > 0:
# print('题⽬：')
# print(f,'=')
# print('请输出答案：')
# x = Fraction('{}'.format(eval(input()))).limit_denominator()
# if n == x: #输⼊的数与表达式⽐较
# print(True)
# else:
# print(False)
# s=input("a+b")
# print("s")
#
from tkinter import *
import random


def main():
    a = random.randint(1, 18)
    if a < 10:
        b = random.randint(10 - a, 9)
        c = a + b
        result = "%d  +  %d" % (a, b)
        return (result, c)
    if a >= 10:
        b = random.randint(a - 9, 9)
        c = a - b
        result = "%d  -  %d" % (a, b)
        return (result, c)


def check():
    if int(result.get()) == int(t[1]):
        h = "恭喜你！回答正确"
        hint.set(h)

    else:
        h = "抱歉！回答错误！"
        hint.set(h)
        result.set('')


def next():
    global t
    t = main()
    e.set(t[0])
    result.set('')
    hint.set('')


master = Tk()
master.geometry('500x500+100+100')
master.title("20以内加减进退位运算")
Label(master, text="题目").grid(row=0)
Label(master, text="答案").grid(row=1)
Label(master, text="信息").grid(row=4)
e = StringVar()
result = StringVar()
hint = StringVar()
e1 = Entry(master, textvariable=e)
e2 = Entry(master, textvariable=result)
e3 = Entry(master, textvariable=hint)
t = main()
e.set(t[0])
result.get()

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=4, column=1)

btn = Button(master, text='确定', command=check)
btn2 = Button(master, text='下一题', command=next)
btn.grid(row=2, column=2)
btn2.grid(row=2, column=4)

master.mainloop()

