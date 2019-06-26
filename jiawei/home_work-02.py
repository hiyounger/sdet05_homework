#encoding:utf-8
try:
    y=int(input("请输入年份："))
except NameError:
    y="重新输入"
except TypeError:
    y="重新输入"
except SyntaxError:
    y="重新输入"

if y%4==1 or y%4==2 or y%4==3:
    print("%d是普通年份"%y)
elif y=="重新输入":
    print("年份输入错误，请重新输入")
elif y%4==0:
    print("%d是普通闰年"%y)
elif y%400==0:
    print("%d是世纪闰年"%y)
else:
    print("年份输入错误，重新输入！")