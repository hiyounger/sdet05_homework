#encoding:utf-8
members=[
    {'uid':'1','tel':'13419591290','disc':'0.8'}
]
class MemberHelper():
    def get_member_discount(self,user_tel):
        for member in members:
            if member['tel']==user_tel:
                return member['disc']
        return 1.0


user_disc=MemberHelper().get_member_discount('13419591290')
print(user_disc)
user_disc2=MemberHelper().get_member_discount('10086')
print(user_disc2)
