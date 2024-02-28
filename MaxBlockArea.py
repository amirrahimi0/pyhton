import math

def calculate_block_area(n, m, a, b):
    """
    Calculates the maximum area of blocks that can be formed given the dimensions and block size.
    
    Parameters:
    - n (int): The length of the x-axis.
    - m (int): The length of the y-axis.
    - a (int): The size of each block along the x-axis.
    - b (int): The size of each block along the y-axis.
    
    Returns:
    - int: The maximum area of blocks that can be formed.
    """
    xaxis = 1
    yaxis = 1
    
    for i in range(n + 1):
        if a > math.ceil((n - (i * a)) / (i + 1)):
            xaxis = i
            break
    
    for i in range(m + 1):
        if b > math.ceil((m - (i * b)) / (i + 1)):
            yaxis = i
            break
    
    return xaxis * yaxis

t = int(input("Enter the number of test cases: "))
answers = []

for _ in range(t):
    n, m, a, b = map(int, input("Enter the values of n, m, a, b: ").split())
    answers.append(calculate_block_area(n, m, a, b))

print("Maximum areas of blocks:")
for answer in answers:
    print(answer)
