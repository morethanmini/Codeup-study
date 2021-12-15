# Code up Python basic test 100
# [기초-실행구조] 6065 ~ 6076

"""
#6065
def evennumber():
    a, b, c = map(int, input().split())
    if a%2==0 :
        print(a)

    if b%2==0 :
        print(b)

    if c%2==0 :
        print(c)

evennumber()

#6066
def evenodd():
    a, b, c = map(int, input().split())
    if a%2==0:
        print("even")
    else:
        print("odd")

    if b%2==0:
        print("even")
    else:
        print("odd")

    if c%2==0:
        print("even")
    else:
        print("odd")
evenodd()

#6067
def evenodd2():
    a = int(input())
    if a<0:
        if a%2==0:
            print('A')
        else:
            print('B')
    else:
        if a%2==0:
            print('C')
        else:
            print('D')
evenodd2()

#6068
def evaluation():
    a = int(input())

    if a<100:
        if 90<=a<=100:
            print('A')
        elif 70<=a<=89:
            print('B')
        elif 40<=a<=69:
            print('C')
        elif 0<=a<=39:
            print('D')
    else:
        print('0~100 입력')

evaluation()

#6069
def evaluation2():
    a = input()

    if a=="평가":
        print('내용')
    elif a=="A":
        print('best!!!')
    elif a=="B":
        print('good!!')
    elif a == "C":
        print('run!')
    elif a == "D":
        print('slowly~')
    else:
        print('what?')

evaluation2()

#6070
a = int(input())

if a//3==1:
    print('spring')
elif a//3==2:
    print('summer')
elif a//3==3:
    print('fall')
else:
    print('winter')

#6071
a=1
while a!=0:
    a = int(input())
    if a!=0:
        print(a)

#6072
a = int(input())

while a!=0:
    print(a)
    a = a-1

#6073
a = int(input())

while a!=0:
    print(a-1)
    a = a-1

#6074
c = ord(input())
t = ord('a')
while t<=c :
  print(chr(t), end=' ')
  t += 1

#6075
a = int(input())
b = 0
while b<=a:
    print(b, end='\n')
    b += 1

#6076
a = int(input())
for i in range(a+1):
    print(i)
"""