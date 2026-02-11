arr = [1, 2, 3, 4, 2, 4, 7,4,1]

new_arr =[]

for i in arr:
    if i not in new_arr:
        new_arr.append(i)

print(f"the new array is {new_arr}")