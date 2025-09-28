"""1. Develop a function that takes a text and a list of forbidden words. Replace all
occurrences of these forbidden words with asterisks (*) using regular expressions."""

import re

def censor_text(text, forbidden_words):
    for word in forbidden_words:
        text = re.sub(word, '*' * len(word), text, flags=re.IGNORECASE)
    return text

text = "He is a bad boy and he did a crime."
forbidden = ["bad", "crime"]

result = censor_text(text, forbidden)
print(result)   # Output: He is a *** boy and he did a *****.
