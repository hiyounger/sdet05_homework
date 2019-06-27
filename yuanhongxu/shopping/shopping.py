#coding:utf-8
from huiyuan import huiyuan_help
from sangping import sangping_caozuo

user_tel=raw_input("请输入你的手机号")
disc=huiyuan_help.tel_disc(user_tel)

spjg_list = []
while True:
    shangpin=sangping_caozuo.sp_spjg()
    if shangpin=="Q":
        break
    else:
        spjg_list.append(shangpin)

price_list,sum_price=sangping_caozuo.jisuan(spjg_list,disc)

out_put=sangping_caozuo.format(price_list,sum_price)
print (out_put)