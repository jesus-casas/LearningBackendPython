# Chapter 7 Comparison Operators
# I learned in this chapter how to use comparison operators in Python.
# Objective: This program demonstrates the use of comparison operators in Python.
5 < 6 # evaluates to True
5 > 6 # evaluates to False
5 >= 6 # evaluates to False
5 <= 6 # evaluates to True
5 == 6 # evaluates to False
5 != 6 # evaluates to True

#Example #2 
def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = edward_height == mustang_height
    is_alphonse_edward_same = edward_height == alphonse_height
    is_winry_alphonse_same = winry_height == alphonse_height
    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same

# IF statement
def print_status(player_health):
    if player_health == 0:
        print("dead")
    print("status check complete")

# is in operator

# If-else statement
if score > high_score:
    print('High score beat!')
elif score > second_highest_score:
    print('You got second place!')
elif score > third_highest_score:
    print('You got third place!')
else:
    print('Better luck next time')

#Tip IF statement dont need a comparison operator
# if is_big:
    # ...
# if is_big == True:
    # ...
# Both act the same way