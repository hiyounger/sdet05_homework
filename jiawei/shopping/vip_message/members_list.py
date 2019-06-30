#encoding:utf-8
members=[
    {'uid':1,'tel':'13312345678','disc':0.9,'state':"live"},
    {'uid':2,'tel':'13312345679','disc':0.85,'state':"live"},
    {'uid':3,'tel':'13312345670','disc':0.95,'state':"live"}
]

vip_msg=("会员编号   会员电话        享受折扣\n")

for member in members:

    vip_msg+="   %s\t   %s\t    %s\n" % (member['uid'], member['tel'], member['disc'])
print vip_msg