import pandas as pd
import numpy as np
import random

n_rows = 7500

countries = {
"India":["Hyderabad","Bangalore","Mumbai","Delhi"],
"USA":["New York","Chicago"],
"Germany":["Berlin","Munich"],
"UAE":["Dubai"],
"Singapore":["Singapore"],
"UK":["London"],
"Australia":["Sydney"]
}

categories=["Food","Grocery","Pharmacy"]
subscriptions=["Free","Premium"]

traffic=["Low","Medium","High"]
weather=["Clear","Rain","Storm"]

peak=["Breakfast","Lunch","Snack","Dinner","Late Night"]

data=[]

for i in range(n_rows):

    country=random.choice(list(countries.keys()))
    city=random.choice(countries[country])

    category=random.choice(categories)

    premium=random.choice(subscriptions)

    promised_eta=random.randint(15,50)

    traffic_level=random.choice(traffic)

    weather_condition=random.choice(weather)

    delay=0

    if traffic_level=="High":
        delay+=10

    if weather_condition=="Rain":
        delay+=8

    if premium=="Premium":
        promised_eta-=5

    actual_eta=promised_eta+delay+random.randint(-3,8)

    rating=max(
        1,
        min(
            5,
            5-int((actual_eta-promised_eta)/10)
        )
    )

    refund="No"

    compensation="No"

    if actual_eta-promised_eta>10:
        compensation="Yes"

    if actual_eta-promised_eta>20:
        refund="Yes"

    eta_risk="Low"

    if actual_eta-promised_eta>10:
        eta_risk="High"

    dissatisfaction="Low"

    if premium=="Premium" and actual_eta-promised_eta>10:
        dissatisfaction="High"

    data.append({

"order_id":f"NX{i}",

"country":country,

"city":city,

"category":category,

"subscription":premium,

"promised_eta":promised_eta,

"actual_eta":actual_eta,

"traffic":traffic_level,

"weather":weather_condition,

"peak_hour":random.choice(peak),

"customer_rating":rating,

"refund_given":refund,

"compensation_given":compensation,

"eta_failure_risk":eta_risk,

"premium_dissatisfaction":dissatisfaction

})

df=pd.DataFrame(data)

df.to_csv(
"../data/nexdrop_delivery_data.csv",
index=False
)

print("Dataset upgraded")