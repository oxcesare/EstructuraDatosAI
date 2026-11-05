numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(numbers_squared)          # <map object at 0x7f8c2b5c1d60>
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

# Using map with multiple iterables
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
summed_numbers = map(lambda x, y: x + y, numbers1, numbers2)
print(list(summed_numbers))     # [5, 7, 9]
