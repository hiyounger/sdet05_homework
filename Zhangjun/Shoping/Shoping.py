#encoding:utf-8
members=[{'id':'1','tel':'18812345671','discount':0.95},
{'id':'2','tel':'18812345672','discount':0.9},
{'id':'3','tel':'18812345673','discount':0.85} ]

def vip_tel():
    while True:
        try:
            user_tel = raw_input('请输入你的手机号码:\n')
            return user_tel
        except :
            print ('输入有误，请重新输入')
while True:
    user_tel=vip_tel()
    if len(user_tel)==11:
       break
    else:
        print ('输入有误，请重新输入')

def get_member_discount(user_tel):
    for member in members:
        if member['tel'] == user_tel:
           return  member['discount']
    return 1.0

def get_product_input():
    while True:
        try:
            pro_info = raw_input('请输入你的商品或者Q:\n')
            return float(pro_info)
        except ValueError:
            if pro_info == "Q":
                return "Q"
            print ('输入有误，请重新输入')
user_discount = get_member_discount(user_tel)
product_list=[]
while True:
   pro_info=get_product_input()
   if pro_info == "Q":
       break
   else:
        product_list.append(pro_info)

def caularment_payment(product_list,user_discount):
    payment_list=[]
    total=0
    for i in range(len(product_list)):
        payment_item=[i+1,product_list[i],product_list[i]*user_discount]
        payment_list.append(payment_item)
        total+=product_list[i] * user_discount
    return payment_list,total

pay_list,pay_total = caularment_payment(product_list,user_discount)
print (pay_list)

def format_out_msg(list,total):
    out_msg = "商品\t原价\t折后价\n"
    for i in list:
        out_msg += "%s\t%s\t%s\n"%(i[0],i[1],i[2])
    out_msg += "-----------\n"
    out_msg += "总价：\t%s"%total
    return out_msg
output = format_out_msg(pay_list,pay_total)
print (output)






