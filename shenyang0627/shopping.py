# coding:UTF-8

from members import MemberHelper

user_tel =raw_input("请提供手机号：")
user_disc=MemberHelper.get_member_discount(user_tel)

def get_product_input():
    while True:
      try:
          user_input=raw_input("请输出商品的价格或是Q进行结算：")
          return float(user_input)
      except ValueError:
          if user_input=="Q":
              return "Q"
          print("输入错误，请重新输入")
product_list=[]
while True:
    prod_info = get_product_input()
    if prod_info=="Q":
        break
    else:
        product_list.append(prod_info)

def calculator_payment(prod_list,user_disc):
    payment_list=[]
    total=0
    for i in range(len(prod_list)):
        payment_item=[i+1,product_list[i],product_list[i]*user_disc]
        payment_list.append(payment_item)
        total+=prod_list[i]*user_disc
    return  payment_list,total

pay_list,pay_total=calculator_payment(product_list,user_disc)

def format_out_msg(list,total):
    out_msg="商品ID\t原价\t折后价\n"
    for prod in list:
        out_msg+="%s\t%s\t%s\n"%(prod[0],prod[1],prod[2])
    out_msg+="-------------------\n"
    out_msg+="总价:\t%s"%total
    return  out_msg

output=format_out_msg(pay_list,pay_total)
print output