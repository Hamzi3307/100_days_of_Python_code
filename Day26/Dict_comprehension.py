print("# Exercise 26.4")
sentence = "in the working copy of 'Day26/States Game/main.py', LF will be replaced by CRLF the next time Git touches it"

result = {key : len(key) for key in sentence.split()}

print(result)

print("\n\n# Exercise 26.5")

import random
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

temp_of_day = {key: random.randint(10,19) for key in days_of_week}

Ftemp_of_day = {key: (val *9/5)+32 for (key, val) in temp_of_day.items()}

print(temp_of_day,"\n\n", Ftemp_of_day)