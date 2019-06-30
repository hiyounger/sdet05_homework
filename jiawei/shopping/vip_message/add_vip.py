#encoding:utf-8

members=[]
while True:
    mem_info = raw_input('输入T退出会员输入，输入Q继续输入会员信息！\n')
    if mem_info=="T":
        print("退出成功！")
        break
    elif mem_info=="Q":
        members_len=len(members)
        new_mem_tel=raw_input('请输入新增会员电话：')
        new_mem_disc=raw_input('请输入会员折扣信息：')
        members.append({"uid":members_len+1,'tel':new_mem_tel,'disc':new_mem_disc})
        print ("添加会员成功！\n会员编号：%s\n会员电话：%s\n享受折扣：%s"%(members_len+1,new_mem_tel,new_mem_disc))

print members


