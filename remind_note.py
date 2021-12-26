#remind_note
"""
range(n)은 0, 1, 2, ..., n-2, n-1까지의 수열을 의미
range(3)은 0, 1, 2인 수열을 의미
range(시작, 끝, 증감감

while - 특정 조건을 만족하는 경우 수행, 반복을 멈추게 하는 장치가 필요
for - 리스트, 문자열, 튜플 등 컬렉션 타입의 아이템을 하나씩 순회하면서 사용 가능
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
n = input()
print(n)