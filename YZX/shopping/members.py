members=[
    {'id':'1','tel':'13312345671','disc':0.98},
    {'id':'2','tel':'13312345672','disc':0.95},
    {'id':'3','tel':'13312345673','disc':0.9},
    {'id':'4','tel':'13312345674','disc':0.8}
]
class MembersHelp():
    def get_member_discount(self,tel):
        for member in members:
            if member['tel']==tel:
                return member['disc']
        return 1.0

user1=MembersHelp().get_member_discount("13312345673")
user2=MembersHelp().get_member_discount('123')
print user1
print user2