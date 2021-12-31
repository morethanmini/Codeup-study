# Code up Python basic test 100
# [기초-리스트] 6092 ~ 6098

"""
#6092
n = int(input())
a = input().split()

for i in range(n):
  a[i] = int(a[i])

d = []
for i in range(24):
  d.append(0)

for i in range(n):
  d[a[i]]+=1

for i in range(1,24):
  print(d[i], end=' ')

#6093
n = int(input())
a = input().split()

for i in range(n):
  a[i] = int(a[i])

for i in range(n-1, -1, -1):
  print(a[i],end =' ')

#6094
n = int(input())
a = input().split()

min = 10001

for i in range(n):
  a[i] = int(a[i])
  if(a[i]<min):
    min = a[i]
print(min)

#6095
n = int(input())
d = []
for i in range(20):
  d.append([])
  for j in range(20):
    d[i].append(0)
for i in range(n):
  x, y = map(int, input().split())
  d[int(x)][int(y)] = 1
for i in range(1,20):
  for j in range(1,20):
    print(d[i][j], end = ' ')
  print()

#6096
d = [list(map(int, input().split())) for i in range(19)]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if d[j][y-1] == 0:
            d[j][y-1] = 1
        else:
            d[j][y-1] = 0

        if d[x-1][j] == 0:
            d[x-1][j] = 1
        else:
            d[x-1][j] = 0

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()

#6097
h, w = map(int, input().split())
n = int(int(input()))
array = [[0] * w for i in range(h)]

for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            array[x-1][y+j-1] = 1
    else:
        for j in range(l):
            array[x+j-1][y-1] = 1

for i in array:
    print(' '.join(map(str, i)))

#6098
# 입력 값 설정
maze = [list(map(int, input().split())) for i in range(10)]

# 개미 시작점 설정
x, y = 1, 1
maze[1][1] = 9

while True:
    # 오른쪽 벽이 0일 때
    if maze[x][y + 1] == 0:
        y += 1
        maze[x][y] = 9

    # 오른쪽 벽이 1일 때
    elif maze[x][y + 1] == 1:
        if maze[x+1][y] == 1:
            break
        elif maze[x+1][y] == 2:
            x+=1
            maze[x][y] = 9
            break
        else:
            x += 1
            maze[x][y] = 9

    # 오른쪽 벽이 2일 때
    else:
        y += 1
        maze[x][y] = 9
        break

for i in maze:
    print(' '.join(map(str, i)))
"""
