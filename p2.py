n = int(input('Enter the number of rows: '))
for i in range(1,n+1):
    print(' '*(n-1) + '*'*i)
    n -=1