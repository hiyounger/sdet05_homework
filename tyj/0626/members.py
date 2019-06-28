# encoding:utf-8
# 定义会员信息
members=[
    {'id':'1','tel':'131','disc':0.98},
    {'id':'2','tel':'132','disc':0.9},
    {'id':'3','tel':'133','disc':0.8}
]
# 定义会员信息
class membershelp():
    @classmethod
    def member_disc(cls,user_tel):
        for member in members:
            if member['tel'] == user_tel:
                return member['disc']
        return 1.0

