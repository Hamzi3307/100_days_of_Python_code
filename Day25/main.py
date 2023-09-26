import pandas as pd

data = pd.read_csv("Day25\Central-Park-Squirrel-Census-Squirrel-Data-2018.csv")

print(data["Primary Fur Color"].value_counts())

gray_data = data[data["Primary Fur Color"] == "Gray"]
black_data = data[data["Primary Fur Color"] == "Black"]
cinnamon_data = data[data["Primary Fur Color"] == "Cinnamon"]

print(len(gray_data))
print(len(cinnamon_data))
print(len(black_data))