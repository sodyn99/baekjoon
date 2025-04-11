R, C, M = map(int, input().split())
sharks = [
    [r-1, c-1, s, d-1, z] for _ in range(M) for r, c, s, d, z in [map(int, input().split())]
]
# x -> R, y -> C
go_x = [i for i in range(R)] + [i for i in range(R-2, 0, -1)]
go_y = [i for i in range(C)] + [i for i in range(C-2, 0, -1)]

#상, 하, 우, 좌
dxs = [-1, 1, 0, 0]
dys = [ 0, 0, 1,-1]

def change_direction(direction):
  if direction < 2:
    direction = abs(1 - direction)
  else:
    direction = abs(5 - direction)
  return direction

score = 0
for t in range(C):
  # sharks 정렬
  sharks.sort(key=lambda x: (x[1], x[0]))

  for i in range(len(sharks)):
    if sharks[i][1] == t:
      score += sharks[i][4]
      sharks.pop(i)
      break

  for shark in sharks:
    x, y = shark[0], shark[1]
    speed = shark[2]
    direction = shark[3]
    nx = (x+speed*dxs[direction]) % ((R-1) * 2)
    ny = (y+speed*dys[direction]) % ((C-1) * 2)
    if nx > R-1 or -(R-1) < nx < 0:
      direction = change_direction(direction)
    if ny > C-1 or -(C-1) < ny < 0:
      direction = change_direction(direction)
    shark[3] = direction
    x, y = go_x[nx], go_y[ny]
    shark[0], shark[1] = x, y

  # sharks 정렬
  sharks.sort(key=lambda x: (x[0], x[1], -x[4]))
  for i in range(len(sharks)-1, 0, -1):
    if (sharks[i][0], sharks[i][1]) == (sharks[i-1][0], sharks[i-1][1]):
      sharks.pop(i)

print(score)