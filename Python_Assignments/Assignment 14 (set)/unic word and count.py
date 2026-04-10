"""3. Write a Python program to find all the unique words and count the
frequency of occurrence from a given list of strings. Use Python set
data type."""
# Given list of strings
sentences = [
    "hi Rahul",
    "Hello Rahul",
    "Hello bhai",
    "hi bhai"
]

all_words = []

for sentence in sentences:
    words = sentence.split()
    all_words.extend(words) 

unique_words = set(all_words)

frequency = {}
for word in unique_words:
    frequency[word] = all_words.count(word)

for word, count in frequency.items():
    print(word, ":", count)
