### Lambdas ###

def sum_two_values(first_value, second_value):
    return first_value + second_value

print(sum_two_values(2, 4))

def make_random_operation(first_value, second_value):
    return first_value * second_value - 3

print(make_random_operation(2, 4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(2)(2, 4))

lambda_func = sum_three_values(3)
print(lambda_func(2, 4))
