# --------------------
# Example 8 (Dictionaries)

# syntax:
# (dict_name) = ('key1':'value1', 'key2':'value2', 'key3':'value3')

stars = {
        'Ben Simmons':'Philedelphia 76',
        'Luka Doncic':'Dallas Mavericks',
        'Trae Young':'Atalanta Hawks',
        'James Harden':'Houston Rockets',
        'Klay Thomson':'Golden State'
        }

print(" -",stars.get('Ben Simmons')) # Philedelphia 76
print(" -",stars.get('Luka Doncic')) # Dallas Mavericks
print(" -",stars.get('Trae Young'))  #Atalanta Hawks
print(" -",stars.get('James Harden')) # Houston Rockets
print(" -",stars.get('Klay Thomson')) # Golden State
print(stars)