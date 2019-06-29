#encoding:utf-8
members=[
    {'uid':1,'tel':'13312345678','disc':0.9,'state':"live"},
    {'uid':2,'tel':'13312345679','disc':0.85,'state':"live"},
    {'uid':3,'tel':'13312345670','disc':0.95,'state':"live"}
]

def get_mem_four():
    mem_last_four=raw_input("请输入电话号码的后四位数：\n")
    n=list(mem_last_four)
    s=[]
    for member in members:
        tel=member["tel"]
        m=list(tel)
        if m[7:11]==n:
            s.append(member)
    return s

mem_message=get_mem_four()
print mem_message








