# Chip Rater
# Author: Matt Santha
# 1 November 2023
# Interview people about thier
# perception of how delicious chips are
# based on a set of questions
# In the end, we'll give an aggegate score.


# Greet the user
print("please answer the follwojg questions based on the chip you just ate.")

# create a list of questions ot ask
questions = [
    "How crispy is that chip on a scale from 1-5? 5 is very crispy. 1 is mushy.",
    "How would you rate the taste from 1-5? 5 being best taste ever. 1 being i would ratehr eat dirt.",
    "from 1-5 how would you rate the packaging? 5 is I would buy this just for the packaging. 1 is I bought this because I am blind."
]

final_score = 0

# Ask the questions to the user
for question in questions:
    print(question)

    # Store thier response
    rating = int(input().strip(",.?!"))
    final_score += rating

# Do some math 
average_score = final_score / len(questions)

# Present the results to the user
print(f"The avergae score of this chpi is: {average_score:.2f} / 5")
