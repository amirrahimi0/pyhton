"""
 You have a combination lock with multiple wheels, 
 each displaying numbers. 
 The code figures out the minimum number of turns needed 
 to make the lock display a specific passcode.

"""
# Read the length of the password
password_length = int(input())

# Read the password
password = input()

# Initialize the total time to enter the password
total_time = 0

# For each character in the password
for i in range(password_length):
    # Read the available characters
    available_chars = input()

    # Find the position of the password character in the available characters
    position = available_chars.index(password[i])

    # Add the time to enter the character to the total time
    if position < 5:
        total_time += position
    else:
        total_time += 9 - position

# Print the total time to enter the password
print(total_time)