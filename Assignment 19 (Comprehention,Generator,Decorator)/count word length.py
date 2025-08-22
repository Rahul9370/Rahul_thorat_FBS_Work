"""6. Use a dictionary comprehension to count the length of each word
in a sentence (take input from user)"""

sentence = input("Enter a sentence: ")

word_length = {word: len(word) for word in sentence.split()}

print("Word lengths:", word_length)
