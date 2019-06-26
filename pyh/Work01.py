#encoding:utf-8
i=int(input("请输入年份:"))
if i%4==0 and i%100!=0 :
    print("%d是闰年"%(i))
elif i%400==0 :
    print ("%d是世纪闰年"%(i))
else:
    print ("%d不是闰年"%(i))