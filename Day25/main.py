import pandas as pd

data = pd.read_csv("Day25\Central-Park-Squirrel-Census-Squirrel-Data-2018.csv")

print(data["Primary Fur Color"].value_counts())

gray_data = data[data["Primary Fur Color"] == "Gray"]
black_data = data[data["Primary Fur Color"] == "Black"]
cinnamon_data = data[data["Primary Fur Color"] == "Cinnamon"]

count_gray = len(gray_data)
count_red = len(cinnamon_data)
count_black = len(black_data)

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [count_gray, count_red, count_black]
}

data = pd.DataFrame(data_dict)
data.to_csv("Day25/data.csv")