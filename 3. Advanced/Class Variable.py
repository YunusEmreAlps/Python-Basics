# Class Variable

class Employee:
    raise_percent = 0.5
    num_emp = 0
    
    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        Employee.num_emp += 1
        
    def apply_raise(self):
        self.pay += (self.pay * Employee.raise_percent) # self.raise_percent
        
        
emp_1 = Employee("Yunus Emre", "Alpu", 22, 5000)
emp_2 = Employee("Yusuf Emre", "Alpu", 28, 4000)

# Instance Variable: Class'tan yaratılan objelerin kendilerine özgü değişkenleri. Bu örnekte name, last, age, pay
# Class Variable: Class'tan yaratılan tüm objelerde paylaşılan değişkenler.

# Instance Variable her obje için farklı olabilir, ama class variable hepsi için aynı olmak zorunda

# Tüm çalışanlar arasında hangi verinin paylaşılmasını isteyebilirim? Mesela şirket herkese aynı yüzdelik zam uyguluyorsa
# bunu class variable olarak tutabilirim

emp_1.apply_raise()
print(emp_1.pay)

# emp1.raise_percent (ilk olarak instance'a bakar, eğer bulamazsa class variable olarak var mı diye bakar)

print(emp_1.__dict__)
print(Employee.__dict__)


Employee.raise_percent = 1.06

# Class variable'ı class üzerinde güncellemek demek tüm objeler için günceller


emp_1.raise_percent = 1.07

# Class variable instance üzerinde güncellemek sadece o objenin üzerinde günceller.

print(Employee.num_emp)
















