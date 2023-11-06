# World Traveller Bot
# Author: Matt
# November 6 2023

import time

# Ask for users name and greet them
user_name = input("I am a World Traveller Bot whats your name?")
                  
print(f"Hello {user_name} my purpose is to tell you how many conintients you've been to.")
time.sleep(1)

print("Now lets begin.")

#Ask the user question
contintients_list = ["Asia", "Europe", "North America", "South America", "Australia", "Africa", "Antarctica"]

places = 0

for contintient in contintients_list:
    contintient_visited = input(f"Have you been to {contintient}?(Yes/No)")
    if contintient_visited.lower().strip(",.?!") == "yes":
        places += 1

print(f"Cool {user_name} you've visited {places}/7 continents!")
