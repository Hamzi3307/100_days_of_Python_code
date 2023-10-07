import pandas as pd
import datetime as dt
import random, smtplib
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
data = pd.read_csv("Day32\Birthday Wisher\\birthdays.csv")
for _, row in data.iterrows():
    # print(row.day)
    
    # 2. Check if today matches a birthday in the 
    # birthdays.csv
    now = dt.datetime.now()
    if now.day == row['day'] and now.month == row['month']:
        print("Today is Birthday of ", row['name'])

        # 3. If step 2 is true, pick a random letter from 
        # letter templates and replace the [NAME] with the
        # person's actual name from birthdays.csv
        file_path = f"Day32\Birthday Wisher\letter_templates\letter_{random.randint(1,3)}.txt"
        with open(file_path) as file:
            file = file.read()
            mail = file.replace("[NAME]", row['name'])

        # 4. Send the letter generated in step 3 to that person's email address.
        # to_addr = row["email"]
        # from_addr = "hamzi3307@gmail.com"
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=from_addr, password="password")
        #     connection.send_message(to_addrs=to_addr, from_addr=from_addr, msg=mail)
        print(mail)
