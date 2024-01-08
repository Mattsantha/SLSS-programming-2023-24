# Winter Holidays
# Author: Matt 
# 8 January 2024

import random

# Requirments
# - create a functuion called winter_holiday()
#    -  takes one parameter - string
#    - returns a summary of an event from your holidays

# Please do not use ChatGPT or any LLM

good = ["I went to calgary to see my family", 
        "I got lots of chocolate",
        "I bought a laptop"
]

bad = ["I got very sick on Christmas day", 
       "It ended ;-;",
       "I had to do homework"
]

def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winetr holidays 2023 - 2024
    
    params:
        good_or_bad - string that indicates whether the event is good or bad
        
    returns:
        an event that happended to you during the holidays the event is selected part"""
    
    if good_or_bad == "good":
        return random.choice(good)
    elif good_or_bad == "bad":
        return random.choice(bad)


def main() -> None: 
    # Runs all the things we want to test in out .py file
    print(winter_holiday("good"))
    # "I went to calgary to see my family"
    # "I got lots of chocolate"
    print(winter_holiday("bad"))
    # "I got very sick on Christmas day"
    # "It ended ;-;"



# If we're running this file using python
#if __name__ == "__main__":
#    main()