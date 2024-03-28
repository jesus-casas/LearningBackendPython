# Chapter 4 Loops
for i in range(0, 10):
    print(i)
# Output: 0 1 2 3 4 5 6 7 8 9
# automatically increments by 1
# range(start, stop, step)
# stops at stop - 1

for i in range(0, 10, 2):
    print(i)
# prints:
# 0
# 2
# 4
# 6
# 8

for i in range(3, 0, -1):
    print(i)
# prints:
# 3
# 2
# 1

# In this example, the function sum_of_odd_numbers takes in an integer end 
# and returns the sum of all odd numbers from 0 to end - 1.
def sum_of_odd_numbers(end):
    total = 0
    for i in range(0, end):
        if i % 2 == 1:
            total += i
    return total

