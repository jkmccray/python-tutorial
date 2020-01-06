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