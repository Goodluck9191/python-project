arr = [10, 20, 30, 40, 50]

k = 2

for i in range(k):
    last = arr[-1]
    arr.pop()
    arr.insert(0, last)

print(arr)