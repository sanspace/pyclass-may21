from functools import wraps

def loggy(func): # func = hello
    @wraps(func)
    def inner(*args, **kwargs):
        print("function start")
        r = func(*args, **kwargs) # hello()
        print("function end")
        return r
    return inner

@loggy
def add(x, y):
    return x + y

@loggy
def hi():
    print("hi there")

print(hi)
hi()