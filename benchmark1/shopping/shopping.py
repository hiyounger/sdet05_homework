# -*- encoding:utf-8 -*-

from members import MemberHelper
from client import SalesClient

def saling():
    #1. 获取用户手机号，并通过手机号码获取用户的折扣额度
    user_tel = raw_input("请提供手机号:")
    user_disc = MemberHelper.get_memeber_discount(user_tel)

    # #2. 录入商品信息
    product_list = []
    while True:
        prod_info = SalesClient.get_product_input()
        if prod_info == "Q":
            break
        else:
            product_list.append(prod_info)
    #3. 计算商品的结算清单
    pay_list, pay_total = SalesClient.calculator_payment(product_list, user_disc)
    #4. 格式化输出内容
    output = SalesClient.format_out_msg(pay_list, pay_total)
    # #5. 输出
    print(output)
if __name__ == '__main__':
    saling()




