#encoding:utf-8
members=[
    {'uid':'001','tel':'13419591290','disc':'0.8'}
]
# TODO 定义一个获取会员信息的方法
def get_member_discount(tel):
    # 如果是会员手机号，返回disc
    #如果不是会员手机号，返回1
    disc=0.95
    return disc
# TODO 获取用户的商品信息
demo_counter=0
def get_product_input():
    prod_info=raw_input('请输入商品的价格或者按Q进行结算:')
    global demo_counter
    demo_counter+=1
    if demo_counter ==2:
        return 'Q'
    return 100


# 1.获取用户的手机号，并通过手机号码获取用户的折扣额度
# 获取客户的手机号码
user_tel=raw_input('请提供手机号码：')
# 通过提供的手机号码，获得他可以获得的折扣值
user_disc=get_member_discount(user_tel)

# 2.录入商品的信息
product_list=[]
while True:
    prod_info=get_product_input()