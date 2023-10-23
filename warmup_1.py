# Warmup Bot
# Author Matt Santha
# Date sept 25 2023

# Create a bot that says BEEP BOOP

print("BEEP BOOP")

some_string = "This is some string."
print(some_string.upper().strip(".!").lower().split())

for i in range(10): print("Loop dee scoop!")

words = ["tickle", "pop", "roll", "dance"]
output = ""
for word in words:
  output = output + word[1]
print(output)

is_raining = True
is_cloudy = True
is_sunny = True
if is_raining:
       if is_sunny:
             print("Bring your shades and your umbrella!")
       elif is_cloudy:
             print("Brrrrr.")

adjectives = ["Golden", "Tiny", "Purple"]
stars = ["Polaris", "Vega", "Sun"]
for adj in adjectives:
  for word in stars:
    print(adj + word)