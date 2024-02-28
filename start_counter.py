# Read the dimensions of the grid
rows, cols = map(int, input().split())

# Initialize the counter for the number of stars
star_count = 0

# Iterate over each row in the grid
for _ in range(rows):
    # Read the current row
    row = input()

    # Count the number of stars in the current row and add it to the total count
    star_count += row.count("*")

# Print the total number of stars
print(star_count)