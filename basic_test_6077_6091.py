# Code up Python basic test 100
# [기초-종합] 6077 ~ 6091

"""
#6077
a = int(input())
b = 0
for i in range(1, a+1):
    if i%2==0:
        b += i
print(b)

#6078
a = input()

while a !='q':
    print(a)
    a = input()

if a=='q':
    print(a)

#6079
a = 1
cnt = 0 #언제까지 더해야하는지 카운트
sum = 0
n = int(input())
while (sum < n):
    sum = sum + a
    a = a + 1
    cnt = cnt + 1
print(cnt)

#6080
n, m = map(int, input().split())
for i in range(1, n+1) :
  for j in range(1, m+1) :
    print(i, j)

#6081
n = int(input(), 16)

for i in range(1, 16) :
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
"""

#6082
n = int(input())
for i in range(1, n+1) :
    if i%10==3 or i%10==6 or i%10==9:
        print("X", end=' ')
    else:
        print(i, end=' ')