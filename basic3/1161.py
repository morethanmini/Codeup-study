a, b = map(int, input().split())

n1, n2, result = '', '' ,''

if a % 2 == 1:
    n1 = '홀수'
else:
    n1 = '짝수'

if b % 2 == 1:
    n2 = '홀수'
else:
    n2 = '짝수'

if n1 == n2:
    result = '짝수'
else:
    result = '홀수'

print(f'{n1}+{n2}={result}')