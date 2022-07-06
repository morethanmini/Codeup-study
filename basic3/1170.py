num = input().split()

if int(num[2]) <= 10:
    num.insert(2, '0')

print(''.join(num))