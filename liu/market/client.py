#encording:utf-8
u_disc=get_member_disc(u_tel)
def get_prod_input():
    while True:
        try:
            user_input=raw_input('请输入商品的价格或者Q进行结算：')
            return float(user_input)
        except ValueError:
            if user_input=="Q":
                return"Q"
        print('输入有误，重新输入')
prod_list=[]
while True:
    prod_info=get_prod_input()
    print('[DEBUG]:%s'%prod_info)
    if prod_info=="Q":
        break
    else:
        prod_list.append(prod_info)

# #3.计算商品账单
def calculator_payment(prod_list,u_disc):
    pay_list=[]
    total=0
    for i in range(len(prod_list)):
        pay_item=[i,prod_list[i],prod_list[i]*u_disc]
        pay_list.append(pay_item)
        total+=prod_list[i]*u_disc
    return pay_list,total
pay_list,total=calculator_payment(prod_list,u_disc)
print(pay_list)
print(total)
# #4.格式化输出内容
def format_out_msg(pay_list,total):
    out_msg='商品ID\t原价\t折后价\n'
    for prod in pay_list:
        out_msg+="%s\t%s\t%s\n"%(prod[0],prod[1],prod[2])
    out_msg += "------------------\n"
    out_msg +="总价:\t%s'"%total
    return out_msg
output=format_out_msg(pay_list,total)
print(output)



from members import memberselp
from client import Saling
def Sale():

  while True:
      user_tel=membershelp.vip_tel()
      if len(user_tel)==11:
          break
      else:
          print ('输入有误，请重新输入')

  user_discount = MembersHelp.get_member_discount(user_tel)

  product_list=[]

  while True:
     pro_info=Saling.get_product_input()
     if pro_info == "Q":
         break
     else:
         product_list.append(pro_info)

  pay_list,pay_total = Saling.caularment_payment(product_list,user_discount)

  print (pay_list)

  output = Saling.format_out_msg(pay_list,pay_total)

  print (output)

if __name__ =='__main__':
   Sale()