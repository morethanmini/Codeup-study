#remind_note
"""
while - 특정 조건을 만족하는 경우 수행, 반복을 멈추게 하는 장치가 필요
    while [조건문]:
       [수행부분]
while과 while [Ture]의 차이::
    while 문은 조건이 True 로 평가될 때만 반복하게 됩니당.
    즉, while True: 라는 것은 항상 참이기 때문에
    무한히 반복하는 반복문을 작성할 때 주로 쓰게 됩니당.

for - 리스트, 문자열, 튜플 등 컬렉션 타입의 아이템을 하나씩 순회하면서 사용 가능
    for [변수] in [문자열, 리스트, 튜플]:
	    [수행부분]

    range(n)은 0, 1, 2, ..., n-2, n-1까지의 수열을 의미
    range(3)은 0, 1, 2인 수열을 의미
    range(시작, 끝, 증감감

"""

"""
n = 1 #처음 조건 검사를 통과하기 위해 0이 아닌 값을 임의로 저장
while n!=0:
    n = int(input())
    if n != 0:
        print(n)

n = int(input())
for i in range(0, n+1):
    print(i)


"""
n = int(input())

s = 0
t = 0
while s < n:
    t = t + 1
    s = s + t

print(t)
