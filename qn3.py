arr = [1,1,1,2,2,2,3,3,3,4,5,6]

updated_array = []

for i in arr:
    if i  not in updated_array:
        updated_array.append(i)
print(updated_array)
