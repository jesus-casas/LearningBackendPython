# Chapter 5 Testing and Debugging
def unlock_achievement(before_xp, ach_xp, ach_name):
    new_xp = before_xp + ach_xp
    ach_message = "Achievement Unlocked: " + ach_name
    return new_xp, ach_message

# Stack trace is an error message that shows the sequence of function calls that led to the error
def create_stats_message(strength, wisdom, dexterity):
    total = strength + wisdom + dexterity
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
    return msg
