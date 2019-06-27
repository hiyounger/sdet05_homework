# encoding:utf-8
members=[{'id':'1','tel':'188','disc':'0.9'},
{'id':'2','tel':'187','disc':'0.8'},
{'id':'3','tel':'186','disc':'0.7'}]

class Membershelp():
    def get_member_disc(self,u_tel):
        for member in members:
            if member['tel'] == u_tel:
                return member['disc']
        return 1.0

use_disc=Membershelp().get_member_disc('188')
print(use_disc)
use_disc1=Membershelp().get_member_disc('187')
print(use_disc1)