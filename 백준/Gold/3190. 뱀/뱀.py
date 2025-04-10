from collections import deque

N = int(input()) # 보드 크기
K = int(input()) # 사과 개수
apples = []
for _ in range(K):
  i, j = input().split()
  i, j = int(i) - 1, int(j) - 1
  apples.append((i, j))
arr = [[0 for _ in range(N)] for _ in range(N)]
arr[0][0] = 1
L = int(input()) # 뱀 방향 변환 횟수
changes = {}
for _ in range(L):
  X, C = input().split()
  X = int(X)
  changes[X] = C

snake = deque()

# 상, 우, 하, 좌
dxs = [-1, 0, 1, 0]
dys = [ 0, 1, 0,-1]
def change_direction(direction, C):
  if C == "L":
    direction -= 1
    if direction == -1:
      direction = 3
  else:
    direction += 1
    if direction == 4:
      direction = 0
  return direction

def is_range(x, y):
  return 0 <= x < N and 0 <= y < N and arr[x][y] == 0

t = 0
direction = 1
head_x, head_y = 0, 0
while True:
  t += 1
  snake.append((head_x, head_y))
  if t - 1 in changes:
    direction = change_direction(direction, changes[t-1])
  head_x, head_y = head_x + dxs[direction], head_y + dys[direction]
  if not is_range(head_x, head_y):
    break
  if (head_x, head_y) in apples:
    apples.remove((head_x, head_y))
  else:
    tail = snake.popleft()
    arr[tail[0]][tail[1]] = 0
  arr[head_x][head_y] = 1

print(t)