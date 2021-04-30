travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, times, cities):
  travel_log.append({"country": country, "visits": times, "cities": cities})






#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

print(travel_log[2]["country"])

print("You've visited " + str(travel_log[2]["country"]) + " " + str(travel_log[2]["visits"]) + " times.")

print("You've been to " + str(travel_log[2]["cities"][0]) + " and " +  str(travel_log[2]["cities"][1]) + ".")




