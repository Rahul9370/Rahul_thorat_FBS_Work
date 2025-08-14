"""
8. Write a Python program to find all the anagrams and group them
together from a given list of strings.
"""

# 8. Find all the anagrams and group them together (using set)

words = ["listen", "silent", "enlist", "rat", "tar", "art", "hello"]

groups = [] 

while words:  
    first_word = words[0]          
    first_set = set(first_word)   
    group = set()                  

    for w in words[:]:               
        if set(w) == first_set:      
            group.add(w)            
            words.remove(w)          

    groups.append(group)             

for g in groups:
    print(g)
