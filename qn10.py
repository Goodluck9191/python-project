# Function to reverse string using stack
def reverse_string(input_string):
    stack = []

    # Push all characters into stack
    for char in input_string:
        stack.append(char)

    reversed_string = ""

    # Pop characters from stack
    while stack:
        reversed_string += stack.pop()

    return reversed_string


# Main Program
user_input = input("Enter a string: ")

reversed_output = reverse_string(user_input)

print("Reversed string:", reversed_output)