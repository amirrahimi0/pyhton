# Read the input string
input_string = input()

# For each character in the input string
for index, char in enumerate(input_string):
    # Repeat the character based on its position in the string
    repeated_char = char * index

    # Append the rest of the string after the character
    rest_of_string = input_string[index:]

    # Construct the output string
    output_string = repeated_char + rest_of_string

    # Print the output string
    print(output_string)