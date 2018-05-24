# 리스트 생성
l = []
l = [1, 2, "python"]

# 인덱싱
print(l[-3], l[-2], l[-1], l[0], l[1], l[2])

# 슬라이싱
print(l[1:3])           # list[n:m] : n번째 부터 m-1번째 까지
print(l[:])             # list[:]   : 처음부터 끝까지
print(l[2:])            # list[n:]  : n번째 부터 끝까지
print(l[2::-1])         # step -> list[n::-1] : n번째 부터 -1씩 감소시키면서 맨 앞까지
print(l[len(l)-1::-1])

# 반복(*)
l2 = l * 2
print(l2)

# 연결(+)
l3 = l + [3, 4, 5]
print(l3)

# 길이
print(len(l3))

# 확인
print(5 in l3)

# del() : 삭제 함수
del l3[0]
print(l3)

# 변경 가능한 시퀀스 (mutable)
a = ['apple', 'banana', 10, 20]
a[2] = a[2] + 90
print(a)

# 슬라이스를 통한 치환
a = [1, 12, 123, 1234]
a[0:2] = [10, 20]
print(a)

a[0:2] = [10]
print(a)

a[1:2] = [20]
print(a)

a[2:3] = [30]
print(a)

# 슬라이스를 통한 삭제
a = [1, 12, 123, 1234]

a[1:2]= []
print(a)

a[0:] = []
print(a)

# 슬라이스를 통한 삽입
a = [1, 12, 123, 1234]
a[1:1] = ['a']
print(a)

a[5:] = [12345]
print(a)

a[:0] = [-12, -1, 0]
print(a)

#########################################################

# 객체 함수 (메소드)

a = [1, 3, 4]

# 중간 삽입
a.insert(1, 2)      # insert(n,m) : n번째 위치에 m 객체 삽입
print(a)

# 맨 뒤 삽입
a.append(5)
print(a)

# 맨 앞 삽입
a.insert(0, 0)
print(a)

# reverse
a.reverse()
print(a)

# 제거
a.remove(3)     # remove(n) : n 값 삭제
print(a)

# 확장
# append -> 값 하나씩 추가, extend -> 값 여러개를 배열로 추가
a.extend([-1, -2, -3])
print(a)

# 리스트를 스택으로 사용하기
stack = []

stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

print(stack.pop())
print(stack.pop())
print(stack)

# 큐로 사용하기
q = [1, 2]

q.append(3)
q.append(4)
q.append(5)
print(q)

print(q.pop(0))
print(q.pop(0))
print(q)

# sort() : 객체 함수 -> 내장된 sorting 알고리즘에 따라 정렬
l = [1, 5, 3, 9, 8, 4, 2]
l.sort()
print(l)

l.sort(reverse=True)    # 역순
print(l)

l = [10, 2, 22, 9, 8, 33, 4, 11]
l.sort(key=str)         # 스트링 key 값 기반으로 정렬
print(l)

l.sort(key=int)         # 정수형 key 값 기반으로 정렬
print(l)

# sorted() : 내장(전역) 함수
l = [19, 46, 37, 28, 91, 55, 64]
l2 = sorted(l)
print(l2)

l2 = sorted(l, reverse=True)
print(l2)

def f(i):
    return i % 10

l2 = sorted(l, key=f, reverse=True)
print(l2)













