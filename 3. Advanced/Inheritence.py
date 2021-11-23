# Inheritence (Kalıtım)
# Inheritance belirttiğimiz başka classlardaki method ve attribute'lara erişmemizi sağlar.
# Diyelim ki farklı tipte çalışanlar yaratmak istiyorum IT ve HR olsun.


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
        
    @classmethod
    def set_raise(cls, amount):
        cls.raise_percent = amount

    @classmethod
    def from_string(cls, userstr):
        name, last, age, pay = userstr.split('-')
        return cls(name, last, int(age), float(pay))
    
    @staticmethod
    def holiday_print(day):
        if(day == "weekend"):
            print("This is an off day")
        else:
            print("This is not an off day")
                
        
emp_1 = Employee("Yunus Emre", "Alpu", 22, 5000)
emp_2 = Employee("Yusuf Emre", "Alpu", 28, 4000)

# Hangi class'tan inherit etmek istediğimizi parantezin içine yazıyoruz.
# Inherit ettiğimiz class'a super/parent class, inherit edene de child/subclass deniyor.

class IT(Employee):
    raise_percent = 1.2
    
    def __init__(self, name, last, age, pay, lang):
        super().__init__(name, last, age, pay)
        self.lang = lang
    pass

# Employee raise_percent attribute'unu kullanmak yerine içine belirtiğimizi kullanıyor. Kendi içerisinde bulabilirse kullanıyor. Bulamazsa inherit ettiği yere bakıyor.

# IT'nin içine hiç bir şey yazmasak da, Employee'nin özelliklerine erişimi var.
# IT içerisinde bulamazsa aradığını, inherit ettiği yere gidip bakacak. IT'nin içerisinde __init__ methodu yok.O yüzden Employee classının içine bakacak.
    

it_1 = IT("Yunus", "Alp", 22, 10000, "Python")
print(it_1.__dict__)

class IK(Employee):
    raise_percent = 1.5
    
    def __init__(self, name, last, age, pay, experience):
        super().__init__(name, last, age, pay)
        self.experience = experience
    def print_exp(self):
        print(f"This employee has {self.experience} years of experience")
    
    pass


ik_1 = IK("Yun", "Alp", 22, 10000, 10)
print(ik_1.__dict__)








