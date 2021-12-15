# Code up Python basic test 100
# [기초-실행구조] 6065 ~ 6076

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