"""4. Write a function that extracts all the URLs from a given text using regular expressions.
Return a list of URLs found in the input text."""
import re

def extract_urls(text):
    pattern = r'https?://[^\s]+'   
    urls = re.findall(pattern, text)
    return urls

text = "Check https://www.google.com and http://example.com for details. Also visit https://openai.com."
result = extract_urls(text)
print(result)
