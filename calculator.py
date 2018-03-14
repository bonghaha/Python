class Cal(object):
    _history = []

    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2

    def add(self):
        result = self.v1 + self.v2
        # Cal._history.append("add : " + str(self.v1) + " + " + str(self.v2) + " = " + str(result)) # 햇갈려서 아래와 같이 바꿈.
        # 문자열에 숫자(int) 추가 하고 싶으면 %d
        Cal._history.append("add : %d + %d = %d" % (self.v1, self.v2, result))
        return result

    def subtract(self):
        result = self.v1 - self.v2
        Cal._history.append("subtract : %d - %d = %d" % (self.v1, self.v2, result))
        return result

    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v

    def getV1(self):
        return self.v1

    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)


class CalMultiply(Cal):
    def multiply(self):
        result = self.v1 * self.v2
        Cal._history.append("multiply : %d * %d = %d" % (self.v1, self.v2, result))
        return result


class CalDivide(CalMultiply):
    def divide(self):
        result = self.v1 / self.v2
        Cal._history.append("divide : %d / %d = %d" % (self.v1, self.v2, result))
        return result


c1 = CalMultiply(10, 10)
print(c1.add())
print(c1.multiply())
print(c1.subtract())
c2 = CalDivide(20, 10)
print(c2, c2.add())
print(c2, c2.multiply())
print(c2, c2.divide())
Cal.history()