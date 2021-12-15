# Code up Python basic test 100
# [기초-비트시프트, 비교,논리연산] 6046 ~ 6064

"""
#6046
a = input()
#print(int(a)*2)
print(int(a)<<1)

#6047
a, b = input().split()
print(int(a) << int(b))

#6048
a, b = map(int, input().split())
print(a<b)
#split의 결과를 map 함수로 모두 int 변환

#6049
a, b = map(int, input().split())
print(a==b)

#6050
a, b = map(int, input().split())
print(a<=b)

#6051
a, b = map(int, input().split())
print(a!=b)

#6052
a = int(input())
print(bool(a))

#6053
a = bool(int(input()))
print(not a)

#6054
a, b = map(int, input().split())
print(bool(a) and bool(b))

#6055
a, b = map(int, input().split())
print(bool(a) or bool(b))

#6056
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

#6057
a, b = map(int, input().split())
c = bool(a)
d = bool(b)
print(c == d)

#6058
a, b = map(int, input().split())
c = bool(a)
d = bool(b)
print((not c) and (not d))

#6059
a = int(input())
print(~a)

#6060
a, b = map(int, input().split())
print(a&b)

#6061
a, b = map(int, input().split())
print(a|b)

#6062
a, b = map(int, input().split())
print(a^b)

#6063
a, b = map(int, input().split())
c = (a if(a>=b) else b)
print(c)

#6064
a, b, c = map(int, input().split())
d = (a if a<b else b) if ((a if a<b else b)<c) else c
print(d)
"""