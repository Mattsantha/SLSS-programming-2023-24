# Star wars bot
# Matt Santha
# Oct 16 2023

import time

# Create a bot that with a series of yes or no questions that will decied weather your on the light side or dark side

print("Hello I am a Star wars chatbot that will decied if you belong on the light or dark side.")
time.sleep(1)
print("Please answer these yes or no questions honestly.")
time.sleep(1)
print("Let us begin!")
time.sleep(1)

#Ask the user if they like capes and the coulor red
cape_question = input("Do you like wearing capes?")

red_question = input("Do you like the coulor red?")

# Decied if the user is on the dark or light side based on the questions
if cape_question.lower().strip(",.?!") or red_question.lower().strip(",.?!") == "yes":
    print("You belong to the dark side of the force.")
else: 
    print("I sence the light side within you.")