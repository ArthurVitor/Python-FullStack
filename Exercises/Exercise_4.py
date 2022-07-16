# Write a function1 that receives function2 as a parameter and returns the value of the function2 executed

def function1(*args):
    return args


def function2():
    print('Hey! Hey!')


if __name__ == '__main__':
    function1(function2())