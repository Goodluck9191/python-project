string = "hello"

stack = []

for i in string:
    stack.append(i)

reverse = ''
while stack:
    reverse = reverse + stack.pop()
print(reverse)