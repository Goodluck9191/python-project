
def reverse_string(input_string):
    stack = []

    
    for char in input_string:
        stack.append(char)

    reversed_string = ""

    
    while stack:
        reversed_string += stack.pop()

    return reversed_string



user_input = input("Enter a string: ")

reversed_output = reverse_string(user_input)

print("Reversed string:", reversed_output)