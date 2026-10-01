#1. Function without argument without return

#create a function to check whether the number is prime or not
'''
number = int(input('Enter a number : '))
factor_count = 0

for i in range(1, number + 1):
    if number % i == 0:
        factor_count += 1

if factor_count == 2:
    print(f'{number} is a prime number')
else:
    print(f'{number} is not a prime number')
'''

'''
def prime_check():
    number = int(input('Enter a number : '))
    factor_count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            factor_count += 1

    if factor_count == 2:
        print(f'{number} is a prime number')
    else:
        print(f'{number} is not a prime number')
prime_check()
'''

'''
def check_even_odd():
    a = 10
    if a % 2 == 0:
        print('even')
    else:
        print('odd')
check_even_odd()
print(check_even_odd)
x = check_even_odd
print(x)
print(type(check_even_odd))
print(type(check_even_odd()))
'''

#2. Function with argument without return

#create a function to check whether the number is prime or not
'''
def prime_check(number, factor_count):
    for i in range(1, number + 1):
        if number % i == 0:
            factor_count += 1

    if factor_count == 2:
        print(f'{number} is a prime number')
    else:
        print(f'{number} is not a prime number')
prime_check()
'''

'''
def prime_check(number, factor_count):
    for i in range(1, number + 1):
        if number % i == 0:
            factor_count += 1

    if factor_count == 2:
        print(f'{number} is a prime number')
    else:
        print(f'{number} is not a prime number')
prime_check(int(input('Enter a number : ')), 0)
'''



#3. Function without argument with return

#create a function to check whether the number is prime or not
'''
def prime_check():
    number = int(input('Enter a number : '))
    factor_count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            factor_count += 1

    if factor_count == 2:
        return f'{number} is a prime number'
    else:
        return f'{number} is not a prime number'
print(prime_check())
'''

'''
def x():
    print(10)
    print(20)
    return 30
    print(40)
x()
'''

'''
def a():
    print('hi')
    return 
    print(True)
    print(20)
print(a())
'''


#4. Function with argument with return

#create a function to check whether the number is prime or not
'''
def prime_check(number, factor_count):
    for i in range(1, number + 1):
        if number % i == 0:
            factor_count += 1

    if factor_count == 2:
        return f'{number} is a prime number'
    else:
        return f'{number} is not a prime number'
print(prime_check(int(input('Enter a number : ')), 0))
'''


#wap to find the sum of all digits of a number
'''
def sum_digits(number, sum_of_digits):
    while number != 0:
        sum_of_digits += number % 10
        number //= 10
    return sum_of_digits
print(sum_digits(int(input('Enter a number : ')), 0))
'''
#create a function to find the sum of all digits of a number
'''
def sum_digits(number, sum_of_digits):
    while number != 0:
        sum_of_digits += number % 10
        number //= 10
    return sum_of_digits
print(sum_digits(2343, 0))
'''
#create a function to find the factorial of a number
'''
def find_factorial(number, factorial):
    for i in range(1, number + 1):
        factorial *= i        
    return factorial
print(find_factorial(int(input('Enter a number : ')), 1))
'''
#create a function to check whether the number is strong or not
'''
def strong_number(number, sum_of_factorials):
    for i in str(number):
        factorial = 1
        for j in range(1, int(i) + 1):
            factorial *= j
        sum_of_factorials += factorial

    if sum_of_factorials == number:
        return f'{number} is a strong number'
    else:
        return f'{number} is not a strong number'
print(strong_number(int(input('Enter a number : ')), 0))
'''
'''
def xyz():
    a = 10
    b = 2
    print(a + b)
    print(a ** b)
xyz()
'''
