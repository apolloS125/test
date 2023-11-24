n = int(input('Enter the number of rows: '))
symbo = input('Enter print symbol: ')
for x in range(1,n+1):
  for y in range(n - x):
    print (" ",end="")
  for y in range(1,x+1):
    print(symbo,end="")
  for y in range(2,x+1):
    print(symbo,end="")
  print()
