print('Welcome to FizzBuzz Game')

def calculate_fizz_buzz(number):
    result = ''
    if number % 3 == 0:
        result += 'Fizz'
    if number % 5 == 0:
        result += 'Buzz'
    if not result:
        result = 'NoFizzBuzz'
    
    char_count = len(result)
    return char_count

def main():
    total = 0
    while True:
        user_input = int(input("Enter number: "))
        fizz_buzz = calculate_fizz_buzz(user_input)
        total += user_input % fizz_buzz
        
        if total > 20:
            break
    
    final_result = total % int(str(total)[-1])
    print(f"Your score: {final_result}")

if __name__ == "__main__":
    main()
