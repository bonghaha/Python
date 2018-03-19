# 기본 자료형

# Numbers(Integers, floats)
x = 3
print(type(x))  # <class 'int'>
print(x)  # 3
print(x + 1)  # 덧셈 : 4
print(x - 1)  # 뺄셈 : 2
print(x * 2)  # 곱셈 : 6
print(x ** 2)  # 제곱 : 9
x += 1
print(x)  # 4
x *= 2
print(x)  # 8
y = 2.5
print(type(y))  # <class 'float'>
print(y, y + 1, y * 2, y ** 3)  # 2.5 3.5 5.0 15.625
# 증감 단항연산자(x++, x--)가 없다.

# 불리언(Booleans)
# 기호(&&, || 등) 대신 영어 단어로 구현되어 있다.
t = True
f = False
print(type(t))  # <class 'bool'>
print(t and f)  # False
print(t or f)  # True
print(not t)  # False
print(t != f)  # True

# 문자열(Strings)
hello = 'hello'  # 따음표나 쌍따음표나 상관 없다.
world = "world"
print(hello, world)  # hello world
print(len(hello))  # 5
hw = hello + ' ' + world  # 문자열 연결
print(hw)  # hello world
hw12 = '%s %s %d' % (hello, world, 12)  # sprintf 방식의 문자열 서식 지정
print(hw12)  # hello world 12

s = 'hello'
print(s.capitalize())  # 문자열을 대문자로 시작 : "Hello"
print(s.upper())  # 모든 문자 대문자 : "HELLO"
print(s.rjust(7))  # 문자열 오른쪽 정렬, 빈공간은 여백으로 채움 : "  hello"
print(s.center(7))  # 문자열 가운데 정렬, 빈공간은 여백으로 채움 : " hello "
print(s.replace('l', '(ell)'))  # 첫 번째 인자를 두 번째 인자로 바꿈 : he(ell)(ell)o"
print('  world'.strip())  # 문자열 앞뒤 공백 제거 : "world"

# 컨테이너(Containers)
# list, dictionaries, sets, and tuples

# 리스트(Lists)
# 배열같은 존재. 그렇지만 배열과 달리 크기 변경 가능하고 서로 다른 자료형일지라도 하나의 리스트에 저장될 수 있다.
xs = [3, 1, 2]  # 리스트 생성
print(xs, xs[2])  # [3, 1, 2] 2
print(xs[-1])  # 인덱스 음수일 경우 리스트의 끝에서부터 카운트 : 2
xs[2] = 'foo'  # 리스트는 자료형이 다른 요소들을 저장할 수 있다.
print(xs)  # [3, 1, 'foo']
xs.append('bar')  # 리스트의 끝에 새 요소 추가
print(xs)  # [3, 1, 'foo', 'bar']
x = xs.pop()  # 리스트의 마지막 요소 제거하고 반환
print(x, xs)  # bar [3, 1, 'foo']

# 슬라이싱(Slicing)
nums = range(5)  # 정수들로 구성된 리스트 생성
print(nums)  # range(0, 5)  # [0, 1, 2, 3, 4]
print(nums[2:3])  # range(2, 3)  # [2]
# print(type(nums[2:3]))
print(nums[2:4])  # range(2, 4)  # [2, 3]
print(nums[2:])  # range(2, 5)  # [2, 3, 4]
print(nums[:2])  # range(0, 2)  # [0, 1]
print(nums[:])  # range(0, 5)  # [0, 1, 2, 3, 4]
print(nums[:-1])  # range(0, 4) # [0, 1, 2, 3]
# nums[2:4] = [8, 9]  # range 에는 특정한 값을 할당할 수 없다.
# http://cs231n.github.io/python-numpy-tutorial/ 에서 잘못 됨.

# 반복문(Loop)
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
# 출력 "cat", "dog", "monkey", 한 줄에 하나씩 출력.

animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
# Prints "#1: cat", "#2: dog", "#3: monkey", each on its own line

# 리스트 comprehensions
num = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)  # [0, 1, 4, 9, 16]

# 리스트 comprehensions를 이용해서 위의 코드를 간단하게 만들 수 있다.
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)  # [0, 1, 4, 9 ,16]

# 리스트 comprehensions에 조건 추가도 할 수 있다.
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)  # [0, 4, 16]

# 딕셔너리(dictionary) (키, 값)
d = {'cat' : 'cute', 'dog' : 'furry'}  # dictionary 생성
print(d['cat'])  # cute
print('cat' in d)  # True
d['fish'] = 'wet'
print(d['fish'])  # wet
print(d.get('monkey', 'N/A'))  # dictionary의 값을 받음. 존재하지 않는다면 'N/A'; 출력 : 'N/A'
del d['fish']  # dictionary에 저장된 요소 삭제
print(d.get('fish', 'N/A'))  # 'N/A'

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
    print('A %s has %d legs' % (animal, legs))
# A person has 2 legs
# A cat has 4 legs
# A spider has 8 legs

# 딕셔너리 comprehensions를 이용해 손쉽게 딕셔너리를 만들 수 있다.
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)  # {0: 0, 2: 4, 4: 16}

# sets : 순서 구분이 없고 서로 다른 요소 간의 모임.
animals = {'cat', 'dog'}
print('cat' in animals)  # True
print('fish' in animal)  # False
animals.add('fish')  # 요소를 set에 추가
print(len(animals))  # 집합에 포함된 요소의 수; 3
animals.add('cat')  # 이미 포함되어 있는 요소를 추가할 경우 아무 변화 없음
animals.remove('cat')  # 요소 cat을 집합에서 삭제
print(len(animals))  # 2
animals.add('cat')
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
# set은 순서가 없어서 어떤 순서로 출력될지 추측할 수 없다.

# set comprehensions
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}  # 30미만의 수 중 모든 제곱근
print(nums)  # {0, 1, 2, 3, 4, 5}
print(type(nums))  # <class 'set'>

# tuple : 요소 간 순서 있으며 값이 변하지 않는 리스트.
# tuple은 dictionary의 키와 set의 요소가 될 수 있지만, 리스트는 불가능하다.
d = {(x, x + 1): x for x in range(10)}  # tuple을 key로 하는 dictionary 생성.
print(d)  # {(0, 1): 0, (1, 2): 1, (2, 3): 2, (3, 4): 3, (4, 5): 4, (5, 6): 5, (6, 7): 6, (7, 8): 7, (8, 9): 8, (9, 10): 9}
print(type(d))  # <class 'dict'>
t = (5, 6)
print(type(t))  # <class 'tuple'>
print(d[t])  # 5
print(d[(1, 2)])  # 1


# 함수
def hello(name, loud=False):
    if loud:
        print('HELLO, %s!' % name.upper())
    else:
        print('Hello, %s' % name)


hello('Bob')  # "Hello, Bob"
hello('Fred', loud=True)  # "HELLO, FRED!"


# class
class Greeter(object):
    # 생성자
    def __init__(self, name):
        self.name = name  # 인스턴스 변수 선언

    # 인스턴스 메서드
    def greet(self, loud=False):
        if loud:
            print('HELLO, %s!' % self.name.upper())
        else:
            print('Hello, %s' % self.name)


g = Greeter('Fred')  # Greeter 클래스의 인스턴스 생성
g.greet()  # "Hello, Fred"
g.greet(loud=True)  # "HELLO, FRED!"


