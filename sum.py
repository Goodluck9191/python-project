arr =[1, 2, 3, 4, 5, 6, 7, 8]

even = 0
odd = 0
TotalEven = 0
TotalOdd = 0

for i in range (len(arr)):
    if (arr[i] % 2 == 0):
        even = even + 1
        TotalEven = TotalEven + arr[i]
    else:
        odd = odd + 1
        TotalOdd = TotalOdd + arr[i]


print('Number of even is:',even)
print('NUmber of odd is:', odd)
print('Total number of even:', TotalEven)
print('Total number of odd:', TotalOdd)


