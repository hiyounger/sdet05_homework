# coding:UTF-8

members=[
    {'uid':'1','tel':'13912345671','disc':0.8},
    {'uid':'2','tel':'13912345672','disc':0.9},
    {'uid':'3','tel':'13912345673','disc':0.95},
    {'uid':'4','tel':'13912345674','disc':0.98}
]

class MemberHelper():
    @classmethod
    def get_member_discount(self,user_tel):
         for member in members:
            if member["tel"] == user_tel:
                return member["disc"]
            return 1.0

user_disc=MemberHelper().get_member_discount("13912345671")
print(user_disc)
user_disc2=MemberHelper()
print(user_disc2.memberinfo)