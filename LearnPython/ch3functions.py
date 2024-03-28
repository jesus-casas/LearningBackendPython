# Chapter 3 learning about functions

# defining a function with a parameter needs def keyword
def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result

radius = 5
area = area_of_circle(radius)
print(area)
# 78.5

# defining a function with multiple parameters
def subtract(a, b):
    result = a - b
    return result

# calling the function need to create the function first before calling it
def main():
    print("Fantasy Quest is booting up...")
    print("Game is running!")

main()

# Order of operations we need to define the function before calling 
# the entry point main() function
def main():
    health = 10
    armor = 5
    add_armor(health, armor)

def add_armor(h, a):
    new_health = h + a
    print_health(new_health)

def print_health(new_health):
    print(f"The player now has {new_health} health")

    # call entrypoint last
main()

# Function with no return

def my_func():
    print("I do nothing")
    return
    # will return None
    
# Multiple return values example use comma to separate the values
def become_warrior(first_name, last_name, power):
    full_name = first_name + " " + last_name + " the warrior"
    new_power = power + 1
    return full_name, new_power


# Don't edit below this line


def main():
    test("Frodo", "Baggins", 5)
    test("Bilbo", "Baggins", 10)
    test("Gandalf", "The Grey", 9000)


def test(first_name, last_name, power):
    title_string, power = become_warrior(first_name, last_name, power)
    print(title_string, "has a power level of:", power)


main()

# Arguments VS Parameters example
# a and b are parameters
def add(a, b):
    return a + b

# 5 and 6 are arguments
sum = add(5, 6)

# DEFAULT VALUES FOR FUNCTION ARGUMENTS
def get_greeting(email, name="there"):
    print("Hello", name, "welcome! You've registered your email:", email)

# PRINTING VS RETURNING 
def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return title


# Don't touch below this line


def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")