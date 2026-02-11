attendace = [60,65, 70, 85, 90, 95]


updated_attendance = []

for j in attendace:
    list = j + 10
    list = min(list, 100)
    updated_attendance.append(list)

print(updated_attendance)