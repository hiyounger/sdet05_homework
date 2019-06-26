# encoding:utf-8
i = int(input("月利润额为:"))
if i <=100000 and i > 0:
    print("奖金可提取：%d"%(i*0.1))
i1 = 10000
elif i > 100000 and  i <= 200000:
    print((i2=("奖金可提取：%d"%((i-100000)*0.075)+i1)))
i3=i1+i2
elif i > 200000 and  i<= 400000:
i4=i3+i2
    print((i4=("奖金可提取：%d"%((i-200000)*0.05)+i3)))
elif i > 400000 and  i<= 600000:
i5=i4+i3
    print((i5("奖金可提取：%d"%(i*0.03)+i4)))
i6=i5+i4
elif i > 600000 and  i<= 1000000:
    print((i6=("奖金可提取：%d"%(i*0.015)))
i7=i6+i5
else:
    i > 1000000
    print((i7=("奖金可提取：%d"%(i*0.001)))


