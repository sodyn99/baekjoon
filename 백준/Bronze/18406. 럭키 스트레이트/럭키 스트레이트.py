N = list(map(int, list(input())))

if sum(N[:int(len(N)/2)]) == sum(N[int(len(N)/2):]):
  print("LUCKY")
else:
  print("READY")