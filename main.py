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

#Below is teacher's answer, a little different than mine and interesting:
 #def add_new_country(country_visited, times_visited, cities_visited):
  # new_country = {}
  # new_country["country"] = country_visited
  # new_country["visits"] = times_visited
  # new_country["cities" = cities_visited
  # travel_log.append(new_country)]






#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

print(travel_log[2]["country"])

print("You've visited " + str(travel_log[2]["country"]) + " " + str(travel_log[2]["visits"]) + " times.")

print("You've been to " + str(travel_log[2]["cities"][0]) + " and " +  str(travel_log[2]["cities"][1]) + ".")




