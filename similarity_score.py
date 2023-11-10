# Comparing Simialrity Score
# Author: Matt 
# 8 November 2023

# Calculate similarity scores between two people

# Create two lists that represent the movies that poeple like 
matts_favorite_movies = [
    "spider-man: Into the spider-verse", 
    "John Wick 2", 
    "Equalizer", 
    "Infinity War", 
    "Forest Gump"
]

kevin_favorite_movies = [
    "Black Panther", 
    "Five Nights at Freddies", 
    "John Wick 2", 
    "Cars 2", 
    "2 Fast 2 Furious"
]

# Initialize the similarity score
similarity_score = 0

# For each item in the first list
for movie in matts_favorite_movies:
    if movie in kevin_favorite_movies:
        similarity_score += 1

# Display tghe results 
print(f"Matt and Kevin have a similarity score of {similarity_score}.")