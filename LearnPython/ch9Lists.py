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
    
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # delete the fourth item
    del nums[3]
    print(nums)
    # Output: [1, 2, 3, 5, 6, 7, 8, 9]

    # delete the second item up to (but not including) the fourth item
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    del nums[1:3]
    print(nums)
    # Output: [1, 4, 5, 6, 7, 8, 9]

    # delete all elements
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    del nums[:]
    print(nums)
    # Output: []
    
    print("=====================================")
    print("Example: Tuples")
    
    my_tuple = ("this is a tuple", 45, True)
    print(my_tuple[0])
    # this is a tuple
    print(my_tuple[1])
    # 45
    print(my_tuple[2])
    # True

    my_tuples = [("this is the first tuple in the list", 45, True),("this is the second tuple in the list", 21, False)]
    print(my_tuples[0][0]) # this is the first tuple in the list
    print(my_tuples[0][1]) # 45
    print(my_tuples[1][0]) # this is the second tuple in the list
    print(my_tuples[1][2]) # False
    
    print("=====================================")
    print("Example: First Element")
    
    def get_first_item(items):
        if len(items) == 0: # if the list is empty return "ERROR"
            return "ERROR"
        return items[0]     # return the first element in the list

    print(get_first_item([1, 2, 3])) # 1
    
    print("=====================================")
    print("Example: Reverse List")
    
    items = [1, 2, 3, 4, 5]
    
    def reverse_array(items):
        array = []
        for item in range(len(items)-1,-1,-1):
            array.append(items[item])
        return array
    print(reverse_array(items))
    
    print("=====================================")
    print("Example: Filter Messages")
    
    def filter_messages(messages): # remove the word "dang" from the messages
        # create an empty list to store the filtered messages
        filtered_messages = []
        words_removed = []
        # iterate over each message in the list
        for message in messages:
            words = message.split()
            new_words = []
            removed = 0
            # iterate over each word in the message
            for word in words:
                if word == "dang": # if the word is "dang" increment removed by 1
                    removed += 1
                else:
                    new_words.append(word) # add the word to the new_words list
            filtered_messages.append(" ".join(new_words))
            words_removed.append(removed)

        return filtered_messages, words_removed

    print(filter_messages(["dang it he got me", "I need backup", "Look at it go"]))
    
    print("=====================================")
    print("End of chapter 9 notes")
    
# This block checks if the script is being run directly on system.
# If it is run directly, the main() function is called.
# This is a common pattern used to organize code in Python scripts.
if __name__ == "__main__":
    main()
