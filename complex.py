# 복소수는 실수부 + 허수부
# 허수부는 j 또는 J를 숫자 뒤에 붙힌다.

a = 4 + 5j
print(type(a))
print(isinstance(a, complex))

# 연산
b = 7 - 2j

print(a + b)
print(b.real, b.imag)   # real : 실수부, imag : 허수부

# complex 객체 함수
p = 2.5
q = 3
print(complex(p, q))    # complex(a, b) : a를 실수부, b를 허수부로 하여 complex 만듬

# 켤레 복소수
print(a.conjugate())    # conjugate() : 켤레 복소수 출력