def sum_of_digits(n):
    sum = 0
    if n < 0:
        n = -n
    while n > 0:
        sum += n % 10
        n = n // 10

    return sum


number = 1325132435356
print 'The sum of the digits of %s are:' % number
print sum_of_digits(number)
print sum_of_digits(123)
print sum_of_digits(6)
print sum_of_digits(-10)


def to_digits(n):
    list_of_digits = []
    if n < 0:
        n = -n
    while n > 0:
        list_of_digits.insert(0, n % 10)
        n = n // 10

    return list_of_digits


print to_digits(123)
print to_digits(99999)
print to_digits(123023)


def to_number(digits):
    number = 0
    for i in range(len(digits)):
        number += digits[i] * 10 ** (len(digits) - 1 - i)

    return number


print to_number([1, 2, 3])
print to_number([9, 9, 9, 9, 9])
print to_number([1, 2, 3, 0, 2, 3])


def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return factorial


def fact_digits(n):
    sum = 0
    list_digits = to_digits(n)
    for digit in list_digits:
        sum += fact(digit)

    return sum


print fact_digits(111)
print fact_digits(145)
print fact_digits(999)


def fibonacci(n):
    sequence = []
    if n >= 1:
        sequence.append(1)
    if n >= 2:
        sequence.append(1)
    if n > 2:
        for i in range(2, n):
            sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence


print fibonacci(1)
print fibonacci(2)
print fibonacci(3)
print fibonacci(10)


def fib_number(n):
    result = to_number(fibonacci(n))
    return result


print fib_number(3)
print fib_number(10)


def palindrome(obj):
    obj = str(obj)
    is_palindrome = True
    for i in range(len(obj) / 2 + 1):
        if obj[i] != obj[len(obj) - i - 1]:
            is_palindrome = False

    return is_palindrome


def palindrome2(obj):
    obj_a = str(obj)
    obj_b = obj_a[::-1]
    if obj_a == obj_b:
        return True
    else:
        return False


print palindrome2(121)
print palindrome2('kapak')
print palindrome2('baba')


def count_vowels(str):
    sum_vowels = 0
    vowels = 'aeiouy'
    for i in range(len(str)):
        if str[i].lower() in vowels:
            sum_vowels += 1

    return sum_vowels


print count_vowels('Python')
print count_vowels('Theistareykjarbunga')
print count_vowels('grrrrgh!')
print count_vowels('Github is the second best thing that happend to programmers, after the keyboard!')
print count_vowels('A nice day to code!')


def count_consonants(str):
    sum_consonants = 0
    consonants = 'bcdfghjklmnpqrstvwxz'
    for i in range(len(str)):
        if str[i].lower() in consonants:
            sum_consonants += 1

    return sum_consonants


print count_consonants('Python')
print count_consonants('Theistareykjarbunga')
print count_consonants('grrrrgh!')
print count_consonants('Github is the second best thing that happend to programmers, after the keyboard!')
print count_consonants('A nice day to code!')


def char_histogram(string):
    histogram = {}
    for i in range(len(string)):
        if string[i] in histogram:
            histogram[string[i]] += 1
        else:
            histogram[string[i]] = 1

    return histogram


print char_histogram('Python')
print char_histogram('Python!')
print char_histogram('AAAaaa!!!')
