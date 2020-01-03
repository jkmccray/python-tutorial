# ====== Variables ======
import turtle

a = 5
print(a)

b = "hello"
print(b)

credit_card = 112233555937372
print(credit_card)

qazi_turtle = turtle.Turtle()
qazi_turtle.speed(15)

#  ====== Functions ======

# Make a square
def square():
  qazi_turtle.forward(100)
  qazi_turtle.right(90)
  qazi_turtle.forward(100)
  qazi_turtle.right(90)
  qazi_turtle.forward(100)
  qazi_turtle.right(90)
  qazi_turtle.forward(100)

# square()
# qazi_turtle.forward(200)
# square()

#  ====== If else statements ======
elephant_weight = 3000
ant_weight = 0.1

if elephant_weight < ant_weight:
  square()
else:
  qazi_turtle.forward(100)

#  ====== While loops ======
qazi = 'happy'
while qazi == 'sad':
  qazi_turtle.forward(10)

#  ====== For loops ======
for i in range(5):
  print(i)

for count in range(1):
  square()

def star():
  qazi_turtle.forward(100)
  qazi_turtle.right(144)
  qazi_turtle.forward(100)
  qazi_turtle.right(144)
  qazi_turtle.forward(100)
  qazi_turtle.right(144)
  qazi_turtle.forward(100)
  qazi_turtle.right(144)
  qazi_turtle.forward(100)
  qazi_turtle.right(144)
  qazi_turtle.forward(100)

star()

qazi_turtle.forward(100)

def triangle():
  qazi_turtle.forward(100)
  qazi_turtle.right(120)
  qazi_turtle.forward(100)
  qazi_turtle.right(120)
  qazi_turtle.forward(100)
  qazi_turtle.right(120)
  qazi_turtle.forward(100)

triangle()

#  ====== Data types: Integers, Floats, Strings, Booleans ======
# Casting
x = 1
print(float(x))
print(str(1))
print(int("34"))
print(bool(0))
print(bool(1))

# Strings
s = "hello"
print(s[0])

# Lists
names = ["Joe", "John", "James"]
print(names)
names.append("Gary")
print(names)
names.insert(0, "Jeff")
print(names)
names.remove("Joe")
print(names)
names.reverse()

numbers = [5,2,6,10,7,14,1]
print(numbers)
numbers.sort()
print(numbers)
# Iterate over a list
for num in numbers:
  print(num)

#  ====== Indexing, Slicing, Striding ======
digits = [0,1,2,3,4,5,6,7,8,9]

# Indexing:
# Negative index starts from the end of the list
print(digits[-1])
# Print the first element using negative index
print(digits[-len(digits)])

# Slicing - Print a range of elements
print(digits[:3])
print(digits[5:])
print(digits[1:5])
print(digits[1:-1])

# Striding - Print a range from 0 - 10 (not including 10) with a stride of 3
# Strides are leaps
print(digits[0:10:3])
# Reverse the list:
print(digits[::-1])
# If using a negative stride, have to reverse the indices of the range
print(digits[5:0:-2])

for d in range(len(digits)):
  print(digits[0:d])

# Get every group of 3 possible in the list
window_size = 3
for i in range(len(digits)-(window_size-1)):
  print(digits[i:i+window_size])

#  ====== String Parsing: Join and Split Functions ======
colors = 'blue, pink, orange, green'

colors_list = colors.split(', ')
print(colors_list)

joined = ' and '.join(colors_list)
print(joined)
csv = ','.join(colors_list)
print(csv)

#  ====== Tuples ======
# Tuple is a list with constraints
# Can't add or remove elements or change immutable elements within it
tuple_nums = (1,2,3)

# It can be useful to have a list of tuples
credit_card1 = (49195714362748261, 'Joe Rogan', '12/20', 123)
credit_card2 = (47262859371537109, 'Hoe Rogan', '2/20', 456)
credit_cards = [credit_card1, credit_card2]
print(credit_cards)

# Unpacking a tuple
person1 = ('Nancy Pants', 25, 'Pizza')
person2 = ('Rancy Rants', 21, 'Pasta')
people = [person1, person2]

(name, age, favfood) = person1
print(name)
print(age)
print(favfood)

for name, age, favfood in people:
  print(name)
  print(age)
  print(favfood)

# ====== Sets ======
# Cannot have duplicates in a set
s = {'blueberry', 'raspberry'}
s.add('strawberry')
s.add(4)
# The add method will only add the element to the set if it does not already exist in the set
# Will print in a random order
print(s)

# Remove the duplicates in a list
nums_list = [1,2,3,3,4,4,4,5]
# Cast to a set and then cast back to a list
no_duplicates_set = set(nums_list)
print(no_duplicates_set)
no_duplicates_list = list(no_duplicates_set)
print(no_duplicates_list)

# Methods: Union, Intersection, Difference
library1 = {'Harry Potter', 'Hunger Games', 'Lord of the Rings'}
library2 = {'Harry Potter', 'Romeo and Juliet'}

all_books_in_town = library1.union(library2)
print(all_books_in_town)

books_at_both_libraries = library1.intersection(library2)
print(books_at_both_libraries)

diff1 = library1.difference(library2)
print(diff1)
diff2 = library2.difference(library1)
print(diff2)

# .clear() will clear out the set and make it empty

# ====== Dictionaries ======
# Do not have an order
groceries = {
  'bananas': 5,
  'oranges':3
}
print(groceries['bananas']) # will throw an error if not in the dictionary
print(groceries.get('bananas')) # will return 'none' if not in the dictionary

contacts = {
  'Joe': '123-4567',
  'Jane': '987-6543'
}
print(contacts['Joe'])

sentence = 'Kiwi is the cutest cat in the world'
word_counts = {
  'kiwi': 1,
  'the': 2,
  'cat': 1
}
# change the value of 'the'
word_counts['the'] += 1
print(word_counts)

# Methods:
# dict.items() returns a list of tuples. Each tuple is a key-value pair
print(word_counts.items())
# dict.keys() returns a list of keys
print(word_counts.keys())
# dict.values() returns a list of values
print(word_counts.values())
# Delete an item from the dictionary using .pop() with its key
word_counts.pop('cat')
print(word_counts)
# Add an item to the dictionary
word_counts['kitty'] = 1
print(word_counts)
# Clear out the dictionary with dict.clear()

