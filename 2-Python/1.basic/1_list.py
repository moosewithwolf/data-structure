# - install Jupyter
#   $ jupyter lab
# - install Anaconda


## basic syntax of python
x = [1, 2, 3]
l = len(x)  # length of x
print(x)  # print x
print(l)  # print length of x

# list comprehension -> create a new list based on an existing one
# ^ syntax: [expression for item in iterable if condition]
my_list = [x for x in range(10) if x % 2 == 0]  # list of even numbers from 0 to 9
print(my_list)  # print my_list

# spells with list comprehension
spelling = [x for x in "SHINSEONG"]  # list of characters in "hello world"
print(spelling)  # print spelling

# real logic when using list comprehension
result = []
for i in "hello":
    result.append(i)

# for in range
for i in range(5):  # loop from 0 to 4
    print(i)  # print i
# for in list
for i in [1, 2, 3]:  # loop through the list
    print(i)  # print i
# for in string
for i in "hello":  # loop through the string
    print(i)  # print i

c_degs = [-10, 0, 10, 100]
# convert celsius to fahrenheit
f_degs = [
    c * 9 / 5 + 32 for c in c_degs
]  # list comprehension to convert celsius to fahrenheit
print(f_degs)  # print fahrenheit degrees

basket = ["    apple", "banana    ", "orange  ", "kiwi"]
fruit = [item.strip() for item in basket]  # strip whitespace from each fruit
print(fruit)  # print fruit without whitespace

square = [n * n for n in range(2, 10)]
print(square)  # print square of numbers from 2 to 9

a, b, c, d = 0, 2, 3, 4
print("b:" + str(b))
items = ["hello", [1, 2], (a, c, b, d)]
length = [len(item) for item in items]
print(length)


store = [
    ("apple", 1),
    ("banana", 3),
    ("kiwi", 6),
]
# create a list of tuples with fruit and its price
order = [price * 2 for (name, price) in store]
print(order)

# dictionary
order = [{name: price * 3} for (name, price) in store]
print(order)
order = [(name, price * 3) for (name, price) in store]
print(order)
order = {name: price * 3 for name, price in store}
print(order)
order = dict([(name, price * 3) for name, price in store])
print(order)
order = [dict(name=name, price=price * 3) for (name, price) in store]
print(order)

# filtered list
vector = [2, 4, 6]
my_vec = [x * x for x in vector if x > 3]
print(my_vec)  # print squares of vector elements greater than 3

# Summary: Features of lists
# • Information in a list is stored contiguously in memory
# • location of the information can be calculated
# • location = start of the list + index * size of each element
# • Efficiency issues
# • It takes the same time to access any of the elements
# • Slow to move elements around (i.e. add and delete elements from within the list)
