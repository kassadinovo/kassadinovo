username=input("please input your user name")
if username=="admin":
    password1 = int(input("please insert your password"))
    if password1 == 123456:
        print("验证成功")
    else:
        print("密码错误")
else:
   print("账号错误")

