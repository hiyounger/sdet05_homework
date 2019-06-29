#encoding:utf-8
product_list=[]
def get_product_input(cls):
    while True:
        try:
            user_input = raw_input('请输入商品的价格或是Q结束：\n')
            return float(user_input)
        except:
            if user_input == "Q":
                return 'Q'
            print('输入错误，请重新输入')


while True:
    prod_info = get_product_input()
    if prod_info == "Q":
        break
    else:
        product_list.append(prod_info)