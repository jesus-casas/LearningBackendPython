# Chapter 4: Scope 
# I learned in this chapter trying to access a variable outside of its scope will result in an error
# My notes to help me quickly reference the syntax and concepts of scope in Python.

def main():
    # Example 1: Subtracting two numbers
    def subtract(x, y):
        return x - y

    # If we try to access the x or y variable here, it will result in an error
    # because they are not defined in this scope.
    result = subtract(5, 3)
    print(f"Result of subtraction: {result}")

    # Example 2: Calculating the area of a circle
    pi = 3.14

    def get_area_of_circle(radius):
        return pi * radius * radius

    area = get_area_of_circle(5)
    print(f"Area of the circle: {area}")

if __name__ == "__main__":
    main()
