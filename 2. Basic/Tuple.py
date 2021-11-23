# --------------------
# Example 7 (Tuple)

# syntax:
# (tuple_name) = ('value_1', 'value_2', 'value_3')

# not changeable
# not appendable

billonaiers = ('Bill Gates', 'Warren Buffett', 'Jeff Bezos', 'Elon Musk')

print(" -",billonaiers[0]) # Bill Gates
print(" -",billonaiers[1]) # Warren Buffett
print(" -",billonaiers[2]) # Jeff Bezos
print(" -",billonaiers[3]) # Elon Musk

print(" -",billonaiers[-1]) # Elon Musk
print(" -",billonaiers[-2]) # Jeff Bezos

# ----------
# syntax: (variable_name)[start: stop: step]
#         [:2] -> That means [0:2]
#         [2:] -> That means [2:last index]

print(" -",billonaiers[:2]) # ('Bill Gates', 'Warren Buffett', 'Jeff Bezos')
print(" -",billonaiers[2:]) # ('Jeff Bezos', 'Elon Musk')

print(" -",billonaiers[::2]) # ('Bill Gates', 'Jeff Bezos')
print(" -",billonaiers[::3]) # ('Bill Gates', 'Elon Musk')

# ----------
# methods
# len
# count
# index

# ----------
# len: total components number
print(" -",len(billonaiers)) # 4


# ----------
# count: total components number
print(" -",billonaiers.count("Jeff Bezos")) # 1
print(" -",billonaiers.count("Bill Gates")) # 1
print(" -",billonaiers.count("Elon Musk")) # 1

# ----------
# index: searches the list for a specified value and returns the position of where it was found
print(" -",billonaiers.index("Jeff Bezos")) # 2