a, b ,c = map(int, input().split())

car = 170

if a <= car or b <= car or c <= car:
    print('CRASH')
else:
    print('PASS')