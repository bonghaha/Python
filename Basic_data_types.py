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
    print animal
# 출력 "cat", "dog", "monkey", 한 줄에 하나씩 출력.
