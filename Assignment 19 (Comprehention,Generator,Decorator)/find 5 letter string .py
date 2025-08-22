# 5. Find all of the words in a string that are less than 5 letters (take
# input from user)

mystr = input("Enter a string: ")
words = mystr.split()

short_words = [word for word in words if len(word) < 5]

print("Words less than 5 letters are:", short_words)
