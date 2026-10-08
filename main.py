# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.



from datetime import datetime
# import pandas
# import random
# import smtplib
# import os
# 
# # import os and use it to get the Github repository secrets
# MY_EMAIL = os.environ.get("MY_EMAIL")
# MY_PASSWORD = os.environ.get("MY_PASSWORD")
# 
# today = datetime.now()
# today_tuple = (today.month, today.day)
# 
# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"])                  : data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])
# 
#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )






import requests
import os



api_key = os.environ.get("OWM_API_KEY")
# city_country = 'Huelva,Spain'
lat = 50.075539 # Prague
lon = 14.437800 # Prague
# lat = 37.261421 # Huelva
# lon = -6.944722 # Huelva
cnt = 4

# api_endpoint_current = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
# api_endpoint_current = f"https://api.openweathermap.org/data/2.5/weather?q={city_country}&appid={api_key}"
# api_endpoint_forecast = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = { 'lat': lat, 'lon': lon, 'appid': api_key, 'cnt': cnt }

response = requests.get( owm_endpoint, params=parameters )

response.raise_for_status()

data = response.json()

forecasts = data['list']

is_umbrella_needed = False

weather_codes = []



for forecast in forecasts:

    weather_items = forecast['weather']

    for weather_item in weather_items:

        weather_code = weather_item['id']

        if weather_code < 700:

            is_umbrella_needed = True

        weather_codes.append(weather_code)



print(weather_codes)
print(is_umbrella_needed)

