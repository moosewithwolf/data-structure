
# immutable object
# ex)str, tuple, int, float, bool

# mutable object
# ex)list, dict, set, bytearray

# [start:end]  # slice the list from start to end       
# [:] -  [::-1]  # reverse the list

x = [1,2,3]
y = x.copy()# shallow copy
# y = x  # reference copy
# y = x[:]  # shallow copy
# y = list(x)  # shallow copy
# y = x.copy()  # shallow copy


x = [1,2,3]
y = x
print(x is y) # check if x and y are the same object
print(x == y) # check if x and y have the same value

x = [1,2,3]
y = x.copy() # shallow copy
print(y)
print(x)
print(x is y)
print(x == y)

# deep copy
import copy
x = [[1,2],[3,4]]
y = copy.deepcopy(x)
print(y)
print(x)
print(x is y)
print(x == y)
print(x[0] is y[0])
print(x[0] == y[0])

# shallow copy
x = [[1,2],[3,4]]
y = x.copy()
print(y)
print(x)
print(x is y)
print(x == y)
print(x[0] is y[0])
print(x[0] == y[0])

# convert other type like tuples, list
x = (1,2,3)
y = list(x)
print(y)

x = [1,2,3]
y = tuple(x)
print(y)
