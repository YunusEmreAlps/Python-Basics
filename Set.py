# Set

S = set()
print(type(S))

arr = [1, 2, 3, 4] # list
S = set(arr) 
print(S) # {1, 2, 3, 4}

arr = [1,2,3,4,1,2] # list
S = set(arr)
print(S) # {1, 2, 3, 4}

tup = (1, 2, 3, 4, 1) # tuple
S = set(tup)
print(S) # {1, 2, 3, 4}

msg = "Hello, Are you there?"
S = set(msg)
print(S)

# --------- len() ---------

S = set([1, 2, 3, 4, 5])
print(len(S)) # 5

S = set((1, 2, 3, 3, 4)) 
print(len(S)) # 4

S = set((1, 2, 3, 3, 2)) 
print(len(S)) # 3

# --------- add() ---------
S = {1, 2, 3, 4, 5}
S.add(6)
print(S) # {1, 2, 3, 4, 5, 6}
S.add(5)
print(S) # {1, 2, 3, 4, 5, 6}

# --------- remove() ---------
print(S) # {1, 2, 3, 4, 5, 6}
S.remove(2)
print(S) # {1, 3, 4, 5, 6}
# S.remove(9) -> KeyError

# --------- discard() ---------
print(S) # {1, 3, 4, 5, 6}
S.discard(10)
print(S) # {1, 3, 4, 5, 6}
S.add(10)
print(S) # {1, 3, 4, 5, 6, 10}
S.discard(10)
print(S) # {1, 3, 4, 5, 6}

# --------- difference() ---------
S1 = set([1, 5, 10])
S2 = set([2, 5, 3])

print(S1) # {1, 5, 10}
print(S2) # {2, 5, 3}

print(S1.difference(S2)) # {1, 10}
print(S1 - S2) # {1, 10}

print(S2.difference(S1)) # {2, 3}
print(S2 - S1) # {2, 3}

# --------- symmetric_difference() ---------
print(S1) # {1, 5, 10}
print(S2) # {2, 5, 3}

print(S1.symmetric_difference(S2)) 
# {1, 2, 3, 10}
print(S2.symmetric_difference(S1)) 
# {1, 2, 3, 10}

# --------- intersection() ---------
print(S1) # {1, 5, 10}
print(S2) # {2, 5, 3}

print(S1.intersection(S2)) # {5}
print(S2.intersection(S1)) # {5}

print(S1 & S2) # {5}
print(S1 - (S1-S2) ) # {5}

S1 = S1.intersection(S2)
print(S1)

# --------- union() ---------
S1 = set([1, 5, 10])

print(S1) # {1, 5, 10}
print(S2) # {2, 5, 3}

print(S1.union(S2)) # {1, 2, 3, 5, 10}
print(S2.union(S1)) # {1, 2, 3, 5, 10}

# --------- isdisjoint() ---------
S3 = set([12, 11])

print(S1) # {1, 5, 10}
print(S2) # {2, 5, 3}
print(S3) # {12, 11}


print(S1.isdisjoint(S2)) # False
print(S2.isdisjoint(S1)) # False
print(S3.isdisjoint(S2)) # True
print(S3.isdisjoint(S1)) # True

# --------- issubset() ---------
S3 = set([2, 5])

print(S1) # {1, 5, 10}
print(S2) # {2, 5, 3}
print(S3) # {2, 5}


print(S1.issubset(S2)) # False
print(S2.issubset(S1)) # False
print(S3.issubset(S2)) # True

# --------- issuperset() ---------
print(S1) # {1, 5, 10}
print(S2) # {2, 5, 3}
print(S3) # {2, 5}


print(S1.issuperset(S2)) # False
print(S2.issuperset(S1)) # False
print(S2.issuperset(S3)) # True










