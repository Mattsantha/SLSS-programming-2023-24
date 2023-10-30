#  Bubble Tea Popularity Algorithm
# Author: Matt Santha
# Date: 27 October 2023

# Ask 5 users whta thier favorite bubble tea place is
# Prints out a summery of the data

# ------ CONSTANTS

NUM_RESPONDENTS = 5

# ------

coco_likes = 0         # Intitialize the varable to 0
suntea_likes = 0
chatime_likes = 0
bubqueen_likes = 0
other_likes = 0

for _ in range(NUM_RESPONDENTS): 
    # Ask the user what thier favorite place is
    # Store that information somewhere
    print("What's your favourite bubble tea place?")

    fave_place = input().strip(",.?!").lower()

    # Tally or counting algo
    # Options: CoCo, Suntea, Chatime, Bubble Queen, 
    # If they choose any of these options, increase the counterC
    if fave_place == "coco":
        coco_likes = coco_likes + 1
    elif fave_place == "suntea":
        suntea_likes += 1           # alternate to above
    elif fave_place == "bubble queen":
        bubqueen_likes += 1
    elif fave_place == "chatime":
        chatime_likes += 1
    else: 
        other_likes +=1

# Repeat the code above 5 times


# print out summary
# Give the raw score and the score percentage
print(f"CoCo likes: {coco_likes} / {round (coco_likes / NUM_RESPONDENTS * 100)}%")
print(f"Suntea likes: {suntea_likes} / {round (suntea_likes / NUM_RESPONDENTS * 100)}%")
print(f"Bubble Queen likes: {bubqueen_likes} / {round (bubqueen_likes / NUM_RESPONDENTS * 100)}%")
print(f"Chatime likes: {chatime_likes} / {round (chatime_likes / NUM_RESPONDENTS * 100)}%")
print(f"Other likes : {other_likes} / {round (other_likes / NUM_RESPONDENTS * 100)}%")