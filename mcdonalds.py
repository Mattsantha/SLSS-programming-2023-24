# McDonald program
# Author: Matt Santha
# 3 November 2023

# Greet User
print("Welcome to McDonalds!")

total_price = 0


# Ask what they want to eat
burger = input("Whould you like a buger for $5? (Yes/No)")

if burger.lower().strip(",.?!") == "yes":
    total_price = total_price + 5
    print("Ok that will add $5 to your total cost.")
elif burger.lower().strip(",.?!") == "no":
    print("Ok onto the next item.")
else: print("We don't have that on our menu")


fries = input("Would you like fries for $3? (Yes/No)")

if fries.lower().strip(",.?!") == "yes":
    total_price = total_price + 3
    print("Perfect.")
elif fries.lower().strip(",.?!") == "no":
    print("Ok then.")
else: print("YES OR NO PLEASE!")

tax = total_price * 0.14
final_price = total_price + tax

# Tell them their total price
print(f"Your total price will be {final_price:.2f}. How would you like to pay?")



