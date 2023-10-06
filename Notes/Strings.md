# Formate Strings
If we want to evaluate inside of a string, we use *f-strings*
To create an f-sting, we put an f before the open quote

```python
favorite_food = input("whats your favorite food?")

prinf(f"Oooooo,  {favorite_food} sounds good!")
```

# String Methods
[[Methods]] are function we can use on [[objects]].

String methods allow use to modify strings. 

Say for example we want to make all the characters of a string lowercase.

```python
mr_ubial_yelling = "YOU SHOULD PUSH YOU CHAIRS IN"

print(mr_ubial_yelling.lower())
```
wee can use string methods to help solve [[Errors#Semantic Errors|semantic errors]] 
## .lower()

The .lower() method takes a string and converts all uppercase characters to lowercase.

## .upper()

The .upper() method uppercases all the letters.

## .strip(chars)

The .strip method removes characters from both the beginning and the end of the string.

```python
user_feeling = input("How are you feeling today?")

# "good!" "good." "Good!" "good!!!!!!!!!!"
if user_feeling.lower().strip("!.,") == "good":
	print("That's great!")
```

## .split(str) -> List

The .split() method splits a string into a list, separating the string based on the characters you give.

```python
grocery_str = "eggs milk cheese hotwheels"

grocery_list = grocery_str.slpit("")
```

