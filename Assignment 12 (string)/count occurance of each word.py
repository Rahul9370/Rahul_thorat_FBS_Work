# 14. Python Program to count the occurrences of each word in a string.
# 14. Python Program to count the occurrences of each word in a string

mystr = "hi Rahul Hello Rahul Hello bhai"

words = mystr.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Occurrences of each word:")
for word, count in word_count.items():
    print(word, ":", count)

