# 한 줄 문자열 정의
s = ''
str1 = 'hello world'
str2 = "hello world"
print(type(s), type(str1), type(str2))
print(isinstance(str2, str))

# 여러 줄 문자열 정의
str3 = """ABC
DEF
가나다라마
바사아자차
"""
print(str3)

# 여러 줄 주석 : 여러 줄 문자열 사용
"""
여러 줄 주석:
여러 줄 문자열 사용
"""
###########################################################
# escape
print("Hello\nWorld\nI Say \"Hello World\"")
print('Hello\nWorld\nI Say "Hello World"')

# 문자열 연산
str1 = "First String"
str2 = "Second String"

# 인덱싱
print(str1[0], str1[2], str1[4])

# 슬라이싱
str3 = str2[2:5]
print(str3)     # str[n:m] -> n번째 부터 m-1번째 까지
print(str2[2:]) # str[n:] -> n번째 부터 끝까지
###########################################################
# 연결(+)
# 자바에서의 스트링 + 연산은 컴파일 시 StringBuffer에 저장되는 형태
# 파이썬은 + 연산을 오버로딩을 통해 지원해준다.
# __add__(self, str) { }
print(str1 + " " + str2)

# + 생략 가능
str3 = "str1" " " "str2"
print(str3)

# 문자열 객체와 정수형 객체는 + 연산을 할 수 없다.
name = "길동"
age = 30
# print(name + age)   # exception 발생하면서 exit() 실행됨

# 반복(*)
print(str1 * 3)
###########################################################
# len() 함수
print(len(str2))

# in, not in 연산
print("S" in str2)
print("S" not in str2)

# 문자열 객체는 변경할 수 없다. (immutable)
# str1[0] = "f"
###########################################################
# 서식 (formatting) - format() 함수
print("name:" + name + ", age:" + format(age, "d"))
print("name:" + format(name, "s") + ", age:" + format(age, "d"))

# C 스타일
# print("name:%s, age:%d", name, age);

# 서식 (formatting) - 튜플 이용한 포맷팅
f = "name:%s, age:%d"
print(f)                    # 단순 문자열
print(f % ("둘리", 13))    # 포맷팅
print(f % ("또치", 20))

# 서식 (formatting) - 딕셔너리 이용한 포맷팅
f = "name:%(name)s, age:%(age)d"
print(f % {"name": "둘리", "age": 13})
print(f % {"name": "또치", "age": 20})
###########################################################
# 대소문자 관련 객체 함수
s = "i like Python"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())
###########################################################
# 검색 관련 객체 함수
s = "I Like Python, I Like Java Also"
print(s.count("Like"))

print(s.find("Like"))
print(s.find("Like", 5))        # 5번째 부터 find
print(s.find("JavaScript"))    # 없으면 -1
print(s.rfind("Like"))

# find -> 발견 못하면 -1, index -> 발견 못하면 예외 발생
# print(s.index("JavaScript"))
print(s.rindex("Like"))

print(s.startswith("I Like"))
print(s.startswith("i Like"))
print(s.startswith("Like", 2))
print(s.endswith("Also"))
print(s.endswith("Java", 0, 26))    # endswith(str, n, m) : 문자열 str이 n 부터 m-1까지 끝나는지
print(s.endswith("Java", 0, 27))    # False. Java가 25번째에서 끝나기 때문
###########################################################
# 편집과 치환
s = '       spam and ham   '
print("---"+s.strip()+"---")
print("---"+s.rstrip()+"---")
print("---"+s.lstrip()+"---")

s = "<><abc><><defg><><>"
print(s.strip("<>"))    # 양쪽 끝에서 < 와 > 가 제거됨 <>를 합쳐서 생각하지 말고 개별 문자로 생각

s = "Hello Java"
print(s.replace("Java", "Python"))
###########################################################
# 정렬
s = "King and Queen"
print("--"+s.center(60) + "--")
print(s.center(60, "-"))
print(s.ljust(60, "-"))
print(s.rjust(60, "-"))
###########################################################
# 분리와 결합
s = "spam and ham"
t = s.split()
print(t)    # list
t = s.split(" and ")
print(t)

s2 = ":".join(t)
print(s2)

s3 = "one:two:three:four:five"
print(s3.split(":", 2))
print(s3.rsplit(":", 2))

lines = """1st line
2nd line
3rd line
4th line
"""
print(lines.split("\n"))    # 공백 문자열 표시
print(lines.splitlines())    # 공백 문자열 표시 안함
###########################################################
# 판별
print("1234".isdigit())
print("abcd".isalpha())

print("1234".isalpha())
print("abcd".isdigit())

print("abcd".islower())
print("ABCD".isupper())

print("\r\n".isspace())
print("\t".isspace())
print("    ".isspace())
print("".isspace())
###########################################################
# 0 채우기
print("20".zfill(5))
print("1234".zfill(5))
###########################################################
# 서식(포맷팅) 객체 함수
f = "name:{}, age:{}"
print(f)
print(f.format("둘리", 10))

print("name:{0}, age:{1}".format("둘리", 10))
print("name:{1}, age:{0}".format(30, "마이콜"))

print("{:3}의 제곱근은 {:.5}".format(2, 2**0.5))
print("{1:03}의 제곱근은 {0:.5}".format(2**0.5,2))

f = "name:{name}, age:{age}"
print(f.format_map({'name': '도우넛', 'age': 10 }))

