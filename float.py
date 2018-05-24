
a = 1.2
print(type(a))
print(isinstance(a, float)) # isinstance(변수, 자료형)

# 값으로 정수인지 실수인지 확인하는 객체 함수
# 타입을 확인하는 함수가 아니다.
b = 2.0
print(type(b))
print(b.is_integer())       # is_insteger() : 실수 타입 객체의 값이 정수인지 판별

# 다른 언어처럼 소수점 이나 e, E로 지수 표현 가능
b = 3e3
c = -0.2e-4
print(a, b, c)


