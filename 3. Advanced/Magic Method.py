# Magic Methods
# Magic Method'ları kullanarak bazı built-in davranışları değiştirebiliriz.
# Magic Methodlar __ ile çevrilidir. Bunlara dunder method da denir.

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
        
    # Objenin okunabilir bir tanımını oluşturur.
    def __str__(self):
        print(f"name: {self.name}, last: {self.last}, age: {self.age), pay: {self.pay}")

    def __add__(self, other):
        return self.pay + other.pay                
        
emp_1 = Employee("Yunus Emre", "Alpu", 22, 5000)
emp_2 = Employee("Yusuf Emre", "Alpu", 28, 4000)







