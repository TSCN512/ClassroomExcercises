import smtplib
import datetime as dt #alias for clarity
import random
import pandas

sender_email = "ThisIsMe@goodwebsite.com"
sender_password = "GoodPassword"
receiver_email = "ThisIsThem@betterwebsite.com"
receiver_pwd="BetterPassword"


Dob = dt.datetime(year=2001, month=1, day=23) #this would be for testing, a real world app would just use current date
now = dt.datetime.now()

birth_csv= pandas.read_csv("birthdays.csv") #also have sample birthdate/recipient within csv
#for row in birth_csv[Dob.month==birth_csv.month][Dob.day==birth_csv.day].name:
#    print(row)
#           the above logic works with syntax, but is recommended to split into two lines,
#           troubleshooting suggests the above code is unclear/implicit
#           refactor below
birth_csv = birth_csv.loc[Dob.month==birth_csv.month]
birth_csv = birth_csv.loc[Dob.day==birth_csv.day]
#we have the birthday recipients, now format them into name:email pairs
birthday_dict= {row[0]:row.email for index,row in birth_csv.iterrows()}
print(birthday_dict)

pick = random.choice(range(1,4)) #determines which letter to send

with smtplib.SMTP(host="smtp.live.com", port=587) as connection:
    connection.starttls()
    connection.login(user=sender_email, password=sender_password)
    with open(f"letter_templates/letter_{pick}.txt") as file:
        for name in birthday_dict:
            bdayWishes = file.read()
            bdayWishes= bdayWishes.replace("[NAME]", name)
            connection.sendmail(from_addr=sender_email, to_addrs=birthday_dict[name], msg=f"Subject:Nice!\n\n{bdayWishes}")

