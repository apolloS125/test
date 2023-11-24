def arabic_to_thai_number(arabic_number):
    thai_digits = ['๐', '๑', '๒', '๓', '๔', '๕', '๖', '๗', '๘', '๙']
    arabic_str = str(arabic_number)
    thai_number = ''.join([thai_digits[int(digit)] for digit in arabic_str])
    return f'Thai number is {thai_number}'

arabic_input = input('Enter only 5 Arabic number: ')
thai_output = arabic_to_thai_number(arabic_input)
print(thai_output)
