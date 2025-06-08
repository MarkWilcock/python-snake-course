"""
This short script demos conditional flow (while, for and if)

This script asks the user for a word, spells it out letter by letter and calculates a points
score for the word based on the letters used. (Z = 5, X = 4, vowels = 1, other consonants = 2)

It uses a while loop to allow the user to enter multiple words.
It uses a for loop to iterate over each letter in the word 
and an if statement to determine the points scored.  

It then repeats this until the user enters "exit".

This mimics the conditional flow structure introduced in our snake main loop

We will build this in several steps.

1. the input function is used to get input from the user.
2. the print function is used to display output to the user.
3. a for loop will iterate over each letter in the word to spell it out
4. an if statement within the for loop will add points based on the letter.

5. A basic while loop will allow the user to enter words repeatedly until they type 'exit'.
a. with the test on the while clause 
b. with the test inside the loop the causes a break
c. with the test inside the loop that sets a boolean variable to True

"""
print("Game started")

print("Game over")