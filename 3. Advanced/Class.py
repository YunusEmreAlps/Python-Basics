# Class
# Fonksiyonlarda belirli fonksiyonalite ifade eden kodları bir araya getirmeyi görmüştük.
# Class mantığında hem fonksiyonalite hem de veriyi bir arada tutma yoluna bakacağız.

# Class'ın içerisindeki veri(data)'lara attribute, fonksiyonlara method diyeceğiz.

# Diyelim ki bir işyeri çalışanlarını kodumuzla ifade etmek istiyoruz. Sanki bu class mantığı ile uyumlu.
# Her çalışanın farklı farklı özellikleri(attribute)'ları ve yaptıkları şeyler methodları olacak.

# Fonksiyon tanımlarken def kullanıyorduk, class yaratırken class ile tanımlayacağız.

# Class'ın içerisinde method yaratırken, classtan yaratılan objeyi methodlar ilk arguman olarak alırlar.
# İstediğimiz adı verebiliriz ama genellikle self diye geçer.


# ----- Attribute -----
class Employee:
    pass

emp_1 = Employee()

# emp_1 objesin 'a' attribute ekledik
emp_1.a = 4

print(emp_1.a) # 4

# Böyle tek tek belirtmek yerine en başta oluştururken de attribute'ları verebiliriz.
class Employee:
    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        
# Class bunlardan obje oluşturmak için bir kalıptır sadece!
emp1 = Employee("Yunus Emre", "Alpu", 22, 10000)

print(emp1.age)

# Yukarıda yarattığımız bir obje oldu, Employee class'ının bir objesi 
emp2 = Employee("Yunus", "Alpu", 29, 50000)

# Burada yarattığımız bütün attribute'lar instance variable. Her obje(classtan yaratılan instance), kendine özel
# attribute'a sahip.        

# ----- Method -----
class Employee:
    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
    
    def fullname(self):
        print(f"{self.name} {self.last}")
        

emp1 = Employee("Yunus Emre", "Alpu", 22, 10000)        
emp1.fullname()

# self otomatik olarak verildiği için, method tanımında onu belirtmez isek hata alıyoruz.

