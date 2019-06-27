# encoding:utf-8
# 定义会员信息
members=[
    {'id':'1','tel':'131','disc':0.98},
    {'id':'2','tel':'132','disc':0.9},
    {'id':'3','tel':'133','disc':0.8}
]
# 3.主程序
# 1.获取用户手机号，并通过手机号判断是否会员，返回会员折扣
def member_disc(user_tel):
    for member in members:
        if user_tel == member['tel']:
            print member['tel']
            return member['disc']
    return 1.0
def get_product_input():
    while True:
        try:
            user_input = raw_input("请输入商品价格，或输入Q进行结算")
            return float(user_input)
        except ValueError:
            if user_input == "Q":
                return "Q"
            print ("输入有误，请重新输入")
def payment(goods_list,user_disc):
    payment_list=[]
    total = 0
    for i in range(len(goods_list)):
        payment1= [i+1,goods_list[i],goods_list[i]*user_disc]
        payment_list.append(payment1)
        total += goods_list[i]*user_disc
    return payment_list,total
def format_out_msg(list,total):
    out_msg = "商品ID\t原价\t折后价\n"
    for prod in list:
        out_msg += "%s\t%s\t%s\n" % (prod[0], prod[1], prod[2])
    out_msg+= "--------------------\n"
    out_msg+= "总价=\t%s" %total
    return out_msg


user_tel = raw_input('请输入手机号')
user_disc = member_disc(user_tel)
# 2.录入商品信息
goods_list = []
while True:
        prod_info = get_product_input()
        print ('商品价格为：%s'% prod_info)
        if prod_info =="Q":
            break
        else:
            print ('商品已添加至商品清单')
            goods_list.append(prod_info)
print ("商品清单 %s" %goods_list)
# 3.计算商品的结算清单

pay_list,pay_total = payment(goods_list,user_disc)
# 4.格式化输出内容
out_put = format_out_msg(pay_list, pay_total )
print out_put
