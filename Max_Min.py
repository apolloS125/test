lst =[]
while True:
    x = int(input('Enter number: '))
    if x <0:
        break
    else:
        lst.append(x)

print('Minimum number is',min(lst))
print('Maximum number is',max(lst))