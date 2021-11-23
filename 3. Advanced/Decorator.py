# Decorator
# Decorator'lar başka fonksiyonları parametre olarak kabul edip yeni bir fonksiyonalite ile yeni bir fonksiyon döndüren yapılardır.

def print_func():
    print("Hello")
    pass


def decorator_func(func):    
    def wrapper_func():
        return func()
    
    return wrapper_func
    pass


decorated_print = decorator_func(print_func)
decorated_print()

# Var olan fonksiyona fonksiyonu değiştirmeden yeni bir davranış kazandıracağız

def decorator_func(func):    
    def wrapper_func():
        print(f"Name of the function is {func.__name__}")
        return func()
    
    return wrapper_func
    pass


decorated_print = decorator_func(print_func)
decorated_print()

# @func un yapınca aslında fonksiyonumuzu func'a input olarak veriyoruz.

@decorator_func
def print_func():
    print("Hello")
    pass

print_func()


def func(name, number):
    print(f"Name: {name}, Number: {number}")
    pass

func("Yunus Emre", 402)

def decorator_func(func):    
    def wrapper_func(*args):
        print(f"Name of the function is {func.__name__}")
        return func(*args)
    
    return wrapper_func
    pass

@decorator_func
def func(name, number):
    print(f"Name: {name}, Number: {number}")
    pass


func("Yunus Emre", 402)





