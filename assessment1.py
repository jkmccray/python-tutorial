# Objects and Data Structures Assessment Test

# ======== Vocabulary ========
# Write a brief description of all the following Object Types and Data Structures we've learned about:

# Numbers: Either integers or floating point values that can be used in arithmetic expressions to calculate a result

# Strings: A collection of characters in a sequence, enclosed by either single or double quotation marks

# Lists: An ordered collection of elements that can be of any type

# Tuples: An ordered collection of elements that can be of any type, but the collection is immutable

# Dictionaries: An unordered collection of key value pairs

# ======== Numbers ========
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.

result = (3 * 16 / 2 - 14) ** 2 + 0.25

# Answer these 3 questions without typing code. Then type code to check your answer.

# What is the value of the expression 4 * (6 + 5)
# Answer: 44

# What is the value of the expression 4 * 6 + 5
# Answer: 29

# What is the value of the expression 4 + 6 * 5
# Answer: 34

# What is the type of the result of the expression 3 + 1.5 + 4?
# Answer: float

# What would you use to find a number’s square root, as well as its square?
# Square root: ** 0.5
# Square: ** 2

# ======== Strings ========
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
# Print out 'e' using indexing
print(s[1])
# Reverse the string 'hello' using slicing:
print(s[::-1])
# Given the string hello, give two methods of producing the letter 'o' using indexing.
# Method 1:
print(s[-1])
# Method 2:
print(s[4])

# ======== Lists ========
# Build this list [0,0,0] two separate ways.
# Method 1:
the_list = [0,0,0]
# Method 2:
the_list = [0]
the_list.append(0)
the_list.append(0)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'

# Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()

# ======== Dictionaries ========
# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

# Can you sort a dictionary? Why or why not?
# No because it does not have a specified order

# ======== Tuples ========
# What is the major difference between tuples and lists?
# --> Tuples are not immutable and have fewer built-in methods
# How do you create a tuple?
# --> Same as a list but with ()

# ======== Sets ========
# What is unique about a set?
# --> A set is an unordered collection of unique elements. It does not contain duplicates
# Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

# ======== Booleans ========
# What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

2 > 3 # --> False
3 <= 2 # --> False
3 == 2.0 # --> False
3.0 == 3 # --> True
4**0.5 != 2 # --> False

# Final Question: What is the boolean output of the cell block below?
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1'] # --> False
