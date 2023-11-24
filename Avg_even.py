lst = []
lst3=[]
for i in range(20):
    numbers = int(input(f'Enter number #{i+1}: '))
    lst.append(numbers)

sets = sorted(set(lst))

for i in range(len(sets)):
    if i %2 ==0:
        lst3.append(sets[i])


avg_even = sum(lst3) / len(lst3)
unique_numbers = ' '.join(map(str, sets))

print(f'Unique numbers is {unique_numbers}')
print(f'Average number of even position in list is {avg_even:.2f}')
