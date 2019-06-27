# coding:utf-8
from members import membersHelper
# 定义一种获取会员信息的方法
u_tel=raw_input("请输入用户的手机号：")
u_dscount=membersHelper().get_member_discount(u_tel)
# # 获取用户对商品信息的输入
product_list=[]
def get_product_input():
    while True:
        try:
            user_input=raw_input("请输入商品的价格或是Q进行结算：")
            return float(user_input)

        except ValueError:
            if user_input=="Q":
               return "Q"
while True:
     product_info=get_product_input()
     if product_info=="Q":
        break
     else:
         str(product_info)
         product_list.append(product_info)

 # 依据输入的商品列表，计算商品的结算清单及总价

def calcultor_payment(prod_list,disc):
    total = 0
    pay_list=[]
    for i in range(len(product_list)):
        payment_item=[i+1,product_list[i],product_list[i]*u_dscount]
        pay_list.append(payment_item)
        total+=product_list[i]*u_dscount
    return pay_list,total

pay_list,total=calcultor_payment(product_list,u_dscount)



 # 格式化输出内容
def format_out_msg(list,total):
     out_msg="商品\t原价\t折后价\n"
     for prod in list:
         out_msg+="%s\t%s\t%s\n"%(prod[0],prod[1],prod[2])
     out_msg+="-----------------------\n"
     out_msg+="总价：\t%s"%total
     return out_msg
output=format_out_msg(pay_list,total)
print(output)






