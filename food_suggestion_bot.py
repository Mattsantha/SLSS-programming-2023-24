#Food Suggestion Bot
# Author: Matt
# 6 October 2023

# A bot that asks the user what their favorite food is. 
#Based on that food, t will classify the type/genre/cuisine of the food, then give a restaurant suggestion.

import random
import time

# Introduce the bot to the user
# Ask the user what their favorite food is
print("Hello, Iam here to suggets you a restaurant.")
time.sleep(1)
fave_food = input("To help me suggest a restaurant, tell me what your favorite food is.")
time.sleep(1)

# Italian Cuisine
italian_food = ["pasta", "pizza", "canneloni", "tramisu"]
# Add another cuisine that our bot should make a suggestion for
# Japenese Cuisine
japenese_food = ["sushi", "ramen", "mochi", "sashimi"]


# If they answer with Italian food,
# Suggest an Italian restaurant
if fave_food.lower().strip("!,.?") in italian_food:
    print("I see that you might like italiaj food🍝")
    time.sleep(1)
    print("I suggest Broli Kitchen.")
    print("Here's their address.")
    print("186-8180 No 2 Rd, Richmond, BC.")
elif fave_food.lower().strip("!,.?") in japenese_food:
    print("Based on your favorite fod it seems you like japenese food.")
    time.sleep(1)
    print("I recomend Gami sushi.")
    print("Address: 10111 No. 3 Rd #126, Richmond, BC V7A 1W6")
else:
    print("Sorry I'n not sure what kind of food that is.")
    print("I can't, unfortunately recomend a restaurant")


