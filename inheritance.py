class Class1(object):
    def method1(self):
        return "m1"


# Class1을 상속받는 Class2를 생성.
class Class2(Class1):
    def method2(self):
        return "m2"


c1 = Class1()
c2 = Class2()
print(c1, c1.method1()) # <__main__.Class1 object at 0x0000007EA9F3B1D0> m1
print(c2, c2.method1()) # <__main__.Class2 object at 0x000000B4172CB1D0> m1
print(c2, c2.method2()) # <__main__.Class2 object at 0x000000544096BDD8> m2
print(c2.method2()) # m2
