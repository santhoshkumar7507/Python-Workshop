# Write a Python program to reverse the order of words in a given sentence without reversing the individual characters in each word.

s = "The Blue Color"
word = s.split()
words = " ".join(word[::-1])
print(words)
