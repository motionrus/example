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