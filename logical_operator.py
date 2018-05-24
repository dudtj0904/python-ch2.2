# 논리 연산자

a = 20
b = 30
print(not a < b)
print(a < b and a != b)
print(a == b or a > b)
# print(a == b || a > b)

# True -> 1 False -> 0
print( True + 1 )
print( (a > b) + 1)

# bool()
print(bool(10), bool(0))
print(bool(3.14), bool(0.))
print(bool("abc"), bool(""))
print(bool([1, 2, 3]), bool([]))
print(bool({"1": 2}), bool({}))
print(bool(None))