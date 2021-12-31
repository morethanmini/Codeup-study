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

#6082
n = int(input())
for i in range(1, n+1) :
    if i%10==3 or i%10==6 or i%10==9:
        print("X", end=' ')
    else:
        print(i, end=' ')

#6083
r, g , b = input().split()
r = int(r)
g = int(g)
b = int(b)
n = 0
for i in range (r):
  for j in range (g):
    for k in range (b):
      print(i, j, k)
      n = n+1
print(n)

#6084
h, b, c, s = map(int, input().split())
m = (h*b*c*s)/(8*1024*1024)
a = round(m, 1)
x = "MB"
print(a, x)

#6085
w, h, b = map(int, input().split())
m = (w*h*b)/(8*1024*1024)
print(format(m,".2f"), "MB")

#6086
n = int(input())
s=0
c=0
while True:
  s+=c
  c+=1
  if(s>=n):
    break
print(s)

#6087
n = int(input())
for i in range(1, n+1):
  if i%3==0:
    continue
  print(i, end=' ')

#6088
a, d, n= map(int,input().split())
m = a + (n-1)*d
print(m)

#6089
a, r, n= map(int,input().split())
m = a*r**(n-1)
print(m)

#6090
a, m, d, n= map(int,input().split())
l = a*m+d
if n==1:
  print(a)
elif(n==2):
  print(l)
elif(n==3):
  l = l*m+d
  print(l)
elif(n>=4):
  i=3
while True:
  if(n<i):
    break
  l = l*m+d
  i+=1
print(l)

#6091
a, b, c = map(int, input().split())
d = 1
while d%a!=0 or d%b!=0 or d%c!=0:
  d+=1
print(d)

"""
