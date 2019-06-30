#encoding:utf-8
members=[
    {'uid':1,'tel':'13312345678','disc':0.9,'state':"live"},
    {'uid':2,'tel':'13312345679','disc':0.85,'state':"live"},
    {'uid':3,'tel':'13312345670','disc':0.95,'state':"live"}
]
mem_tel_cancel=raw_input('请输入要注销的会员手机号：')
for member in members:
    if mem_tel_cancel==member['tel']:
       member['state']='die'

    print member

# 修改会员信息
for member in members:
    if mem_tel_cancel!=member['tel']:
        print("您还不是会员！")
