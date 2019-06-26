# coding:utf-8
a=input('请输入一个年份')
if int(a)>0:
    if int(a)%4==0 or int(a)%400==0:

        if int(a)%400==0  :
            print('%d年是世纪闰年'%a)
        elif int(a)%4==0 and int(a)%100!=0:
            print('%d年是普通闰年'%a)
        else:
            print('%d年不是闰年'%a)
else:
    print('输入错误')


