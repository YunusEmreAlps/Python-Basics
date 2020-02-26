# --------------------
# Example 6 (List)

# syntax:
# (list_name) = ['value_1', 'value_2', 'value_3']

# changeable
# appendable

groups = ['Metallica', 'Queens','Fleetwood Mac', 'Abba', 'Rolling Stones', 'Mamas and Papas', 'Queens', 'Metallica', 'Metallica']

print(" -",type(groups)) # <class 'list'>

print(" -",groups[0]) # Metallica
print(" -",groups[1]) # Queens
print(" -",groups[2]) # Fleetwood Mac
print(" -",groups[3]) # Abba
print(" -",groups[4]) # Rolling Stones
print(" -",groups[5]) # Mamas and Papas

print(" -",groups[-1]) # Metallica
print(" -",groups[-2]) # Metallica
print(" -",groups[-3]) # Queens

# ----------
# syntax: (variable_name)[start: stop: step]
#         [:3] -> That means [0:3]
#         [3:] -> That means [3:last index]


print(" -",groups[:3]) # ['Metallica', 'Queens','Fleetwood Mac']
print(" -",groups[3:]) # ['Abba', 'Rolling Stones','Mamas and Papas', 'Queens', 'Metallica', 'Metallica']
print(" -",groups[::2]) # ['Metallica', 'Fleetwood Mac','Rolling Stones', 'Queens', 'Metallica']
print(" -",groups[::3]) # ['Metallica', 'Abba', 'Queens']

# ----------
# methods
# len
# count
# index
# append
# insert
# pop
# remove 
# sort
# clear

# ----------
# len: total components number
print(" -",len(groups)) # 9


# ----------
# count: total components number
print(" -",groups.count("Metallica")) # 3
print(" -",groups.count("Queens")) # 2
print(" -",groups.count("Abba")) # 1

# ----------
# index: searches the list for a specified value and returns the position of where it was found
print(" -",groups.index("Fleetwood Mac")) # 2
print(" -",groups.index("Mamas and Papas")) # 5
print(" -",groups.index("Queens")) # 1

# ----------
# append: add a specified value in a last index of list
groups.append("Duman")
print(" -",groups)
print(" -",len(groups)) # 10
groups.append("Mor ve otesi")
print(" -",groups) 
print(" -",len(groups)) # 11

# ----------
# insert: add a specified value in a specified index of list -> (list_name).insert(index, value)
groups.insert(2,"Pink Floyd")
print(" -",groups)

# ----------
# sort: sorts the list
groups.sort() # alphabetically
print(" -",groups)

# ----------
# pop: removes a specified value
groups.pop(2) # "Fleetwood Mac" is deleted
print(" -",groups)

# ----------
# remove: removes the first item with the specified value
groups.remove("Pink Floyd") # "Pink Floyd" is deleted
print(" -",groups)

# ----------
# clear: delete all values
groups.clear()
print(" -",groups)