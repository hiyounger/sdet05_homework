#-*- encoding:utf-8 -*-

# 会员信息表
huiyuan=[
    {"id":"1","tel":"13512345678","disc":0.8}
]

class huiyuan_help():
    #通过电话号码返回折扣
    @classmethod
    def tel_disc(cls,user_tel):
        for i in huiyuan:
            if i['tel']==user_tel:
                return i['disc']
        return 1.0


# disc1=huiyuan_help.tel_disc('13512345678')
# print disc1
# disc2=huiyuan_help.tel_disc('1111')
# print disc2