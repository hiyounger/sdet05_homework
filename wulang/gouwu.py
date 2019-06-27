# encoding:utf-8

members = [
    {'id':'1','tel':'13112345678','disc':0.9},
    {'id': '2', 'tel': '13212345678', 'disc': 0.95},
    {'id': '3', 'tel': '13312345678', 'disc': 0.8},
    {'id': '4', 'tel': '13412345678', 'disc': 0.7},
    {'id': '5', 'tel': '13512345678', 'disc': 0.85},
    {'id': '6', 'tel': '13612345678', 'disc': 0.75},
    {'id': '7', 'tel': '13712345678', 'disc': 0.65},
]

def get_member_discount(user_tel):
    for member in members:
        if member['tel'] == user_tel:
            return member['disc']
    return 1.0
user_tel = input("请提供手机号码:")
user_disc = get_member_discount(user_tel)
def get_product_input():
    while True:
        try:
            user_input = input("请输入商品的价格或是Q进行结算:")
            return float(user_input)
        except ValueError:
            if user_input == "Q":
                return "Q"
            print("输入错误，请重新输入:")
product_list = []
while True:

    prod_info = get_product_input()
    if prod_info == "Q":
        break
    else:
        product_list.append(prod_info)


def calculator_payment(prod_list,user_disc):
    payment_list = []
    total = 0
    for i in range(len(prod_list)):
        payment_item = [i+1,prod_list[i],prod_list[i] * user_disc]
        payment_list.append(payment_item)
        total += prod_list[i] * user_disc
    return payment_list,total

pay_list, pay_total = calculator_payment(product_list,user_disc)
print(pay_list)
print(pay_total)

def format_out_msg(list,total):
    out_msg = "商品ID\t原价\t折后价\n"
    for prod in list :
        out_msg +="%s\t%s\t%s\n"%(prod[0],prod[1],prod[2])
    out_msg += "------------\n"
    out_msg += "总价:\t%s"% total
    return out_msg

output = format_out_msg(pay_list,pay_total)
print(output)





