time, score = map(int, input().split())

if time % 10 == 0:
    result = score + int((90 - time) // 5)
else:
    result = score + int((90 - time) // 5) + 1

print(result)