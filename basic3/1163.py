year, month, day = map(int, input().split())
result = year + month + day
result = str(result)
result_int = int(result[-3])

if result_int % 2 == 0:
    print('대박')
else:
    print('그럭저럭')