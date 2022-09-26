# Write a function1 that receives function2 as a parameter and returns the value of the function2 executed
# Make function1 return two functions who receive differente numbers as parameters

def function1(func, *args, **kwargs):
    return func(*args, **kwargs)


def function2(name):
    return f'Hi, {name}'


def function3(name, saudation):
    return f'{saudation} {name}'

out = function1(function2, 'Luiz')
print(out)