x = 0
y = 0
lst = []
pos = input("Path: ").strip()
for i in pos:
    if i == '^':
        x += 1
    elif i == 'v':
        x -= 1
    elif i == '>':
        y += 1
    elif i == '<':
        y -= 1
    elif i =='x':
        lst.append((y, x))    

ans = ' '.join(map(str, lst))

if not lst:
    print('Not Found')
else:
    print('Locations:', ans)
