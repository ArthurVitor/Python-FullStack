variable = 'I am beautiful'

def Func1():
    print(variable)


def Func2():
    global variable
    variable = 'I am prettier than you'
    print(variable)


Func1()  # I am beautiful
Func2()  # I am prettier than you
print(variable)  # I am prettier than you

