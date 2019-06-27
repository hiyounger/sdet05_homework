# encoding:utf-8
# 1.数据结构
# 定义会员信息
members=[
    {'id':'1','tel':'131','disc':'0.98'},
    {'id':'2','tel':'132','disc':'0.9'},
    {'id':'3','tel':'133','disc':'0.8'}
]

class membershelp():
    def member_disc(self,user_tel):
        for member in members:
            if member['tel'] == user_tel:
                return member['disc']
        return 1.0

user_disc = membershelp().member_disc('133')
print user_disc