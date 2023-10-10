# Loop Practice
# Matt Santha
# 10 October 2023

import time

# Create a list of groceries
groceries = ["hot wheels", "lego", "ice cream", "video games" ]

# Do something for each thing in the list
# Print it out in a pretty way
# e.g.
#   * hot wheels
#     ---
#   * lego
#     ---
#     ect

# print(f"* {groceries[0]}")
# print(f"  ---")
# print(f"* {groceries[1]}")
# print(f"  ---")
# print(f"* {groceries[2]}")
# print(f"  ---")
# print(f"* {groceries[3]}")
# print(f"  ---")

for item in groceries:
    print(f"* {item}")
    print(f"---")

# Using the above method, create the thing below:
# *
# **
# ***
# ****
# *****
# ******

pyramid = ["*", "**", "***", "****", "*****", "******"]

for row in pyramid:
    print(f"{row}")

# Create a New Year's countdown thats automatic

new_year = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "Happy New Year!!!"]

for count in new_year:
    print(f"{count}")
    time.sleep(1)