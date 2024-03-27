# Chapter 6 Computing with Numbers
# Python NUMBERS
2 + 1
# 3

2 - 1
# 1

2 * 2
# 4

3 / 2
# 1.5 (a float)

my_int = 5
my_float = 5.5

#Floor division
7 // 3
# 2 (an integer) - rounds 

#Exponent
# reads as "three squared" or
# "three raised to the second power"
3 ** 2
# 9

#changing in place
player_score = 4
player_score = player_score + 1
# player_score now equals 5

# Plus equals
star_rating = 4
star_rating += 1
# star_rating is now 5

#Scientific Notation
print(16e3)
# Prints 16000.0

print(7.1e-2)
# Prints 0.071

# Underscores for readability
num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000

# Logical Operators
print(True and True)
# prints True

print(True or False)
# prints True

#Python Comparison Operators
print((True or False) and False)
# prints False

#Bitwise Operators
# A 1 in binary is the same as True, while 0 is False
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def can_create_bits(user_permissions):
    ans = can_create_guild & user_permissions
    return ans

def can_review_bits(user_permissions):
    ans = can_review_guild & user_permissions
    return ans

def can_delete_bits(user_permissions):
    ans = can_delete_guild & user_permissions
    return ans
    
def can_edit_bits(user_permissions):
    ans = can_edit_guild & user_permissions
    return ans

#0101 = 5
#&
#0111 = 7
#=
#0101 = 5

# Bitwise OR operator
def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    ans = glorfindel | galadriel | elendil | elrond
    return ans

#0101
#|
#0111
#=
#0111

# NOT operator
print(not True)
# Prints: False

print(not False)
# Prints: True
