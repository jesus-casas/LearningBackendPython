# Chapter 8: Loops
# I learned in this chapter how to use loops in Python to repeat code blocks.
# My notes to help me quickly reference the syntax and concepts of loops in Python.

# automatically increments by 1
# range(start, stop, step)

print("For loop: from 0 to 9")
for i in range(0, 10):
    print(i)
# Output: 0 1 2 3 4 5 6 7 8 9
# stops at stop - 1

print("=====================================")
print("For loop: from 0 to 9 with step 2")
for i in range(0, 10, 2):
    print(i)
# prints:
# 0
# 2
# 4
# 6
# 8

print("=====================================")
print("For loop: from 3 to 0 with step -1")
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

# Main function calls sum_of_odd_numbers with argument 10
def main():
    end = 10 #ends at 10 - 1 = 9
    result = sum_of_odd_numbers(10)
    print(f"Sum of odd numbers from 0 to {end - 1}: {result}")

if __name__ == "__main__":
    main()