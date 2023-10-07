import smtplib, datetime as dt, random

email = "hamzi3307@gmail.com"
password = "Ha23ha23@!"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.send_message(from_addr=email, to_addrs="hamzi@yahoo.com", msg="Subject: Hello\n\n HAPPY BIRTHDAY")

with smtplib.SMTP("smtp.gamil.com") as conn:
    conn.starttls()
    conn.login(user=email, password=password)
    conn.send_message(from_addr=email, to_addrs="hamzi@gmail.com", msg="Subject: ")


with open("Day32\Birthday Wisher (Day 32) start\quotes.txt") as file:
    data_list = file.readlines()
    
print(data_list[89], "\n\n\n", len(data_list))

now = dt.datetime.now()
if now.weekday==0:
    quote = data_list[random.choice(data_list)]
    print(quote)
    
quote = random.choice(data_list) # data_list[]
print(quote.split('-'))
