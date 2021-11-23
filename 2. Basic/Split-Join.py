# Split

# --------- split() ---------

msg = "Hello, How are you?"
print(msg.split(" "))

fruits = "lemon,orange,apple"
print(fruits.split(","))

# --------- join() ---------

arr = ["lemon", "orange", "apple"]
print(",".join(arr)) # lemon,orange,apple
print("-".join(arr)) # lemon-orange-apple
print("/".join(arr)) # lemon/orange/apple
print(" ".join(arr)) # lemon orange apple
