# coding:utf-8
members=[
    {'id':1,'tel':18812345671,'disc':0.98},
    {'id':2,'tel':18812345672,'disc':0.9},
    {'id':3,'tel':18812345673,'disc':0.8}
]
class MenberHelper():
    def member_disc(self,user_tel):
        for member in members:
            if member['tel'] == user_tel:
                return member['disc']
        return 1.0

user_disc=MenberHelper().member_disc(18812345671)
print(user_disc)
user_disc=MenberHelper().member_disc(18812345672)
print(user_disc)
user_disc=MenberHelper().member_disc(18812345673)
print(user_disc)
user_disc=MenberHelper().member_disc(18812345656)
print(user_disc)