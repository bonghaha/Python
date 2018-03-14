class C1:
    def m(self):
        return "parent"


class C2(C1):
    # pass # 클레스에 아무내용이 없을때 pass
    def m(self):
        return super().m() + " child"


o = C2()
print(o.m())