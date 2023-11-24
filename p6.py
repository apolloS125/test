n = int(input('Enter the number of rows: '))
symbo = input('Enter print symbol: ')
for x in range(n,0,-1):
  for y in range(n - x):
    print (" ",end="")
  for y in range(x,0,-1):
    print(symbo,end="")
  for y in range(x,1,-1):
    print(symbo,end="")
  print()
