# 1 . Tuple Unpacking: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.

tuples = [("John", 25), ("Jane", 30),("kuldeep",21)]
string = ""
for i, j in tuples:
    string += f"{i} is {j} years old. "

print(string)

# 2. Dictionary Manipulation: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, 
# update the age of a name, and delete a name from the dictionary.
def add_person(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, new_age):
    if name in dictionary:
        dictionary[name] = new_age

def delete_person(dictionary, name):
    if name in dictionary:
        del dictionary[name]

people = {}
add_person(people, "John", 25)
print(people) 

update_age(people, "John", 26)
print(people)  

delete_person(people, "John")
print(people) 

# 3. Two Sum Problem: Given an array of integers and a target integer, find the two integers in the array that sum to the target.

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)

# 4. Palindrome Check: Write a Python function that checks whether a given word or phrase is a palindrome.

def is_palindrome(word):
    word = word.replace(" ", "").lower()
    if word == word[::-1]:
        return True
    else:
        return False

input_word = "madamh"
if is_palindrome(input_word):
    print(f"The word {input_word} is a palindrome.")
else:
    print(f"The word {input_word} is not a palindrome.")


# 5.  Selection Sort: Implement the selection sort algorithm in Python.

def selection_sort(arr):
    n = len(arr)
 
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
    
        arr[i], arr[min_index] = arr[min_index], arr[i]
my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)
print(my_list)

# 7. FizzBuzz: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# 8. File I/O: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.


