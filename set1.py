# 1. Hello World

print("Hello World")

# 2. Data Type Play

integar = 55
print(integar)
print("Its Type is : ", type(integar))
string = "I am a boy"
print(string)
print("Its Type is : ", type(string))
boolean = True
print(boolean)
print("Its Type is : ", type(boolean))
lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lists)
print("Its Type is : ", type(lists))
tuples = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuples)
print("Its Type is : ", type(tuples))
dictionaries = {
    "name": "Kuldeep",
    "age": 21,
    "class": "graduation",
    "Aim": "Software Engineer",
}
print(dictionaries)
print("Its Type is : ", type(dictionaries))
sets = {1, 2, 3, 4, 5, 6}
print(sets)
print("Its Type is : ", type(sets))

# 3. List Operations

# creating list
num = list(range(1, 11))
print("List : ", num)
# adding to list
num.append(11)
print("Updated List by adding : ", num)
# removing from list
num.remove(1)
print("Updated List by removing : ", num)
# sorting list
num.sort()
print("Sorted List : ", num)

# 4. Sum and Average

num = input("Enter a list of numbers separated by spaces: ").split()
num = [int(num) for num in num];

# sum of numbers
whole = sum(num)

# average of numbers
average = whole/len(num)

print("Sum : ", whole)
print("Average : ", average)

# 5. String reversal
def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string
input_string = input("Enter a string to make it Reverse : ")
reversed_string = reverse_string(input_string)
print("Reversed String : ", reversed_string)

# 6. Count Vowels

def count_vowel(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

string = input("Enter a string: ")
count = count_vowel(string)
print("Number of vowels:", count)

# 7. Prime Number


def is_prime(num):
    if num <= 1:
        return False
    for key in range(2, int(num ** 0.5) + 1):
        if num % key == 0:
            return False

    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# 8. Factorial of a Number

def factorial(number):
    if number < 0:
        return "Enter Postive Number"
    elif number == 0:
        return 1
    else:
        fact = 1
        for i in range(1, number + 1):
            fact *= i
        return fact

number = int(input("Enter a number: "))
ans = factorial(number)
print("Factorial of", number, "is",ans)

# 9. fibonacci series

def fibonacci(n):
    arr = [0, 1]

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return arr

    for _ in range(2, n):
        next_num = arr[-1] + arr[-2]
        arr.append(next_num)

    return arr

# Test the function
n = int(input("Enter any Number: "))
result = fibonacci(n)
print("Fibonacci Sequence (first", n, "numbers):", result)

# 10. List Comprehension

sqrt = [num ** 2 for num in range(1, 11)]
print(sqrt)