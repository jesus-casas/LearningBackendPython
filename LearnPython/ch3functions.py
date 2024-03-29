# Chapter 3: Functions 
# I learned in this chapter how to define functions, pass arguments to functions, 
# return values from functions, and use default argument values.
# My notes to help me quickly reference the syntax and concepts of functions in Python.

# Function to calculate the area of a circle
def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result

# Function to subtract two numbers
def subtract(a, b):
    result = a - b
    return result

# Function to add armor to a player's health
def add_armor(h, a):
    new_health = h + a
    print_health(new_health)

# Function to print the player's health
def print_health(new_health):
    print(f"The player now has {new_health} health")

# Function that does nothing and returns None
def my_func():
    print("I do nothing")

# Function to create a warrior title and increase power
def become_warrior(first_name, last_name, power):
    full_name = first_name + " " + last_name + " the warrior"
    new_power = power + 1
    return full_name, new_power

# Function to add two numbers (demonstrating parameters vs arguments)
def add(a, b):
    return a + b

# Function with a default argument value
def get_greeting(email, name="there"):
    print("Hello", name, "welcome! You've registered your email:", email)

# Function to create a title for a person based on their job
def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return title

# Main function to demonstrate the usage of other functions
def main():
    # Demonstrate area_of_circle
    radius = 5
    area = area_of_circle(radius)
    print(f"Area of circle with radius {radius}: {area}")

    # Demonstrate subtract
    difference = subtract(10, 5)
    print(f"10 - 5 = {difference}")

    # Demonstrate add_armor and print_health
    health = 10
    armor = 5
    add_armor(health, armor)

    # Demonstrate my_func
    my_func()

    # Demonstrate become_warrior
    title, power = become_warrior("Frodo", "Baggins", 5)
    print(f"{title} has a power level of {power}")

    # Demonstrate add (parameters vs arguments)
    sum = add(5, 6)
    print(f"5 + 6 = {sum}")

    # Demonstrate get_greeting with default argument
    get_greeting("frodo@example.com")
    get_greeting("bilbo@example.com", "Bilbo")

    # Demonstrate get_title
    title = get_title("Gandalf", "The Grey", "wizard")
    print(title)

# Entry point of the program
if __name__ == "__main__":
    main()
