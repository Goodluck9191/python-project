score = [110,30,60,60,80,100,86,34,21]

total = 0

for i in score:
    total += i

average = total/len(score)
print(average)

highest = max(score)
print(highest)

lowest = min(score)
print(lowest)


count = 0

for i in score:
    if i > average:
        count +=1

print(f"student score above the average is {count}")