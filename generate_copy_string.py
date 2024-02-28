# This script is used to create a string that repeats the phrase "copy of " a certain number of times, 
# and then appends another string to the end. The number of repetitions and the final string are both 
# provided by the user. The script reads these values from the standard input, processes them, and 
# prints the resulting string. This could be useful in situations where you need to generate a string 
# with a repeating pattern, followed by a specific ending.

# Read the input values
a, b = map(str, input().split())

# Repeat "copy of " a times
copies = "copy of " * int(a)

# Concatenate the copies with b
result = f"{copies}{b}"

# Print the result
print(result)