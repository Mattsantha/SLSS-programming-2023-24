# SFU's Best
# Author: Matt
# 10 Novemebr 2023

# Laod data from .cvs file
# Read it in a meaningful way
# Link our simularity score algo to the data

# Open the file
with open("./data.csv") as f: 

# Read the first line of data

    f.readline()
    print(f.readline())

# Create a "profile" for someone that shows their favourite places at SFU
profile = [
    "Bubble World", 
    "Bamboo Graden",
    "Uncle Fatih's",
    "Guadalupe",
    "Steve's Poke Bar"
]

# Initialize our top similarity score and their name
top_sim_score = 0
top_sim_name = ""

with open("./data.csv") as f:
    # Throw away the header
    header = f.readline()

    # For every line of data in thefile (string)
    for line in f:
        # Convert the line of data into a list
        current_likes = line.split(",")

        # initalize the CURRENT simularity score
        # Store current persomn's name
        current_sim_score = 0    
        current_name = current_likes[1]

        # sim score algo
        for item in profile:
            if item in current_likes:
                current_sim_score += 1

        # print the current_sim_score
        print(f"{current_name} - Score: {current_sim_score}") 

        # if the cur score is > top sim score
        if current_sim_score > top_sim_score:
            #upadte the top sim score and the name
            top_sim_score = current_sim_score
            top_sim_name = current_name

print("🌟🌟🌟TOP SIMILAR PERSON!🌟🌟🌟")
print(f"{top_sim_name} - Score: {top_sim_score}")



