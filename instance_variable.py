class Cal(object):
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.__v1 = v1 # 변수 앞에 '__'를 붙이면 외부에서 바로 접근하는 것 불가능.
        if isinstance(v2, int):
            self.v2 = v2

    def getV1(self):
        return self.__v1

    def setV1(self, v1):
        # v1이 int 인스턴스라면
        if isinstance(v1, int):
            self.__v1 = v1

    def add(self):
        return self.__v1 + self.v2

    def subtract(self):
        return self.__v1 - self.v2


c1 = Cal(10, 10)
print(c1.add())
print(c1.subtract())
c1.v2 = 30
print(c1.subtract())

# print(c1.__v1) # __를 붙인 변수는 바로 접근 불가능.
print(c1.v2)

