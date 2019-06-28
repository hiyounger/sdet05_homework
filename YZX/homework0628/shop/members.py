#encoding:utf-8
members=[
    {'id':'1','tel':'18845871680','disc':0.9},
    {'id':'2','tel':'18845095099','disc':0.1}
]
class Members():
    @classmethod
    def get_disc_by_tell(cls,tel):
        for member in members:
            if tel == member['tel']:
                print member['disc']
                return member['disc']
        return 1.0
    #新增
    @classmethod
    def add_member_by_tell(cls,tel):
        for mem in members:
            if mem['tel']==tel:
                print ("已注册，注册失败")
                return False
        id=len(members)
        member={'id':id,'tel':tel,'disc':1}
        members.append(member)
        print ('注册成功')
        return 1
add=Members()
add.add_member_by_tell('18845871680')
add.add_member_by_tell('111')


