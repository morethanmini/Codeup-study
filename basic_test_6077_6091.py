# Code up Python basic test 100
# [기초-실행구조] 6077 ~ 6091

"""
#6077
a = int(input())
b = 0
for i in range(1, a+1):
    if i%2==0:
        b += i
print(b)
"""
a = int(input())
b = 0
for i in range(1, a+1):
    if i%2==1:
        b+=i
        print(b)