# with open("Day25\weather.csv") as file:
#     data = file.readlines()
#     print(data)

import csv

# with open("Day25\weather.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row)

# take the values of 2nd Column in a list

with open("Day25\weather.csv") as file:
    data = csv.reader(file)
    temp = []
    for row in data:
        if row[1] != "temp":
            temp.append(int(row[1]))
    print(temp)
