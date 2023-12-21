def check_brackets(brackets):
    
    lst = []
    mapping = {')': '(', '}': '{', ']': '['}

    for i in brackets:
        if i in '({[':
            lst.append(i)
        elif i in ')}]':
            if not lst or lst[-1] != mapping[i]: 
                return "Not Equivalent"
            lst.pop()

    return "Equivalent" if not lst else "Not Equivalent"

bracket_str = input("Bracket: ")

result = check_brackets(bracket_str)
print(result)
