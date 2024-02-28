# Read the number of words to print
n = int(input())

# Limit the value of n between 0 and 7
n = max(0, min(n, 7))

# List of words starting with 's'
s_words = ["snake", "summer", "sail", "space", "science", "software", "syntax"]

# Print the first n words from the list
for i in range(n):
    print(s_words[i])