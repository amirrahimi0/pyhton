# Initialize a list of 7 zeros
flags = [0]*7

# Repeat the process 3 times
for _ in range(3):
    # Read the number of elements
    num_elements = int(input())

    # Read the elements and split them into a list
    elements = input().split()

    # For each element in the list
    for element in elements:
        # If the first character of the element is 's'
        if element[0] == 's':
            flags[0] = 1
        # If the first character of the element is 'j'
        elif element[0] == 'j':
            flags[6] = 1
        # If the first character of the element is a positive digit
        elif element[0].isdigit() and int(element[0]) > 0:
            flags[int(element[0])] = 1

# Print the number of zeros in the list
print(7 - sum(flags))