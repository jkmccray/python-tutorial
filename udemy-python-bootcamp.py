# ====== Numbers ======
# 2 to the power of 3:
print(2 ** 3) # can also do roots this way
# Floor division
print (7//4)

# ====== Strings ======
# Strings are immutable in python

# Escape a character
print('hello\nworld')

# Reverse a string
a_string = 'hello world'
print(a_string[::-1])

# Repeat string with multiplication
letters = 'zx'
print(letters*10)

# Built-in string methods
new_string = 'Hello I am a string'
print(new_string.upper())
print(new_string.lower())
print(new_string.split())
print(new_string.split('a'))


# Print formatting with strings
print('This is a string {}'.format('INSERTED'))
print('The {1} {2} {0}'.format('fox','quick', 'brown'))
print('The {q} {b} {f}'.format(f='fox',q='quick', b='brown'))
# Float formatting: {value:width.precision f}
result = 100/777
print('The result was {r:10.5f}'.format(r=result))

# Formatted string literals
name = 'John'
print(f'Hello, his name is {name}')
name = 'Sam'
age = 3
print(f'{name} is {age} years old')

# ====== Lists ======
my_list = [1,2,3]
print(len(my_list))
another_list = [4,5,6]
new_list = my_list + another_list
print(new_list)
# reassign first element in the list
new_list[0] = 'ONE ALL CAPS'
print(new_list)
# add to the list
new_list.append('seven')
print(new_list)
# remove last item from the list
new_list.pop()
print(new_list)
new_list.pop(3)
print(new_list)

# sort and reverse
# both change the list in-place
new_list = ['a', 'e', 'x', 'b', 'w']
num_list = [4,1,7,2,8,3]
print(type(num_list))
new_list.sort()
print(new_list)
num_list.reverse()
print(num_list)

# ====== Dictionaries ======
my_dict = {
  'key1': 'value1',
  'key2': 'value2'
  }
print(my_dict['key1'])

prices_lookup = {
  'apple': 2.99,
  'orange': 1.99,
  'milk': 5.80
}
print(prices_lookup['apple'])

# can nest lists or dictonaries inside dictionaries and have different types

# ====== Tuples ======
# Tuples are similar to lists but are immutable
t = (1,2,3,1)
mylist = [1,2,3]
print(t.count(1))
mytuple = ('a', 'a', 'b', 'c')
# mytuple[0] = 'bbb' will throw an error
print(mytuple)
# built-in methods: t.count() and t.index()

# ====== Sets ======
# unordered collections of unique elements

list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(list(set(list5)))

# ====== If/Elif/Else Statements ======
hungry = True
if hungry:
  print('FEED ME!')
else:
  print("I'm full")

loc = 'Bank'
if loc == 'Auto Shop':
  print('Cars are cool')
elif loc == 'Bank':
  print('Money is kewl')
else:
  print("I'm at the store")

# ====== For Loops ======
mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
  print(num)

for num in mylist:
  # Check for even
  if num % 2 == 0:
    print(num)
  else:
    print(f'odd number: {num}')

list_sum = 0
for num in mylist:
  list_sum += num
print(list_sum)

for letter in 'hello world':
  print(letter)

tup = (1,2,3)
for item in tup:
  print(item)

# Tuple unpacking
mylist = [(1,2), (3,4), (5,6), (7,8)]
print(len(mylist))
for a,b in mylist:
  print(a)

mylist = [(1,2,3), (4,5,6), (7,8,9), (10,11,12)]
for a,b,c in mylist:
  print(b)

# iterate through a dictionary
d = {
  'k1': 1,
  'k2': 2,
  'k3': 3
}
print(d.items())
for key,value in d.items():
  print(value)

# ====== While Loops ======
x = 0
while x < 5:
  print(f'The current value of x is {x}')
  x += 1

# Break, continue, and pass
x = [1,2,3]
for item in x:
  pass
print('end of my script')

mystring = 'Sammy'
for letter in mystring:
  if letter == 'a':
    continue
  print(letter)

mystring = 'Tammy'
for letter in mystring:
  if letter == 'a':
    break
  print(letter)

