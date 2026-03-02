

rainfall = [120, 95, 180, 240, 200, 60, 40, 30, 70, 110, 160, 190]

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

max_rainfall = max(rainfall)
max_month = months[rainfall.index(max_rainfall)]

total_rainfall = sum(rainfall)

print("Month with maximum rainfall:", max_month, "-", max_rainfall, "mm")
print("Total seasonal rainfall:", total_rainfall, "mm")