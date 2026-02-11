expr = '{[()()]}'
stack = []
valid = True

for ch in expr:
    if ch in "{[](":
        stack.append(ch)
    else:
        if not stack:
            valid = False


if valid == True:
    print("valid")
else:
    print('Invalid')