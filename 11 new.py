expression = input("Enter expression: ")

stack = []
pairs = {')': '(', ']': '[', '}': '{'}
valid = True

for ch in expression:
    if ch in "([{":
        stack.append(ch)

    elif ch in ")]}":
        if not stack or stack[-1] != pairs[ch]:
            valid = False
            break
        stack.pop()

if stack:
    valid = False

if valid:
    print("Expression is Balanced")
else:
    print("Expression is NOT Balanced")