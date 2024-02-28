# Read the input string
input_string = input()
# Count the occurrences of 'G', 'R', and 'Y' in the string
count_g = input_string.count('G')
count_r = input_string.count('R')
count_y = input_string.count('Y')

# Check the conditions for printing "nakhor lite"
if count_r > 2 or (count_r + count_y > 3) or count_y == 5 or count_r == 5:
    print("nakhor lite")
# If none of the conditions are met, print "rahat baash"
else:
    print("rahat baash")