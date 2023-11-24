def sensertext(text,words):
    sen = text.replace(words, '*' * len(words))
    return sen

text = input('Enter text: ')
words = input('Enter filter word: ')

print(f'Text after filter is "{sensertext(text,words)}"')
