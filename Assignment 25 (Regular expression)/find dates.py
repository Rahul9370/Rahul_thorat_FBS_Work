"""2. Create a function that extracts all the dates from a given text using regular expressions.
Dates can be in various formats like MM/DD/YYYY, DD-MM-YYYY, or written out like
January 1, 2023. Extract all such date occurrences."""

import re

def extract_dates(text):
    pattern = r'(\b\d{2}[/-]\d{2}[/-]\d{4}\b|' \
              r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b)'

    dates = re.findall(pattern, text)
    return dates

text = "I was born on 25-12-2000. Our meeting is on 01/15/2023. Independence Day is on August 15, 2023."
result = extract_dates(text)
print(result)
