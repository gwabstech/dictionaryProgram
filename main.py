from calendar import c


names = {
    "Abu": 81,
    "ali": 78,
    "hauwa": 99,
    "kopat": 65
}

# list in dictionry
travel_log = {
    "France": {
        "cities_visited":["paris","Lile","Dijon"],
        "To Consider":["Kano","Kaduna"]
        },
    "Nigeria": {
        "cities_visited":["Kaduna","Kano","Zamfara","Katsina","Kebbi","Sokoto","Abuja"],"total state visited":7
    }
}

cities = ["Kaduna", "Kano", "Zamfara", "Katsina",
          "Kebbi", "Sokoto", "Abuja", "Niger"]


#dictionry in list

travel_log1 = [
    {
       "Country": "Nigeria",
       "cities_visited": cities,
       "totalCity visited": len(cities)
       
    },
    {
        "Country": "Nigeria",
        "cities_visited": cities,
        "totalCity visited": len(cities)
    }
    
]

def add_new_Country(country,cities):
    travel_log1.append({"country": country, "cities_visited": cities, "no_of_visit": 10})
    print(travel_log1)
   
    
studentGrades = {}

for i in names:
    score = names[i]
    if names[i] >= 91:
        studentGrades[i] = "Outstanding"
    elif names[i] >= 81:
        studentGrades[i] = "Excelent"
    elif names[i] >= 71:
        studentGrades[i] = "Good"
    else:
        studentGrades[i] = "making progress"
        
for grade in studentGrades:
    print(studentGrades[grade])
    print("")
for city in travel_log:
    for i  in travel_log[city]:
        print(travel_log[city][i])
print(travel_log1)
add_new_Country("Niger",["Damagaran","Madawa","Maradi"])