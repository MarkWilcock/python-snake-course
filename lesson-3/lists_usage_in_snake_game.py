"""
An example of a list that resembles in in some way our snake list.
We start the list with three elements, just like the snake game starts with three segments
We consider the  first element to be the head (pointing in the direction of travel)
We want our list to "walk" through the alphabet while keeping only three elements
"""
letters = ["C", "B", "A"]
print(f"original letters {letters}")  

# Let's move one letter forward in the alphabet
new_letter = "D"
letters.insert(0, new_letter)  # we insert the new letter at the start of the list
letters.pop() # we remove the last element to keep the list length constant
print(f"letters v1 {letters}")  

# And move one more letter forward
new_letter = "E"
letters.insert(0, new_letter)   
letters.pop() 
print(f"letters v1 {letters}")  

# Using tuples

pairs = [("C", "Charlie"), ("B", "Bravo"), ("A", "Alpha" )]
print(f"original pairs {pairs}")

new_pair = ("D", "Delta")
pairs.insert(0, new_pair)  # Insert the new pair at the start of the list
pairs.pop()  # Remove the last element to keep the list length constant
print(f"revised pairs {pairs}")  # Output should be [('D', 'Delta'), ('C', 'Charlie'), ('B', 'Bravo')] 

# Assume the head is the last element in the list

reversed_pairs = [ ("A", "Alpha" ), ("B", "Bravo"), ("C", "Charlie")]
print(f"Original reversed pairs {pairs}")

new_pair = ("D", "Delta")
reversed_pairs.append(new_pair)  # Append a new pair at end of list
reversed_pairs.pop(0)  # Remove the first element to keep the list length constant
print(f"revised reversed pairs {reversed_pairs}")  

