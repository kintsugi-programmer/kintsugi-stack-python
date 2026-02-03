enemy = None # no value

print(enemy is None) # True
print(enemy is not None) # False

enemy = "Voldemort"

print(enemy is None) # False
print(enemy is not None) # True

# True
# False
# False
# True

str_none = "None"
actual_none = None

print(str_none) # None
print(actual_none) # None

print(type(str_none)) # <class 'str'>
print(type(actual_none)) # <class 'NoneType'>
