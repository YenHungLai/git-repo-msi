'''
Created on Dec 15, 2017

@author: Jacob
'''

# =========================================================================
# Print and strings
# Back slash means treating the symbol as regular string.
# print("\"Hello World\"")
# Putting r in front of a string means printing the string as it is.
# print(r"what \n\n\nn\the fuck")

# # Multiple assignment
# x, y, name, is_cool = (1, 2, 'Jacob', True)
# print(x, y, name, is_cool)
# print(type(x))

# # Type cast
# x = str(1)
# print(type(x))

# string = "this is a string"
# print("the last character of the string: " + string[-1])
# print("the first character of the string: " + string[0])
# print("you can pick out a slice of string: " + string[0:4])
# # If you don't include the beging or end it assumes start and end.
# print(string[:])

# Arguments by position
# print('My name is {name} and I am {age}'.format(name='Jacob', age='23'))

# F-Strings(v3.6+)
# Like JS template literals
# name = 'Jacob'
# age = '23'
# print(f'Hello, my name is {name} and I am {age}')

# String methods
# s = 'hello world'
# print(s.capitalize())
# print(s.upper())
# print(s.lower())
# print(len(s))                # Length of the string
# print(s.replace('o', 'A'))
# print(s.count('o'))          # Count the number of letter 'o'
# print(s.startswith('h'))
# print(s.endswith('d'))
# print(s.split())             # Convert into a list(like an array)
# print(s.find('o'))           # Find position of the first 'o'

# # List
# list1 = [23, 24, 69, 85]
# # list2 = [1, 2, 3, 4, 5]
# # # You can combine lists
# # print(list1 + list2)
# # # Add item to the list, append only take 1 argument
# # list1.append("A")
# # print(list1)
# list1.insert(1, 123)
# print(list1)
# list1.remove(23)
# print(list1)

# Membership operators
# if 23 in list1:
#     print('23 is in list1')

# if 23 in list1:
#     print('23 is in list1')

# x = 20
# y = 20
# print(x is y)
# print(x is not y)

# # Replace multiple items at once.
# list1[0:2] = [1, 2]
# print(list1)
# print("\n\n")
#
# Tuples
# # Cannot be modified.
# coordinates = (4, 5)
# print(coordinates)

# # Delete a tuple or anything
# del coordinates

# # if-elif-else
# print("What is your major?(SE, CE or AE ")
# choice = input()
#
# if choice == "SE":
#     print("You are taking CS125\n" * 2)
# elif choice == "CE":
#     print("You are taking CEC220\n" * 3)
# else:
#     print("You suck\n")
# =========================================================================

# =========================================================================
# # for loop
# players = ["LBJ", "KD", "MELO", "CP3"]
#
# for item in players:
#     print(item)
#     print("The word has " + str(len(item)) + " letters")
#
# # range function, range(start, end, increment)
# for item in range(0, 15, 2):
#     print(item)
#
# # Range and while
# index = 0
#
# while players[index] != "MELO":
#     print(players[index] + ", you are not MELO")
#     index += 1
#
# # is operator will return True if two variables point to the same object,
# # it's different from ==.
# list_num = [1, 2, 3, 4, 5]
#
# for item in list_num:
#     if item is 4:
#         print("Found", item)
#         break
#     else:
#         print(item, "is not 4")
#
# # Function
# def Hello(name):
#     print("Hi guys my name is", name)
#     return 9285833646

# print("This is my number", Hello("Jake"))

# Lambda function
# getSum = lambda num1, num2 : num1 + num2
# print(getSum(12, 22))
# =========================================================================

# =========================================================================
# # The None value, the print function returns None.
# # Python adds return None to the end of any function definition
# # with no return statement.
# None
#
# # print() function automatically adds a newline character to
# # the end of the string it is passed.
# print("Hello ", end="")
# print("World")
#
# # sep keyword in print()
# print("cat", "dogs", "rats", sep="&")
# =========================================================================

# =========================================================================
# # Default value for arguments.
#
#
# def salary(amount="empty"):
#     if amount == "Max":
#         player = "Lebron James"
#     elif amount == "Low":
#         player = "JLin"
#     elif amount == "empty":
#         player = "Whoever"
#     print(player)
#
#
# salary()
# =========================================================================

# =========================================================================
# # Keyword arguments
#
#
# def sentence(name="Jacob", action="ate", item="burger"):
#     print(name, action, item)
#
#
# sentence(item="pizza")
# sentence(action="slapped", item="Reen")
# =========================================================================

# =========================================================================
# # Flexible number of arguments
#
#
# def add_num(*args):  # Put * in front of variable name.
#     sum_num = 0
#     for item in args:
#         sum_num += item
#     print(sum_num)
#
#
# add_num(1, 2, 3, 4, 5)
# =========================================================================


# =========================================================================
# def person(age, sex, race):
#     print("This is a", race, age, "year-old", sex)
#
#
# # Has to match the number of arguments in the parameter list.
# info = ['30', 'male', 'black']
# person(*info)   # Unpacking arguments.
# =========================================================================

# =========================================================================
# # # Sets. Can't have any duplicates
# players = {'LBJ', 'CP3', 'KD', 'LBJ'}
# #
# # # Won't print the same item in the set twice.
# # print(players)
# print('LBJ' in players)
# players.add('MELO')
# players.remove('CP3')
# print(players)
# players.clear() # Gives you an empty set, different from delete
# =========================================================================

# # Dictionary. Composed with keys and values.
# dic = {'LBJ': ' Greatest of my time', 'KD': ' Best scorer in the game'}
# print(dic['LBJ'])
# print(dic.get('LBJ'))
# # for k, v in dic.items():
# #     print(k + v)

# # Add key/value
# dic['MELO'] = 'Used to be good'
# print(dic)
# print(dic.keys())   # Returns all the keys
# print(dic.items())

# # Copy a dictionary
# dic2 = dic.copy()
# print(dic2)

# # Delete item
# dic.pop('LBJ')
# del(dic['MELO'])
# print(dic)

# # Clear
# dic.clear()

# # List of dictionary
# people = [
#     {'name': 'Martha', 'age': 30},
#     {'name': 'Kevin', 'age': 20},
# ]

# print(people[0]['name'])

# =========================================================================
# # Modules.
# import mod
# import random
#
# mod.bitch()  # Include the file name.
#
# print(random.randrange(1, 10))

# import datetime
# from datetime import date
# import time
# # Use "pip install" to install modules
# from camelcase import CamelCase

# today = datetime.date.today()
# today = date.today()
# print(today)
# timestamp = time.time()
# print(timestamp)

# c = CamelCase()
# print(c.hump('hello there world'))
# =========================================================================

# =========================================================================
# # Download an image from the internet.
# import random
# import urllib.request
#
#
# def download_img(url):
#     name = random.randrange(1, 1000)
#     fullname = str(name) + '.jpg'
#     urllib.request.urlretrieve(url, fullname)
#
#
# download_img('http://cdn04.cdn.justjaredjr.com/wp-content/uploads/pictures/2014/10/sam-lily/lily-collins-sam-claflin-net-porter-edit-feature-09.jpg')
# =========================================================================

# =========================================================================
# # Read and write files.
# filew = open('sample.txt', 'w')
# filew.write('just writing some stuff in the file.')
# filew.close()
#
# filer = open('sample.txt', 'r')
# text = filer.read()
# print(text)
# filer.close()
# =========================================================================

# =========================================================================
# # Downloading files from the web.
# from urllib import request
#
# url = 'None'
#
# def download_file(file_url):
#     response = request.urlopen(file_url)
#     file = response.read()
#     file_file = str(file)
# =========================================================================

# =========================================================================
# # Exception.
# while True:
#     try:
#         answer = int(input("What is your age? "))
#         print("He is", answer, "years old")
#         break
#     except ValueError:  # Other errors include: ZeroDivisionError.
#         print("Plase enter you number")
#     finally:
#         print("loop complete")
# # A 'finally' clause is always executed before leaving the try statement, whether an exception has occurred or not.
# # If you only write 'except', it includes all kinds of error but it's not good.
# =========================================================================

# =========================================================================
# # Class and Objects.
# class Car:
#     price = 21000
#     def price_up(self):  # 'self' means using something from this class.
#         self.price += 1

# civic = Car()
# print("This car price is", civic.price)
# civic.price_up()
# print("This car price is", civic.price)
#
# fit = Car()
# fit.price_up()
# fit.price_up()
# print("This car price is", fit.price)
# =========================================================================

# init.
# class Dog:
#     # Code in here will execute as soon as you create an obj.
#     def __init__(self):
#         print("Just created an obj!!!")
#
#     def bark(self, num):
#         print("Rooooof!!, Im", num, "year old.")
#
#
# Nori = Dog()
# Nori.bark(10)

# Instance Variables.
# class Dog:
#     # Code in here will execute as soon as you create an obj.
#     def __init__(self, race):
#         print("Just created an obj!!!")
#         self.race = race    # Instance Variable
#
#
# Nori = Dog('GoldenRetriver')
# print(Nori.race)

# # Web crawler
# import requests
# from bs4 import BeautifulSoup
#
# def spider(max_pages):
#     page = 1
#     while page < max_pages:
#         url = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=computer&rh=i%3Aaps%2Ck%3Acomputer"
#         src = requests.get(url)
#         text = src.text
#         soup = BeautifulSoup(text)
#         for

# # os module.
# import os
#
# # # Print current working directory.
# # print(os.getcwd())
# #
# # Change working directory.
# os.chdir('/Users/Jacob/Desktop')
# print(os.getcwd())
# os.listdir()
#
# # Create a directory.
# os.mkdir('/Users/Jacob/Desktop/Test')

# # mkdirs creates all the intermediate directories for you, mkdir does not
# os.makedirs('/Users/Jacob/Desktop/Test/sub_folder')

# # Remove directories.
# os.rmdir('/Users/Jacob/Desktop/Test')
# os.removedirs('/Users/Jacob/Desktop/Test')

# # Rename a file.
# os.rename('Test.txt', 'Test1.txt')

# # Get information about a file.
# print(os.stat('Test.txt'))

# # Does not work for some reason.
# for dirpath, dirnames, filenames in os.walk('/Users/Jacob/Desktop/'):
#     print('Current Path:', dirpath)
#     print('Directory:', dirnames)
#     print('Files:', filenames)

# # Exponent function.
# result = 2**3

# # JSON to dictionary
# import json

# sampleJSON = '{"first_name": "Jacob", "last_name": "Lai"}'
# sample = json.loads(sampleJSON)
# print(sample)

# # Dictionary to JSON
# car = {'make': 'Ford', 'model': 'Mustang', 'year': '2019'}
# carJSON = json.dumps(car)
# print(carJSON)

# Regular expression
# import re

# textToSearch = 'jacob Lai'
# sample = "test.email+alex@leetcode.com"
# sample2 = "test.e.mail+bob.cathy@leetcode.com"
# sample3 = "testemail+david@lee.tcode.com"

# # Compile a regular expression pattern, returning a pattern object.
# pattern = re.compile(r'[a-z]*\.?[a-z]*')
# matches = pattern.search(sample)

# print(matches.group(0))
# for match in matches:
#     print(match)


# Jewels and Stones problem
# J = "aA"
# S = "aAAbbbb"
# count = 0

# for letter in S:
#     if letter in J:
#         count = count+1

# print(count)

# # Better solution, what is this syntax???
# print(sum(s in J for s in S))


# Unique Email Addresses
# sample = "test.email+alex@leetcode.com"
# sample2 = "test.e.mail+bob.cathy@leetcode.com"
# sample3 = "testemail+david@lee.tcode.com"

# emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]

# mySet = set()
# for email in emails:
#     at = email.find('@')
#     temp = email[0:at]
#     print(temp)
#     temp = temp.replace('.', '')
#     plus = temp.find('+')
#     print(plus)
#     if plus is not -1:
#         temp = temp[0:plus]
#     result = temp + email[at:]
#     print(result)
#     mySet.add(result)

# print(mySet)

# Concurrency

# Threading
# import threading
# import time

# def thread_function(name):
#     print('I am the thread function\n')
#     time.sleep(2)
#     print('I am done\n')

# x = threading.Thread(target=thread_function, name='Thread_1', args=(1,))
# x.start()
# print('Main thread here\n')
# x.join()
# print('Say this after thread has joined\n')

# class Test:
#     def __init__(self):
#         self.x = 1

#     def func1(self):
#         print('From func1', self.x)
#         self.x = self.x + 10
#         time.sleep(2)

#     def func2(self):
#         print('From func2', self.x)

# obj = Test()
# t1 = threading.Thread(target=obj.func1)
# t2 = threading.Thread(target=obj.func2)
# t1.start()
# t1.join()
# t2.start()

# OS module
# import os
# print(os.name)
# print(os.getcwd())
# To print absolute path on your system
# print(os.path.abspath('.'))
# To print files and directories in the current directory on your system
# print(os.listdir('.'))
# print(os.getlogin())
# x = input('Enter shit: ')
# print(x)

# File system manipulation
# f = open(r"C:\Users\Jacob\Downloads\Programming Language Practices\Python\practice\inputs.txt", "r")
# f = open("inputs.txt", "r")
# data = f.readlines()
# print(data)

# Binary search
"""
The simplest version of binary search
"""
# nums = [-1, 0, 3, 5, 9, 12, 15, 16, 21]
# target = 9

# def binarySearch(nums):
#     left, right = 0, len(nums) - 1
#     print(f'left: {left}, right: {right}')
#     while left <= right:
#         # Move pivot to the middle of the array
#         pivot = (left + right) // 2
#         # Target found
#         if nums[pivot] == target:
#             return pivot
#         else:
#             # Search the left side of the pivot
#             if target < nums[pivot]:
#                 right = pivot - 1
#             # Search the right side of the pivot
#             else:
#                 left = pivot + 1

#     # Number does not exist in the array
#     return -1

# result = binarySearch(nums)
# if result == -1:
#     print(f'{target} does not exist in nums so return {result}')
# else:
#     print(f'{target} exists in nums and its index is {result}')

# Using binary search to find square root of a number
# target = 81

# def sqrt(target):
#     if target == 0:
#         return 0

#     left, right = 1, target

#     while True:
#         # How to come up with this formula?
#         mid = left + (right - left)//2
#         # How to come up with this formula?
#         if mid > (target/mid):
#             right = mid - 1
#         else:
#             # How to come up with this formula?
#             if (mid + 1) > target/(mid + 1):
#                 return mid
#             left = mid + 1

# print(f'The sqrt of {target} is: {sqrt(target)}')

# Guess Number Higher or Lower
# def guess(n):
#     if n == 3:
#         return 0
#     elif n < 3:
#         return 1
#     elif n > 3:
#         return -1

# # Using binary search


# def guessNumber(n):
#     left, right = 1, n
#     while left <= right:
#         mid = (left + right) // 2
#         if guess(mid) == 0:
#             return mid
#         else:
#             if guess(mid) == 1:
#                 left = mid + 1
#             elif guess(mid) == -1:
#                 right = mid - 1


# print(guessNumber(50))


# Search in Rotated Sorted Array
# def search(nums, target):
#     temp = nums.copy()
#     temp.sort()
#     left, right = 0, len(temp) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if temp[mid] == target:
#             return nums.index(temp[mid])
#         else:
#             if target < temp[mid]:
#                 right = mid - 1
#             elif target > temp[mid]:
#                 left = mid + 1

#     # Number not in list
#     return -1

# print(search([4, 5, 6, 7, 0, 1, 2], 5))


"""
Template #2 is an advanced form of Binary Search. 
It is used to search for an element or condition 
which requires accessing the current index and its 
immediate right neighbor's index in the array.
An advanced way to implement Binary Search.
"""
# def binarySearch(nums, target):
#     if len(nums) == 0:
#         return -1

#     left, right = 0, len(nums)
#     # Loop/Recursion ends when you have 1 element left.
#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid

#     # Post-processing:
#     # End Condition: left == right
#     # Check if the last element is the target
#     if left != len(nums) and nums[left] == target:
#         return left
#     return -1

# print(binarySearch([1, 2, 3, 4, 5], 7))


# First Bad Version

# # Check if version is bad
# def isBadVersion(version):
#     # Everything after version 4 is bad.
#     if version >= 4:
#         return True
#     else:
#         return False


# def firstBadVersion(n):
#     left, right = 1, n
#     # There will be two elements after the loop
#     while left + 1 < right:
#         mid = (left + right) // 2
#         if isBadVersion(mid):
#             right = mid
#         else:
#             left = mid

#     # Post processing
#     # One of the remaining version has to be bad
#     # If both are bad then return the first bad version(left)
#     if isBadVersion(left):
#         return left
#     else:
#         return right


# print(firstBadVersion(5))

# Find Peak Element
# nums = [1, 2, 1, 3, 5, 6, 4]

# def findPeakElement(nums):
#     left, right = 0, len(nums) -1
#     # Minimum three elements in the array
#     while left < right - 1:
#         mid = (left + right) // 2
#         # If the number is bigger than its neighbors
#         if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
#             return mid
#         else:
#             # If the number to the right is bigger, search right side
#             if nums[mid] < nums[mid + 1]:
#                 left = mid + 1
#             # Search right side
#             else:
#                 right = mid - 1

#     # Post processing
#     # Only two elements left to be searched
#     if nums[left] > nums[right]:
#         return left
#     else:
#         return right

# print(findPeakElement(nums))


# Find Minimum in Rotated Sorted Array
"""
If the array is not rotated and the array is in ascending order, then last element > first element.
The array is sorted bu rotated.
Numbers on the left should be less than those on the right in a sorted array.
Find the infection point: [4, 5, 1, 2, 3], the infection point is between 5 and 1.
All the elements to the left of inflection point > first element of the array.
All the elements to the right of inflection point < first element of the array.

Find the mid element of the array.
If mid element > first element of array this means that we need to look for the inflection point on the right of mid.
If mid element < first element of array this that we need to look for the inflection point on the left of mid.
"""
# nums = [3, 4, 5, 0, 1, 2]


# def findMin(nums):
#     left, right = 0, len(nums) - 1

#     # No rotation, return the smallest number.
#     if nums[right] > nums[0]:
#         return nums[0]

#     while left < right:
#         mid = (left + right) // 2

#         if nums[mid] < nums[mid - 1]:
#             return nums[mid]

#         if nums[mid] > nums[mid + 1]:
#             return nums[mid + 1]

#         # Search left for infection point.
#         if nums[mid] < nums[left]:
#             right = mid - 1
#         else:
#             left = mid + 1

#     # There is only one element in the array because left == right
#     return nums[0]


# print(findMin(nums))

"""
Template #3 is another unique form of Binary Search. 
It is used to search for an element or condition which requires accessing the current index 
and its immediate left and right neighbor's index in the array.
"""
# nums = [1, 2, 3, 4, 5]
# def binarySearch(nums, target):
#     if len(nums) == 0:
#         return -1

#     left, right = 0, len(nums) - 1
#     while left + 1 < right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid
#         else:
#             right = mid

#     # Post-processing:
#     # End Condition: left + 1 == right
#     if nums[left] == target: return left
#     if nums[right] == target: return right
#     return -1

# print(binarySearch(nums , 3))


# Search for a Range

# Test cases
# nums = [5, 7, 7, 8, 8, 10]
# nums = []
# nums = [1]
# nums = [7, 8, 8, 8, 8, 8, 8, 9]
# result = []
# Using two Binary search to find starting index and ending index

# def searchRange(nums, target):
#     def searchStart(nums, target):
#         left, right = 0, len(nums) - 1
#         # If array is empty
#         if len(nums) == 0:
#             return result.append(-1)

#         # Breaks when there are two elements left
#         while left + 1 < right:
#             mid = (left + right) // 2
#             # If target found and the item to the left is of different value, starting index found
#             if nums[mid] == target and nums[mid - 1] != target:
#                 return result.append(mid)
#             else:
#                 if nums[mid] < target:
#                     left = mid
#                 # If mid value larger than target or equal to target(But is not the starting index), search left
#                 else:
#                     right = mid

#         # Post processing, 2 elements left
#         print('POST')
#         if nums[left] == target:
#             print('LEFT')
#             result.append(left)
#         elif nums[right] == target:
#             print('RIGHT')
#             result.append(right)
#         # Item not in array
#         else:
#             result.append(-1)


#     searchStart(nums, target)


#     def searchEnd(nums, target):
#         left, right = 0, len(nums) - 1
#         # If array is empty
#         if len(nums) == 0:
#             return result.append(-1)

#         # Breaks when there are two elements left
#         while left + 1 < right:
#             mid = (left + right) // 2
#             # If target found and the item to the right is of different value, ending index found
#             if nums[mid] == target and nums[mid + 1] != target:
#                 return result.append(mid)
#             else:
#                 # If mid value is equal to target(But is not the ending index) or smaller than target, search right.
#                 if nums[mid] == target or nums[mid] < target:
#                     left = mid
#                 else:
#                     right = mid

#         # Post processing, 2 elements left
#         print('POST')
#         if nums[right] == target:
#             print('RIGHT')
#             result.append(right)
#         elif nums[left] == target:
#             print('LEFT')
#             result.append(left)
#         # Item not in array
#         else:
#             result.append(-1)

#     searchEnd(nums, target)

#     return result

# print(searchRange(nums, 8))


# Circular queue
# class MyCircularQueue:
#     def __init__(self, k: int):
#         """
#         Initialize your data structure here. Set the size of the queue to be k.
#         """
#         self.queue = []
#         self.head = 0
#         self.tail = 0
#         self.size = k

#     def enQueue(self, value: int) -> bool:
#         """
#         Insert an element into the circular queue. Return true if the operation is successful.
#         """
#         if len(self.queue) < self.size:
#             self.queue.append(value)
#             self.tail = len(self.queue) - 1
#             print('Current queue:', self.queue)
#             print('Head is at index', self.head)
#             print('Tail is at index', self.tail)
#             print('\n')
#             return True
#         else:
#             return False

#     def deQueue(self) -> bool:
#         """
#         Delete an element from the circular queue. Return true if the operation is successful.
#         """
#         if len(self.queue) != 0:
#             print('Dequeued:', self.queue.pop(self.head))
#             self.tail = len(self.queue) - 1
#             print('Current queue:', self.queue)
#             print('Head is at index', self.head)
#             print('Tail is at index', self.tail)
#             print('\n')
#             return True
#         else:
#             return False

#     def Front(self) -> int:
#         """
#         Get the front item from the queue.
#         """
#         if len(self.queue) == 0:
#             return -1
#         print(f'The front item is {self.queue[self.head]}')
#         return self.queue[self.head]

#     def Rear(self) -> int:
#         """
#         Get the last item from the queue.
#         """
#         if len(self.queue) == 0:
#             return -1
#         print(f'The rear item is {self.queue[self.tail]}')
#         return self.queue[self.tail]

#     def isEmpty(self) -> bool:
#         """
#         Checks whether the circular queue is empty or not.
#         """
#         if len(self.queue) == 0:
#             return True
#         else:
#             return False

#     def isFull(self) -> bool:
#         """
#         Checks whether the circular queue is full or not.
#         """
#         if len(self.queue) == self.size:
#             return True
#         else:
#             return False

#     def traverse(self):
#         print('The queue is: ')
#         while self.head <= self.tail:
#             print(self.queue[self.head], end =" ")
#             self.head = self.head + 1


# circularQueue = MyCircularQueue(3)
# print(circularQueue.enQueue(1))
# print(circularQueue.enQueue(2))
# print(circularQueue.enQueue(3))
# print(circularQueue.enQueue(4))
# print(circularQueue.Rear())
# print(circularQueue.isFull())
# print(circularQueue.deQueue())
# print(circularQueue.enQueue(4))
# print(circularQueue.Rear())
# circularQueue.traverse()


# Moving Average from Data Stream
# class MovingAverage:

#     def __init__(self, size: int):
#         """
#         Initialize your data structure here.
#         """
#         self.queue = []
#         self.head = 0
#         self.tail = 0
#         self.size = size

#     def next(self, val: int) -> float:
#         if len(self.queue) < self.size:
#             self.queue.append(val)
#             self.tail = len(self.queue) - 1
#             return sum(self.queue) / len(self.queue)
#         else:
#             self.queue.pop(self.head)
#             self.queue.append(val)
#             self.tail = len(self.queue) - 1
#             return sum(self.queue) / len(self.queue)

#     def traverse(self):
#         print('The queue is: ')
#         while self.head <= self.tail:
#             print(self.queue[self.head], end=" ")
#             self.head = self.head + 1


# obj = MovingAverage(3)
# print(obj.next(1))
# print(obj.next(10))
# print(obj.next(3))
# print(obj.next(5))

# obj.traverse()


# Queue and BFS(Breadth-first Search)
"""
One common application of Breadth-first Search (BFS) is to find the shortest path from the root node to the target node
The nodes closer to the root node will be traversed earlier.
The processing order of the nodes is the exact same order as how they were added to the queue, which is First-in-First-out (FIFO).
If a node X is added to the queue in the kth round, the length of the shortest path between the root node and X is exactly k
"""

# ???????


# Stack

# Min Stack
# class MinStack:

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.front = 0
#         self.back = 0

#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         self.back = len(self.stack) - 1
#         print(self.stack)

#     def pop(self) -> None:
#         print(f'Poped: {self.stack.pop(self.back)}')
#         print(self.stack)
#         self.back = len(self.stack) - 1

#     def top(self) -> int:
#         if len(self.stack) != 0:
#             return self.stack[self.back]
#         else:
#             return None

#     def getMin(self) -> int:
#         return min(self.stack)

# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(f'The min is: {minStack.getMin()}')
# minStack.pop()
# print(f'The top element is: {minStack.top()}')
# print(f'The min is: {minStack.getMin()}')


# Valid Parentheses
# def isValid(s):
#     stack = []
#     dict = {"]":"[", "}":"{", ")":"("}
#     for char in s:
#         if char in dict.values():
#             stack.append(char)
#         elif char in dict.keys():
#             if stack == [] or dict[char] != stack.pop():
#                 return False
#         else:
#             return False
#     return stack == []

# print(isValid(['(', ')', '[', ']', '{', '}']))

# or

# def isValid(s):
#     stack = []
#     # An empty string is also considered valid
#     if len(s) == 0:
#         return True

#     for char in s:
#         # If char is opening bracket, push closing bracket to stack
#         if char == '(':
#             stack.append(')')
#         elif char == '{':
#             stack.append('}')
#         elif char == '[':
#             stack.append(']')
#         """
#         An empty stack means a closing bracket appeared before an opening bracket,
#         If char does not equal to top item in the stack that means the closing bracket
#         does not match the opening bracket.
#         """
#         elif stack == [] or char != stack.pop():
#             return False

#     return stack == []

# print(isValid(['(', ')', '[', ']', '{', '}']))


# Daily Temperatures
# T = [73, 74, 75, 71, 69, 72, 76, 73]


# def dailyTemperatures(T):
#     stack = []
#     result = [0]*len(T)
#     # enumerate() iterates and returns both index and value
#     for i, temp in enumerate(T):
#         while stack != [] and temp > stack[-1][1]:
#             index, tempInStack = stack.pop()
#             # When encouter a high temperature, pop the stack and calculate result in that position
#             result[index] = i - index

#         stack.append((i, temp))

#     return result


# print(dailyTemperatures(T))

# Negative index for list means last to the list(count backwards).


# Breadth-first search

# Find the shortest path from the root node to the target node.


# Depth-first search


# Hash table

# Organizes data using hash functions in order to support quick insertion and search.

# There are two different kinds of hash tables: hash set and hash map.

# The hash set is one of the implementations of a set data structure to store no repeated values.




from collections import Counter
class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Initialize list of lists
        # Use _ when index value is not important
        self.bucket = [[] for _ in range(20)]

    def hashFunction(self, key):
        return key % 5

    def add(self, key: int) -> None:
        if key not in self.bucket[self.hashFunction(key)]:
            self.bucket[self.hashFunction(key)].append(key)
        print(self.bucket)

    def remove(self, key: int) -> None:
        if key in self.bucket[self.hashFunction(key)]:
            self.bucket[self.hashFunction(key)].remove(key)
        print(self.bucket)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.bucket[self.hashFunction(key)]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(1)
# obj.add(2)
# print(obj.contains(1))
# print(obj.contains(3))
# obj.add(2)
# print(obj.contains(2))
# obj.remove(2)
# print(obj.contains(2))


# The hash map is one of the implementations of a map data structure to store (key, value) pairs.
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = [[] for _ in range(20)]

    def hashFunction(self, key):
        return key % 5

    def if_exist(self, key):
        return key in self.bucket[self.hashFunction(key)].keys()

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        temp = self.bucket[self.hashFunction(key)]
        for i in temp:
            if i[0] == key:
                temp.remove(i)
                temp.append((key, value))
                return

        temp.append((key, value))

        print(self.bucket)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        temp = self.bucket[self.hashFunction(key)]
        for i in temp:
            if i[0] == key:
                return i[1]

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        temp = self.bucket[self.hashFunction(key)]
        for i in temp:
            if i[1] == key:
                temp.remove(i)

        print(self.bucket)

# Your MyHashMap object will be instantiated and called as such:
# hashMap = MyHashMap()
# hashMap.put(1, 1)
# hashMap.put(2, 2)
# print(hashMap.get(1))
# print(hashMap.get(3))
# hashMap.put(2, 1)
# print(hashMap.get(2))
# hashMap.remove(2)
# print(hashMap.get(2))


# Remove Duplicates from Sorted Array
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# Solution 1
# def removeDuplicates(nums):
#     head = 0
#     runner = head + 1
#     result = len(nums)
#     while head <= len(nums) - 2:
#         if nums[head] == nums[runner]:
#             nums.remove(nums[runner])
#             result -= 1
#         else:
#             head += 1
#             runner = head + 1

#     print(nums)
#     return result


# print(removeDuplicates(nums))

# Solution 2
# def removeDuplicates(nums):
#     new_nums = list(dict.fromkeys(nums))
#     nums.clear()
#     for item in new_nums:
#         nums.append(item)
#     return len(new_nums)

# print(removeDuplicates(nums))
# print(nums)

# Best Time to Buy and Sell Stock II
prices = [7, 1, 5, 3, 6, 4]


# def maxProfit(prices):
#     buy = 0
#     profit = 0
#     while True:
#         sell_price = max(prices[(buy+1):])
#         print('sell_price', sell_price)
#         if sell_price > prices[buy]:
#             profit += sell_price - prices[buy]
#             prices.remove(sell_price)

#         buy += 1
#         print('profit', profit)
#         print('arr', prices)

#     return profit


# print(maxProfit(prices))


# Find the NEXT price larger than buying price

# Windows notification
# import time
# from win10toast import ToastNotifier
# toaster = ToastNotifier()
# toaster.show_toast("Hello World!!!",
#                    "Python is 10 seconds awsm!",
#                    duration=10)

# toaster.show_toast("Example two",
#                    "This notification is in it's own thread!",
#                    icon_path=None,
#                    duration=5,
#                    threaded=True)
# # Wait for threaded notification to finish
# while toaster.notification_active(): time.sleep(0.1)

# Ternary operator
# x = True
# y = 5 if x else 10
# print(y)

# z = ('a', 'b')[True]

# var = 1 or 0

# Contains Duplicate
# nums = [3, 1]
nums = [1, 2, 3, 1]


# Using collections
# def containsDuplicate(nums):
#     counter = Counter(nums)
#     print(counter)
#     for num in nums:
#         if counter[num] != 1:
#             return True

#     return False

# print(containsDuplicate(nums))

# def containsDuplicate(nums):
#     for num in nums:
#         count = nums.count(num)
#         if count != 1:
#             return True

#     return False


# print(containsDuplicate(nums))

# def containsDuplicate(nums):
#     compare = []
#     for num in nums:
#         if num in compare:
#             return True

#         compare.append(num)

#     return False


# print(containsDuplicate(nums))

# Sort the list and then consecutive elements should be distinct or there are duplicates
# def containsDuplicate(nums):
#     if len(nums) == 1:
#         return False

#     nums.sort()
#     for i in range(1, len(nums)):
#         # Compare element and the one before it to avoid list index out of range
#         if nums[i - 1] == nums[i]:
#             return True

#     return False


# print(containsDuplicate(nums))

nums = [4, 1, 2, 1, 2]


# def singleNumber(nums):
#     for num in nums:
#         count = nums.count(num)
#         if count != 2:
#             return num


# print(singleNumber(nums))


# Single Number
# def singleNumber(nums):
#     nums.sort()
#     print(nums)
#     for i in range(1, len(nums)):


# print(singleNumber(nums))

# Rotate Image
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# def rotate(matrix):
#     n = len(matrix[0])
#     # Transpose matrix
#     for i in range(n):
#         for j in range(i, n):
#             print(i, j)
#             # Would matrix[j][i] reference the new value or old?
#             matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

#     # Reverse each row
#     for i in range(n):
#         matrix[i].reverse()


# rotate(matrix)
# print(matrix)

# Valid Sudoku
# board = [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"]
# ]


# def isValidSudoku(board):


# print(isValidSudoku(board))


# First Unique Character in a String Solution
# s = 'leetcode'
# s = 'loveleetcode'
# s = ''
s = 'cc'

# from collections import Counter

# def firstUniqChar(s):
#     counter = Counter(s)
#     for index, char in enumerate(s):
#         if counter[char] == 1:
#             return index

#     return -1


# print(firstUniqChar(s))

# This solution will time out
# def firstUniqChar(s):
#     for (index, char) in enumerate(s):
#         if s.count(char) == 1:
#             return index

#     return -1


# print(firstUniqChar(s))

# Intersection of Two Arrays
# nums1 = [1,2,2,1]
# nums2 = [2,2]

# def intersection(nums1, nums2):
#     set1 = set(nums1)
#     set2 = set(nums2)
#     print(set1 & set2)
#     return set1 & set2

# print(intersection(nums1, nums2))

# Happy Number
n = 2

# Using set, array works too but slower
# def isHappy(n):
#     s = set()
#     while n != 1:
#         n = sum([int(i) ** 2 for i in str(n)])
#         print(n)
#         if n in s:
#             return False
#         else:
#             s.add(n)

#     return True

# print(isHappy(n))

# Two Sums
nums = [2, 7, 11, 15]
target = 9

# Using hashmap solution
# def twoSum(nums):
#     hashmap = {}
#     for (v, i) in enumerate(nums):
#         if target - i in hashmap:
#             return [v, hashmap[target-i]]
#         else:
#             hashmap[i] = v
#         print(hashmap)


# print(twoSum(nums))

# Isomorphic Strings?????
s = "egg"
t = "add"
# s = "paper"
# t = "title"
# s = "aba"
# t = "baa"


def isIsomorphic(s, t):
    map1 = {}
    map2 = {}
    for i, v in enumerate(s):
        map1[i] = v
    for i, v in enumerate(t):
        map2[i] = v
    
    print(map1)
    print(map2)




print(isIsomorphic(s, t))
