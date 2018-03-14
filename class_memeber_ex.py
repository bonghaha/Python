class Cs:
    count = 0
    # Cs.count = 0 은 안된다!

    def __init__(self):
        # 객체(인스턴스) 생성 시 count + 1
        Cs.count = Cs.count + 1

    @classmethod
    def getCount(cls):
        return cls.count


i1 = Cs()
i2 = Cs()
print(i2.getCount()) # 2

i3 = Cs()
i4 = Cs()
print(Cs.count) # 4

