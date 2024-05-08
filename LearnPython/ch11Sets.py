# Chapter 11 in Python Course on Sets
# I learned in this chapter how to use sets in Python to store unique values.
# My Notes help me to remember the syntax and how to use sets in Python.

# Sets in Python are used to store unique values.
# Sets are a great way to store groups of information.

def main():
    print("Chapter 11 in Python Course on Sets")
    
    print("=====================================")
    print("Example: Creating a set")
    fruits = {'apple', 'banana', 'grape'}
    print(type(fruits))
    # Prints: <class 'set'>

    print(fruits)
    # Prints: {'banana', 'grape', 'apple'}

    print("=====================================")
    print("Example: Adding elements to a set")
    # fruits from previous example
    # Syntax: set_name.add('element')
    fruits.add('pear')
    print(fruits)
    # Prints: {'banana', 'grape', 'pear', 'apple'}
    
    print("=====================================")
    print("Example: Empty set")
    # Syntax: set_name = set()
    fruit = set()
    fruit.add('pear')
    print(fruits)
    # Prints: {'pear'}


    print("=====================================")
    print("End of chapter 11 notes")

# This block checks if the script is being run directly on system.
# If it is run directly, the main() function is called.
# This is a common pattern used to organize code in Python scripts.
if __name__ == "__main__":
    main()
