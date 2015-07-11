Insight Data Engineering - Coding Challenge
===========================================================

For this challenge, I used the dictionary in python because I wanted to put the words in a hash map.
The algorithm of this code is:
- For finding words in tweets I scan through the tweets, split them according to the spaces and add the to dictionary
- If the item has been added to dictionary, just incremet the count
- For median just scan through the counts arrays and return the middle one (if they are even number of counts, return average of middle ones)

We can also implement it without using dictionary data structure by defining a hash class and also sort them in a heap to ease access to them.
