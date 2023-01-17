#print("Hello World!")

import random


answer = "no"

while answer == "no":
    Destinations = ["California", "Virginia", "New York", "Austrailia"]
    for destination in Destinations:
            choice_one = random.choice(Destinations)
            print(choice_one)
            break
    answer = input("Do you like selected location? ")


answer = "no"

while answer == "no":
    Restaurants = ["Russo's", "Italiano's", "Green Seed Vegan", "Torchy's"]
    for restaurant in Restaurants:
            choice_two = random.choice(Restaurants)
            print(choice_two)
            break
    answer = input("Do you like selected restaurant? ")


answer = "no"

while answer == "no":
    Transportation = ["Train", "Airplane", "Boat", "Teleport"]
    for transportation in Transportation:
            choice_three = random.choice(Transportation)
            print(choice_three)
            break
    answer = input("Do you like selected mode of transportation? ")



answer = "no"

while answer == "no":
    Entertainment = ["Sports", "Cooking", "Nature", "Movies"]
    for entertainment in Entertainment:
            choice_four = random.choice(Entertainment)
            print(choice_four)
            break
    answer = input("Do you like selected form of entertainment? ")


print("You have completed Day Trip Generator")

print(choice_one)
print(choice_two)
print(choice_three)
print(choice_four)



