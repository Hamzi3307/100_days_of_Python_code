import pandas as pd

data = pd.read_csv("Day25\weather.csv")

# print(data["temp"])

# print(data)

data_dict = data.to_dict()
# print(data_dict)
# print(data_dict["temp"])
# print(data_dict["condition"])
# print(data_dict["day"])

# The average temprature

# temp = data["temp"].to_list()
# avg = sum(temp)/len(temp)
# print(avg)

# 2nd way to calculate average is a mean()

print(f"Average Temprature: {data['temp'].mean()}")
print(f"Maximum Temprature: {data['temp'].max()}")
print(f"Manimum Temprature: {data['temp'].min()}")

