"""
  This function helps someone find his seat in the conference hall.

  Args:
      row: row number (1-indexed).
      col: seat number (1-indexed).

  Returns:
      A string indicating the direction (Left or Right), row number, and seat number.
  """
# Read the input values
a, b = map(int, input().split())

# Determine the direction based on the value of b
direction = "Left" if b > 10 else "Right"

# Calculate the first number based on the value of a and b
first_number = 11 - a if b > 10 else a

# Calculate the second number based on the value of b
second_number = 21 - b if b > 10 else a

# Construct the result string
result = f"{direction} {first_number} {second_number}"

# Print the result
print(result)