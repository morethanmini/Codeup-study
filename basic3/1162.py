year, month, day = map(int, input().split())
result = year - month + day
result = str(result)

if result[-1] == '0':
    print('대박')
else:
    print('그럭저럭')