# Parental Bot 
# Author: Matt
# November 15 2023

# Greet user
print("Hello I am your parental bot and I will be checking in on you to see if you need help. So answer my questions truethly.")


# Ask questions
score = 0

questions = [
    "Did you eat?", 
    "Did you study?", 
    "Did you do your laundry?", 
    "Did you call grandma?"
]

# Get score
for question in questions:
    print(question)

    answers = input().lower().strip(",.?!")

    if answers == "yes":
        score += 1
    else: score += 0

if score == 0:
        print("I'm coming over.")
elif score <=2:
        print("Ok.")
elif score >=3:
        print("Good!")
