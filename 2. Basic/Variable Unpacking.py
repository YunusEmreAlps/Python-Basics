# Variable Unpacking
x = 4
y = 7
print(x, y) # 4 7

m, n = (4,7)
print(m, n) # 4 7

x, y, z = (4, 7, 11)
print(x, y, z)

x, _ = (9, 7)
print(x)

x, y, *z = (4, 7, 11, 4, 21)
print(x) # 4
print(y) # 7
print(z) # [11, 4, 21]
type(z)  # list

x, y, *_ = (4, 7, 11, 12, 13)
print(x) # 4
print(y) # 7

x, y, *z, t = (4, 7, 11, 4, 21)
print(x) # 4
print(y) # 7
print(z) # [11, 4]
print(t) # 21


x, y, *z, t, u = (4, 7, 11, 4, 21, 32, 2)
print(x) # 4
print(y) # 7
print(z) # [11, 4, 21]
print(t) # 32
print(u) # 2
# --------- ---------