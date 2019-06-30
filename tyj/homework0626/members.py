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

# 新增
    @classmethod
    def add_new_member(cls,tel):
        for add_new_member_tel in members:
            if add_new_member_tel['tel']==tel:
                print ('会员已存在')
                return False
            add_new_member_id="len(members)+1"
            add_new_member = {'id':add_new_member_id,'tel':add_new_member_tel,'disc':'1'}
            members.append(add_new_member)
            print ("新会员注册成功")
            return 1

# 获取所有会员列表
    @classmethod
    def select_member(cls):
        for member in members:
            print ('会员编号:%s \t 电话:%s \t 折扣:%s'%(member['id'],member['tel'],member['disc']))

#根据手机号的后4位获取会员信息

# 根据手机号注销会员

# 修改会员信息（手机号  折扣）



# 会员可累积购物积分