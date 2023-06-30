# Problem 1: Print the following pattern
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# Problem 2: Display numbers from a list using loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break
    if i > 150:
        continue
    if i%5==0:
        print(i)

#  Problem 3: Append new string in the middle of a given string

def middle(s1, s2):
    mid = len(s1) // 2
    s3 = s1[:mid] + s2 + s1[mid:]
    return s3

s1 = "Aunt"
s2 = "Kelly"
s3 = middle(s1, s2)
print("Resulting string:", s3)

# Problem 4: Arrange string characters such that lowercase letters should come first

# def arrange(string):
#     arr1=[]
#     arr2=[]

#     for i in string:
#         if i.islower():
#             arr1.append(i)
#         else:
#             arr2.append(i)    
#     new_string = "".join(arr1+arr2)
#     return new_string        

# string = input("Enter a string: ")
# arranged_string = arrange(string)
# print("Arranged string:", arranged_string)

# Problem 5: Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

combined = []

for i in range(len(list1)):
    combined.append(list1[i] + list2[i])

print(combined)

# Problem 6: Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

combined_list=[]
for i in range(len(list1)):
    for j in range(len(list2)):
        combined_list.append(list1[i]+list2[j])

print(combined_list)        

# Problem 7: Iterate both lists simultaneously

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

combined_lists=[]
for i in range(len(list1)):
    j = len(list1) - 1 - i
    print(list1[i], list2[j])

print(combined_lists)     

# Problem 8: Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

obj={}

for i in employees:
    obj[i] = defaults.copy()

print(obj)

# Problem 9: Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
# keys = ["name", "salary"]

print({"name":sample_dict["name"], "salary":sample_dict["salary"]})

# Problem 10: Modify the tuple

tuple1 = (11, [22, 33], 44, 55)
list1 = list(tuple1)
list1[1][0] = 222
new_tuple = tuple(list1)
print(new_tuple)