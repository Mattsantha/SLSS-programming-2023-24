---
tags:
  - programming-level-1-2
  - algorithms
  - recommendation-systems
---
## Popularity and Likes

the type of paradigm makes a suggestion based on how many people like the thing

one prime example of this, is the like button(heart) in instagram. When you click that heart, instagram records it,  and based on information it has on you, it might suggest that to someone else that is similar to you. 

We created the Favourite Bubble Tea service which is based on the "Popularity/Likes" paradigm of recommendation systems. 

## N-Point rating Systems

N-Point rating systems are used by many services but one that nearly everyone is familiar with is Amazon's main purchasing service.

This paradigm is where users rate a product out of a certain number.

# Similarity Scores

Amazon, Netflix, ad Meta all use Similarity Scores to help drive users to their platform.

>Example:  Amazon
> Ubial likes ["nintendo switch", "usb chargers","4k blu ray movies"]
> Ben Ubial like ["nintendo switch", "usb chargers", "lego"]
> Fido likes ["lego", "chew toys", "dog food"]


Similarity score between Ubial and Ben Ubial: 2
Similarity between Ubial and Fido: 0
Similarity between Ben and Fido: 1