# Chatbot
# Author: Ubial
# date 20 september 2023

# Greet the user
print("Hello there")
print("I'm a crude Chatbot, here to talk to you.")

# Get the user's name and store it in a varible
user_name = input("So... What's your name?")

#Respeond with the user's name in a friendly way
print(f"It's good too meet you {user_name}")

# Ask the user what thier favorite food is
fav_food = input("Whats your favorite food?")

# Make the comment about their favorite food but NOT BE TERRIBLY REPETITIVE 
# Create a list of possible responese
list_of_food_responses = [
    f"Oh, I've never had {fav_food} before.", 
    "Mmmmm. That sounds good!",
    "I heard that that is delicious",
    "Cool."
]
# Choose one of those responses randomly
import random
random_food_responce = random.choice(list_of_food_responses)

# Print out that chosen response
print(random_food_responce)