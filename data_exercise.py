from pathlib import Path


# File Exercises
# Author: Matt Santha
#

"""Instructions:

Put this file in your programming folder.
Download the data-example.csv file and put it in this same folder.
For each problem, design a solution.
Each part builds on the previous step, so don't skip any.
You can refer to the work that we did last day for any hints.
Do not use any generative AI for the solutions."""

# Since our file has some symbols in it, this is the most
# effective way at opening up the file.

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()

# Note that I've set the encoding parameter to "utf-8"

# --- Problems


# Problem 1:
# Open the file and print the contents of the second line in the file.
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    print(f.readline())

# Problem 2:
# Good! Now that you've done that, open the file, and print out every line of data.
    for line in f:
        print(line)

# Problem 3:
# If you've made it this far, well done. Next task:
# Convert that line of data into a list.
with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        print(line.split(',')) 

# Problem 4:
# Give yourself a pat on the back.
# See if you can count how many people like "Chicken Adobo" as their
# favourite food.
chicken_adobo = 0

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        if "Chicken Adobo" in line:
            chicken_adobo += 1

print(f"{chicken_adobo}: this many people like chicken adobo.")

# Problem 5:
# You should have gotten four people for the last problem. If not,
# see if why your code doesn't work.
# Else, you can move on to this part, which is, find out how many
# people have the first letter of their first name start with "A".
a_people = 0

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        if "A" == line[0]:
            a_people += 1

print(f"{a_people}: amount of A named people.")


# Problem 6:
# 19 people! Excellent. How many people come from Guangzhou?
guangzhou_people = 0

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        if "Guangzhou" in line:
            guangzhou_people += 1

print(f"{guangzhou_people}: this many people live in Guangzhou.")


# Problem 7:
# Just one is from Guangzhou! Alright, last one. How many people have a credit card
# number that is even. There are a couple of ways to solve this.
# You can either do this with the string or with the int.
creditcard_user = 0

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        if int(line.split(",")[3])%2==0:
            creditcard_user += 1


print(f"{creditcard_user} have even creditcard numbers.")
        

# Problem 8:
# Sorry, no answer for the above one. This one is a challenge question.
# Can you design a way to find the most popular food?

food_list = {'a':1}
most_popular_food = 0
popular_food_name = ""

with open("./data_example.csv", encoding="utf-8") as f:
    f.readline()
    for line in f:
        current_food = line.split(",")[1]
        if current_food in food_list:
            food_list[current_food]+=1
        else:
            food_list[current_food]=1

for food in food_list:
    if food_list[food] > most_popular_food:
        most_popular_food = food_list[food]
        popular_food_name = food

print(f"{popular_food_name} is the most popular food.")
    


