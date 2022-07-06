num = input().split()

if int(num[1]) < 10:
    num.insert(1, '0')

if int(num[2]) < 10:
    num.insert(3,'0')
    if int(num[2]) < 100:
        num.insert(4,'0')

print(''.join(num))