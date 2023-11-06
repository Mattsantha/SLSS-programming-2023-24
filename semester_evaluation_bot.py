# Semeseter Evaluation Bot
# Author: Matt
# November 6 2023

# Greet User
print("Hello user I am a bot that will evaluate your semester.")

# Ask questions

courses_taking = int(input("How many couses do you have?"))

courses_num = 0

for courses in range(courses_taking):
    courses_num += int(input(f"How would you rate {courses} out of 5"))


# Avergae score

if courses_num/courses_taking <= 1

