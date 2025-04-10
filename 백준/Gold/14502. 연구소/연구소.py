from collections import deque

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
viruses = []
safe_count = 0
for i in range(N):
  for j in range(M):
    if lab[i][j] == 0:
      safe_count += 1
    if lab[i][j] == 2:
      viruses.append((i, j))

def initialize_visited():
  for i in range(N):
    for j in range(M):
      visited[i][j] = 0

def is_range(x, y):
  return 0 <= x < N and 0 <= y < M

def can_go(x, y):
  if not is_range(x, y):
    return False
  if lab[x][y] > 0 or visited[x][y] > 0:
    return False
  return True

max_safe = 0
V = []
def dfs(n):
  global max_safe
  if n == 3:
    initial_count = safe_count - 3
    initialize_visited()
    for virus in viruses:
      initial_count -= bfs(virus)
    max_safe = max(max_safe, initial_count)
    return
  for i in range(N):
    for j in range(M):
      if lab[i][j] == 0 and (i, j) not in V:
        lab[i][j] = 1
        dfs(n+1)
        lab[i][j] = 0

dxs = [-1, 0, 1, 0]
dys = [ 0,-1, 0, 1]
def bfs(start):
  q = deque([start])
  count = 0
  while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
      nx, ny = x + dx, y + dy
      if can_go(nx, ny):
        visited[nx][ny] = 2
        count += 1
        q.append((nx, ny))
  return count

dfs(0)
print(max_safe)