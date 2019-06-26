#encoding:utf-8


i=float(input("利润:"))
m=float()
if i<=10.0 and i>0:
    print("发放奖金总数：%f万"%(0.1*i))
elif i<=20.0:
    print("发放奖金总数：%f万"%(1+0.075*(i-10)))
elif i<=40.0:
    print("发放奖金总数：%f万"%(1.75+0.05*(i-20)))
elif i<=60.0:
    print("发放奖金总数：%f万"%(2.75+0.03*(i-40)))
elif i<=100:
    print("发放奖金总数：%f万"%(3.35+0.015*(i-60)))
elif i>100:
    print("发放奖金总数：%f万"%(3.95+0.01*(i-100)))



# a=int(input("年份："))
# if a%4==0 and a%100!=0:
#     print("普通闰年")
# elif a%400==0:
#     print("世纪闰年")
# else:
#     print("不是闰年")




