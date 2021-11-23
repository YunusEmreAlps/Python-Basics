# Class ve Static Method

# ----- Class Method -----
# @classmethod decorator methodu ilk arguman olarak instance almak yerine class'ı alacak şekilde günceller.

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

Employee.set_raise(2.05)

print(emp_1.raise_percent)
print(emp_2.raise_percent)
print(Employee.raise_percent)

# Alternative Constructor
# Diyelim ki bize class'ı oluştururken input olarak string veriyorlar ve bizim bundan name, age gibi bilgileri kendimiz çıkarmamız lazım.


emp_1_str = "Yunus Emre-Alpu-22-5000"
emp_2_str = "Yusuf Emre-Alpu-28-4000"

emp_1 = Employee.from_string(emp_1_str)
emp_2 = Employee.from_string(emp_2_str)

print(emp_1.__dict__)
print(emp_2.__dict__)

# Her seferinde kendim parse etmek yerine bir method yazarak bu işlemi daha kolay bir hale getirebilirim. 

# ----- Static Method -----
# Regular methodlar(ilk gördüklerimiz), class'ın instance'ını (oluşturulan objeyi), methodlara otomatik olarak 
# arguman olarak veriyordu(self olarak). Class methodları class'ı otomatik olarak arguman olarak veriyor
# Statik methodlar otomatik olarak bir şey vermeyen methodlar olacak

# Instance veya class'a methodun içerinde erişim olmuyorsa statik olarak tanımlamak daha iyi olabilir. 

Employee.holiday_print("working day")
Employee.holiday_print("weekend")











