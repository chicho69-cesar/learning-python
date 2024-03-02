### Higher Order Functions ###

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(2, 5, sum_one))
print(sum_two_values_and_add_value(2, 5, sum_five))

print('\n')


### Closures ###

def sum_ten(original_value):
    def sum_value(value):
        return value + original_value

    return sum_value

add_closure = sum_ten(1)
print(add_closure(5))

print((sum_ten(5))(1))

print('\n')


### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# Map

def multiply_two(value):
    return value * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda value: value * 2, numbers)))

# Filter

def filter_greater_than_ten(value):
    return value > 10

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda value: value > 10, numbers)))

# Reduce

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))
print(reduce(lambda first_value, second_value: first_value + second_value, numbers))
