# Chapter 9 in Python Course on Lists
# I learned in this chapter how to use lists in Python to store multiple items in a single variable.
# My Notes help me to remember the syntax and how to use lists in Python.
# Called lists not arrays in Python

def main():
    # Example: Creating a list strings, numeric values, and boolean values can all be stored in a list
    inventory = ["Iron Breastplate", "Healing Potion", "Leather Scraps"]

    # Declaring lists on multiple lines to improve readability
    flower_types = [
    "daffodil",
    "rose",
    "chrysanthemum"
    ]
    # Example: Lists can contain different types of variables
    player_ages = [
        23,
        18,
        31,
        42
    ]
    
    #Counting in Python starts at 0
    # Indexes: Bob = 0, Lane = 1, Alice = 2, Breanna = 3 
    names = ["Bob", "Lane", "Alice", "Breanna"]

    # Example: Accessing elements in a list
    print("Example: Accessing elements in a list")
    best_languages = ["JavaScript", "Go", "Rust", "Python", "C"]
    print(best_languages[1])
    # prints "Go", because index 1 was provided
    print(best_languages[3])
    # prints "Python", because index 3 was provided
    
    print ("=====================================")
    print("Example: List length")
    
    length = len(best_languages)
    print(length) 
    # prints 5, because there are 5 elements in the list
    
    print ("=====================================")
    print("Example: List updates")
    
    best_languages[1] = "Ruby"
    print(best_languages[1])
    # prints "Ruby" now, because we updated the value at index 1 to "Ruby"
    
    print ("=====================================")
    print("Example: List append")
    
    best_languages.append("Go")
    print(best_languages)
    # prints ["JavaScript", "Ruby", "Rust", "Python", "C", "Go"]
    # because we added "Go" to the end of the list with .append()
    
    print ("=====================================")
    print("Example: List pop")
    
    vegetables = ["broccoli", "cabbage", "kale", "tomato"];
    last_vegetable = vegetables.pop()
    print(last_vegetable)
    # vegetables = ['broccoli', 'cabbage', 'kale']
    # last_vegetable = 'tomato'
    
    print ("=====================================")
    print("Example: Counting elements in a list")
    
    broccoli_count = 0
    cabbage_count = 0
    kale_count = 0
    for i in range(0, len(vegetables)):
        if vegetables[i] == "broccoli":
            broccoli_count += 1
        elif vegetables[i] == "cabbage":
            cabbage_count += 1
        elif vegetables[i] == "kale":
            kale_count +=1
    print("Broccoli count:", broccoli_count)
    print("Cabbage count:", cabbage_count)
    print("Kale count:", kale_count)
    
    print ("=====================================")
    print("Example: No-index Syntax")
    
    trees = ['oak', 'pine', 'maple']
    for tree in trees:
        print(tree)
    # Prints:
    # oak
    # pine
    # maple
    
    print ("=====================================")
    print("Example: List Find an item in a list")
    
    current_inventory = ["Iron Breastplate", "Healing Potion", "Leather Scraps"]
    def contains_leather_scraps(items):
        found = False
        # 
        for item in items:
            if item == "Leather Scraps":
                found = True
        # 
        return found
    print(contains_leather_scraps(current_inventory))
    
    print ("=====================================")
    print("Example: List Find the Difference Between Two Lists")
    
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

    for i in range(0, len(old_character_levels)):
        if new_character_levels[i] > old_character_levels[i]:
            print(i) # prints 2, 3, 7 the indexes of the levels that increased

    print ("=====================================")
    print("Example: Find max number with help from negative infinity")
    
    numbers = [1, 2, 3, 4, 5]
    def find_max(numbers):
        # float("-inf") is negative infinity float("inf") is positive infinity
        max_number = float("-inf")
        for number in numbers:
            if number > max_number:
                max_number = number
        return max_number
    print(find_max(numbers)) # prints 5
    
    print("=====================================")
    print("Example: Modulo Operator in Python")
    
    for i in range(0, 10):
        
        if i % 2 == 1: # if i is odd print
            print(i)
    
    print("=====================================")
    print("Example: Slicing Lists")
    # my_list[ start : stop : step ]
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numbers)  # Gives [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Example: numbers[:3]")
    print(numbers[:3]) # Gives [0, 1, 2]
    print("Example: numbers[3:]")
    print(numbers[3:]) # Gives [3, 4, 5, 6, 7, 8, 9]
    print("Example: numbers[::2]")
    print(numbers[::2]) # Gives [0, 2, 4, 6, 8]
    print("Example: numbers[-3:]")
    print(numbers[-3:]) # Gives [7, 8, 9]
    
    print("=====================================")
    print("Example: List Operations - Concatenation")
    
    total = [1, 2, 3] + [4, 5, 6]
    print(total)
    # Prints: [1, 2, 3, 4, 5, 6]
    
    print("=====================================")
    print("Example: List Operations - Contains")
    
    fruits = ["apple", "orange", "banana"]
    print("banana" in fruits)
    # Prints: True
    
    print("=====================================")
    print("Example: List Operations - Deletion")
    
    
    print("=====================================")
    print("Example: Tuples")
    
    
    print("=====================================")
    print("Example: First Element")
    
    
    print("=====================================")
    print("Example: Reverse List")
    
    print("=====================================")
    print("Example: Filter Messages")
    
    print("=====================================")
    print("End of chapter 9 notes")
    
# This block checks if the script is being run directly on system.
# If it is run directly, the main() function is called.
# This is a common pattern used to organize code in Python scripts.
if __name__ == "__main__":
    main()
