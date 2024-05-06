# Chapter 10 in Python Course on Dictionaries
# I learned in this chapter how to use dictionaries in Python to store key-value pairs.
# My Notes help me to remember the syntax and how to use dictionaries in Python.

# Dictionaries in Python are used to store data values in key -> value pairs. 
# Dictionaries are a great way to store groups of information.

def main():
    print("Example: Creating a dictionary")
    # use curly braces
    # add key-value pairs
    car = {
        "brand": "Tesla",
        "model": "3",
        "year": 2019
    }
    print(car)
    print("=====================================")
    print ("Example: Duplicate Keys")
    # Because dictionaries rely on unique keys, you can't have two of the same key in the same dictionary. 
    # If you try to use the same key twice, the first value will simply be overwritten.
    car_brands = {
        "brand": "Tesla",
        "brand": "Toyota",
        "brand": "Ford"
    }
    print(car_brands) # prints {'brand': 'Ford'}
    # The key "brand" is repeated three times, but only the last value is stored in the dictionary.
    
    print("=====================================")
    
    

# This block checks if the script is being run directly on system.
# If it is run directly, the main() function is called.
# This is a common pattern used to organize code in Python scripts.
if __name__ == "__main__":
    main()
