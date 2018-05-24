# 2진수, 10진수, 8진수, 16진수 상수(literal)

a = 23
print(type(a))
print(isinstance(a, int))   # isinstance(변수, 자료형)

b = 0b1101
c = 0o23
d = 0x23

print(a, b, c, d)

# 3.x 버전에서는 int와 long이 합쳐졌다. 따라서 표현 범위는 무한대
e = 2**1024
print(type(e))
print(e)
print(e.bit_length()) # bit_length() : 비트 수

# 변환 함수
print(oct(38))  # oct() : 10 -> 8
print(hex(38))  # hex() : 10 -> 16
print(bin(38))  # bin() : 10 -> 2