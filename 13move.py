import string
print('Select 2 options\n'
    ,'- 1 encrypt with ROT 13\n'
    ,'- 2 decrypt with ROT 13\n')
choices = input("Choose option: ")
text = input("Enter text: ")

lower = string.ascii_lowercase
upper = string.ascii_uppercase
answer = ""

for i in text:
    if i.isupper():
        if choices == "1" :
            answer += upper[(upper.index(i) + 13) % 26]
        elif choices == "2" :
            answer += upper[(upper.index(i) - 13) % 26]
    elif i.islower():
        if choices == "1" :
            answer += lower[(lower.index(i) + 13) % 26]
        elif choices == "2" :
            answer += lower[(lower.index(i) - 13) % 26]
    else :
        answer += i

if choices == "1" :
    print('Ciphertext is "{}"' .format(answer))
elif choices == "2" :
    print('Plaintext is "{}"' .format(answer))