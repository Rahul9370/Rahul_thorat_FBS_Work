"""3. Develop a function that counts the occurrences of each word in a given text. Use regular
expressions to split the text into words and then count the frequency of each word."""
import re
from collections import Counter

def word_count(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)


text = "He is a good boy. He is very good."
result = word_count(text)
print(result)
