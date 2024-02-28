# Read the length of the strings
length = int(input())

# Read the first and second strings
first_string = input()
second_string = input()

# Initialize the counter for the number of differences
difference_count = 0

# Iterate over each character in the strings
for i in range(length):
    # If the characters at the current position are different
    if first_string[i] != second_string[i]:
        # Increment the difference count
        difference_count += 1

# Print the total number of differences
print(difference_count)