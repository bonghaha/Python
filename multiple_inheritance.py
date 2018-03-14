# Python 에서는 다중상속을 지원하지만, Java 는 지원하지 않는다
class C1(object):
    def c1_m(self):
        print("c1_m")

    def m(self):
        print("C1 m")


class C2(object):
    def c2_m(self):
        print("c2_m")

    def m(self):
        print("C2 m")


class C3(C1, C2):
    pass


c = C3()
c.c1_m()
c.c2_m()
c.m() # C2 class의 메서드m은 실행 안됨.
print(C3.__mro__) # 우선순위 정보. (<class '__main__.C3'>, <class '__main__.C1'>, <class '__main__.C2'>, <class 'object'>)
