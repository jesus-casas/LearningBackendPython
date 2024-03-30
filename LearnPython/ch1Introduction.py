# Chapter 1: Introduction
# I learned in this chapter how to print strings, perform basic math operations.
# My notes to help me quickly reference the syntax and concepts of functions in Python.

def main():
    # Example: Printing strings
    print("This is an example of printing strings:")
    print("Hello World")
    print('Hello World')
    print("=====================================")

    # Example: Basic math operations
    print("This is an example of basic math operations:")
    print(5 + 1)
    print("=====================================")

    # Example: Variables
    print("This is an example of using variables:")
    my_variable = 5
    print(my_variable)
    my_variable = 10
    print(my_variable)
    print("=====================================")

    # Example: Math operations with variables
    print("This is an example of math operations with variables:")
    a, b = 1, 2
    sum = a + b
    difference = a - b
    product = a * b
    quotient = a / b
    print("Sum:", sum)
    print("Difference:", difference)
    print("Product:", product)
    print("Quotient:", quotient)
    print("=====================================")

    # Example: Types of variables
    print("This is an example of different types of variables:")
    name_with_double_quotes = "boot.dev"
    x = 5
    y = -5
    z = 5.2
    is_true = True
    is_false = False
    sword_name, sword_damage, sword_length = "Excalibur", 10, 200
    print("=====================================")

    # Example: f-strings
    print("This is an example of using f-strings:")
    name = "Yarl"
    age = 37
    race = "dwarf"
    print(f"{name} is a {race} who is {age} years old.")
    print("=====================================")

    # Example: None variable
    print("This is an example of using a None variable:")
    enemy = None
    print(enemy is None)
    print("=====================================")

    # Example: Math with strings
    print("This is an example of math with strings:")
    first_name = "Lane "
    last_name = "Wagner"
    full_name = first_name + last_name
    print(full_name)
    print("=====================================")

# This block checks if the script is being run directly on system.
# If it is run directly, the main() function is called.
# This is a common pattern used to organize code in Python scripts.
if __name__ == "__main__":
    main()
