
# Syntax Errors

These types of errors are ones where you run your code and something breaks.

Syntax errors are relatively easy to fix 

Syntax errors happen when we don't follow the rules completely

Some examples are when we forget a closing". Or if we're missing a closing parenthesis

	Syntx <=> Rules
# Semantic Errors

Semantic Errors are much more challenging (in Mr. Ubial opinion) to squash

Semantic errors are where you code doesn't "mean" what you actually means.

```python
user_response = input("Do you like to eat food?")

if user_response == "yes":
	print("You passes the human test.")
else:
	print("You must be some sort of robot.")
```

The problem with the above code is subtle. What i (Mr. Ubial) means is that if the user answer with anything affirmative the answer should go into the "yes" block. 

One way to solve this problem is to use [[Strings#String Methods| string methods]]. We can use .lower( to catch all permutations of capital letters.

```python
user_response = input("Do you like to eat food?")

if user_response.lower() == "yes":
	print("You passes the human test.")
else:
	print("You must be some sort of robot.")
```
