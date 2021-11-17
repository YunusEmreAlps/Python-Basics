# Dictionaries

grades = {
    "Deniz": 80,
    "Ege": 72,
    "Gizem": 95
}

print(grades["Deniz"]) # 80
print(grades["Ege"]) # 72
print(grades["Gizem"]) # 95


students = {
    "Deniz": {
        "not": 80,
        "ogrenci_no": 703
    },
    "Ege": {
        "not": 72,
        "ogrenci_no": 408
    },
    "Gizem": {
        "not": 95,
        "ogrenci_no": 690
    }
}

print(students["Deniz"]) # {"not": 80, "ogrenci_no": 703}
print(students["Ege"])   # {"not": 72, "ogrenci_no": 408}
print(students["Gizem"]) # {"not": 95, "ogrenci_no": 690}

print(students["Deniz"]["not"]) # 80
print(students["Ege"]["not"])   # 72,
print(students["Gizem"]["not"]) # 95

print(students["Deniz"]["ogrenci_no"]) # 703
print(students["Ege"]["ogrenci_no"])   # 408
print(students["Gizem"]["ogrenci_no"]) # 690

students["Ege"]["not"] += 5

print(students) 

print(len(students)) # 3
print(len(students["Deniz"])) # 2


del(grades["Ege"])
print(grades)