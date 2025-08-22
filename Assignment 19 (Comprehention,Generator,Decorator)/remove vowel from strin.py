# 4. Remove all of the vowels in a string (take input from user)

mystring = input("Enter string: ")
remove_vowel = "".join([x for x in mystring if x.lower() not in "aeiou"])
print("String without vowels:", remove_vowel)
