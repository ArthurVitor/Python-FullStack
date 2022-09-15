def f(var):
    print(var, type(1))

def dumb():
    return f

var = dumb()

if __name__ == '__main__':
    var('daw')