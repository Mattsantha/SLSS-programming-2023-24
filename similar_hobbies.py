# Similar Hobbies Bot
# Author: Matt
# November 14

# Greet User
print("Hello user I am a bot that will calculate your simularity score of hobbies between you and your friend.")

# Get there hobbies
first_person_hobbies = input("Please enter 3 hobbies, seperated by spaces.").lower().split()

second_person_hobbies = input("Please enter the other hobbies, seperated by spaces.").lower().split()

# Calculate there simularity score
simularity_score = 0

for hobbie in first_person_hobbies:
    if hobbie in second_person_hobbies:
        simularity_score += 1

print(f"Your simularity score is {simularity_score}.")
