# 객체의 대소 비교하는 연산
print(1 > 3)
print(2 < 4)
print(6 == 9)
print(6 != 9)

# 복합 관계식 지원
a = 6
print(0 < a and a < 10)
print(0 < a < 10)

# 수치형 이외의 다른 타입의 객체 비교
print("abcd" > "abd")           # False
print((1, 2, 4) < (1, 3, 1))      # True
print([1, 3, 2] > [1, 2, 0])      # True
# print([1, 3, 2] > (1, 2, 0))    TypeError

# 동질성 비교 == (객체의 값 비교), 동일성 비교 is (객체 비교)
a = 10
b = 20
c = a
print(a == b)
print(a is b)
print(a == c)
print(a is c)

# 논리식의 계산순서
print("this")
print([] or 'logical')
print("logical" or "operator")
print("" or "operator")
print("" and "operator")
print(None and 1)
print(None or [])

None or print([])

s = "Hello World"
s = ""
s and print(s)











