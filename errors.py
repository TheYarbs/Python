# A simple script with errors
def greet(name):
    print("Hello" + name)  # Error: Missing space between "Hello" and the name

def add_numbers(a, b):
    return a + b  # Works fine

# Main program
name = input("Enter your name: ")  # Error: The user might not provide input in some contexts
greet()  # Error: Missing the required argument

result = add_numbers(5, "10")  # Error: Mixing integer and string types
print("The result is: " + result)  # Error: Cannot concatenate string and non-string types
