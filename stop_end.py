count_dict = {}
while True:
    text = input('Enter string: ')
    if text == 'end':
        break
    else:
        for char in text:
            if char.isalpha():
                lower_char = char.lower()
                if lower_char in count_dict:
                    count_dict[lower_char] += 1
                else:
                    count_dict[lower_char] = 1

print('******************************')
print('*     Alphabet Counting      *')
print('******************************')

sorted_chars = sorted(count_dict.keys())
for char in sorted_chars:
    print(f"{char} {count_dict[char]}")

print('******************************')