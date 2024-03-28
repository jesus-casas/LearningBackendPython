# Chapter 4 Scope 
# Trying to access a variable outside of its scope will result in an error
def subtract(x, y):
    return x - y
result = subtract(5, 3)
print(x)
# ERROR! "name 'x' is not defined"

# Correct way to access the result
pi = 3.14

def get_area_of_circle(radius):
    return pi * radius * radius
