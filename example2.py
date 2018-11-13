# example mro

class O: pass
class G(O): pass
class E(G): pass
class F(G): pass
class D(E): pass
class C(E,F): pass
class B(D,F): pass
class A(C,B): pass
print(A.__mro__)

# result
# (<class '__main__.A'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.E'>, <class
# '__main__.F'>, <class '__main__.G'>, <class '__main__.O'>, <class 'object'>)
# 
# example class, difference between attribute class and attribute method

class MixinExample:
    data = 'class'
    
    def __init__(self, data):
        self.data = data
    
    def result(self):
        return('self.data = "{}", MixinExample.data = "{}"'.format(self.data, MixinExample.data))

a = MixinExample('a')
b = MixinExample('b')
print(a.result())
print(b.result())

# result
# self.data = "a", MixinExample.data = "class"
# self.data = "b", MixinExample.data = "class"
#
# call class mehod

class CalledExample:
    def printer(self, name):
        self.name = name
        print(self.name)

x = CalledExample()
x.printer("First message")
CalledExample.printer(x, "Second message")

# result
# First message
# Second message
#
# Easy undestand decorate func. How it works, example

def makebold(func):
    def wrapped():
        return '<b>{}</b>'.format(func())
    return wrapped

def makeitalic(func):
    def wrapped():
        return '<i>{}</i>'.format(func())
    return wrapped


@makeitalic
@makebold
def hello():
    return 'hello'

hello()

# '<i><b>hello</b></i>'
# Example 2

def my_shiny_new_decorator(func):
    
    def wrapper_func():
        
        print("Я - код, который отработает до вызова функции")
        func()
        print("А я - код, срабатывающий после")
    
    return wrapper_func
    

@my_shiny_new_decorator
def another_stand_alone_function():
    print("Оставь меня в покое")


another_stand_alone_function()

#my_shiny_new_decorator(another_stand_alone_function)()



# выведет:
# Я - код, который отработает до вызова функции
# Оставь меня в покое
# А я - код, срабатывающий после
#
# Пример функции с педачей аргументов в декоратор

def decorate_func(func):
    def wrapper(first, second):
        print("Передали {}, {}".format(first, second))
        func(first, second)
        print("Конец декорируемой функции")
    return wrapper


#@decorate_func
def print_name(first, second):
    print('Имя: {}, Фамилия: {}'.format(first, second))


decorate_func(print_name)('Иван', 'Иванов')
# or
# print_name('Иван', 'Иванов') # it's syntax sugar

# выведет:
# Передали Иван, Иванов
# Имя: Иван, Фамилия: Иванов
# Конец декорируемой функции

# Передача аргументов в декорируемую функцию
def decorate_multiple_args(func):
    def wrapper_func(*args, **kwargs):
        print("before call decorate func".upper())
        print(args)
        print(kwargs)
        print("END")
        func(*args, **kwargs)
        print("after call decorate func".upper())
        print("END")
    return wrapper_func

@decorate_multiple_args
def print_args(*args, **kwargs):
    print("positional args:".upper())
    i = 0
    for arg in args:
        i += 1
        print('{} lists arg = "{}"'.format(i, arg))
    print("named kwargs:".upper())
    i = 0
    for key in kwargs:
        i += 1
        print('key "{}" have value "{}"'.format(key, kwargs[key]))

print_args([1,2,3], {'a': 1, 'b': 2, 'c': 3}, 4, 5, d=4, e={'A':1,'B':2})

# result
# BEFORE CALL DECORATE FUNC
# ([1, 2, 3], {'a': 1, 'b': 2, 'c': 3}, 4, 5)
# {'d': 4, 'e': {'A': 1, 'B': 2}}
# END
# POSITIONAL ARGS:
# 1 lists arg = "[1, 2, 3]"
# 2 lists arg = "{'a': 1, 'b': 2, 'c': 3}"
# 3 lists arg = "4"
# 4 lists arg = "5"
# NAMED KWARGS:
# key "d" have value "4"
# key "e" have value "{'A': 1, 'B': 2}"
# AFTER CALL DECORATE FUNC
# END


# Расширение функционала декораторов, передача аргументов в декоратор и декорируемую функцию
#
arg1 = 'decorate'
arg2 = 'decorate2'
arg_func = 'arg_func'
def decorate_multiple_args(*args):
    print(args)
    def decorating_func(func):
        def wrapped(*args, **kwargs):
            func(*args, **kwargs)
        return wrapped
    return decorating_func

@decorate_multiple_args(arg1, arg2)
def decorated_func(*args, **kwargs):
    print(args, kwargs)

decorated_func(arg_func)

# result
# ('decorate', 'decorate2')
# ('arg_func',) {}


# Следующий пример с использованием декораторов, передавая параметры в декоратор
# 

def font(size):
    def decorate(func):
        def wrapped(text):
            print("<font size={}>{}</font>".format(size, text))
        return wrapped
    return decorate

def html(text):
    print(text)

# result
# In [103]: font(4)(html)("Hello World4")
# 			<font size=4>Hello World4</font>

@font(7)
def html(text):
    print(text)

# result
# In [106]: html("Hello World")
# 			<font size=7>Hello World</font>

# CHECK DIFFERENT TIMEOVER EXTEND LIST
#

FILE = '/home/rus/Загрузки/logic.memory.profiler.txt'
def benchmark(func):
    def wrapper(first):
        import time
        time_now = time.clock()
        func(first)
        print((time.clock() - time_now)*10**6)
    return wrapper

@benchmark
def add_list(list_file):
    list_file.extend([1])

@benchmark
def add_list2(list_file):
    list_file += [1]

@benchmark
def add_list3(list_file):
    list_file = list_file + [1]

with open(FILE, 'r') as f:
    list_file = f.readlines()

print(len(list_file))
add_list(list_file)
add_list2(list_file)
add_list3(list_file)

# RESULT
# 4018294
# 5.000000001587068
# 5.999999999062311
# 157233.0000000015
