n = int(input('Enter the number of rows: '))
x=0
for i in range(n,0,-1):
    print((' '*x)+'*'*i)
    x+=1