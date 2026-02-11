score  = [12, 25,67,44,67,89,90,76,89]

highest = max(score)
lowest = min(score)
print(f"The maximum sccore and minimum score are {highest} and {lowest}")

total = 0

for i in score:
    total = total + i

average = total/len(score)

print(f"the average is {average}")


count =0
for i in score:
    if i > average:
        count = count +1

print(f'student above the average is {count}')

