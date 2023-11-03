# Olympic Judging 
# Author: Matt Santha
# 3 November 2023


# Greet User
print("Hello welcome to this Olympic judging program! You will need to input 5 scores")

numbers=["first", "second", "third", "fourth", "five"]

scores=0

# Ask the user thier scores
print("The preformer juts did a triple scorpin back flip and then twenty round offs in a row!!!")
for number in numbers:
    scores+=float(input(f"What is the {number} score given from 1-10? 1 being terrible and 10 being amazing."))

print(f"Your Olympic score is: {scores /5 :.2f}")