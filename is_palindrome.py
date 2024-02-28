# Function to check if a string is a palindrome
def is_palindrome(string):
    n = len(string) - 1
    for i in range(n):
        if string[i] != string[n - i]:
            return "NO"
    return "YES"

# Prompt the user for input and check if it is a palindrome
string = input("Enter a string: ")
print("Palindrome:", is_palindrome(string))
        
    

