
text = input('Enter 3 characters: ')
if len(text) != 3:
    print("word length is mismatched")
    
shifted_text = ''
for char in text:
    if char.isupper():
        shifted = chr(((ord(char) - 65 + 1) % 26) + 65)
        shifted_text += shifted
    else:
        shifted = chr(((ord(char) - 97 + 1) % 26) + 97)
        shifted_text += shifted
    
print(f'Ciphertext is {shifted_text.upper()}')