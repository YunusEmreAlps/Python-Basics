# Closure
# Outer(dış) fonksiyonu çağırdıktan sonra bile inner function'ın outer function scope'una erişebilmesi

def outer():
    msg = "Hey"
    
    def inner():
        print(msg)
        
    return inner()

outer()


# Bu örnek daha önce yaptıklarımızdan farklı değiş, inner function enclosing scope'a erişip msg değişkenine bastırabilirdi.

# --------- **kwargs ---------

def outer():
    msg = "Hey"
    
    def inner():
        print(msg)
        
    return inner

f = outer()
print(f)


# Şimdi outer function'ı çağırmış olduk ve bize içinde tanımlanan inner function'ı obje olarak döndürmüş oldu.
# Function call yapmadığım sürece obje olarak kalacak.

f()




def outer(msg):
    msg = msg
    
    def inner():
        print(msg)
        
    return inner

hi_f = outer("Yunus Emre Alpu")
hey_f = outer("Yunus E")
print(f)

hi_f()
hey_f()