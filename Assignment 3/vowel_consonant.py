# 2. Write a program to input any alphabet and check whether it is vowel or consonant.

alphabet = input("Enter any Alphabet : ").lower()    # lower convert all capital letter into small case 

if(alphabet in 'aeiou'):             #in ('aeiou') checks membership in the list of vowels.
    print("Alphabet is Vowel...")
else:
    print("Alphabet is consonant...")
