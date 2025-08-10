# 2. Python Program to Concatenate Two Dictionaries Into One
dict1 = {"name": "Rahul"}
dict2 = {"age": 22}

dict3 = dict1.copy()  
dict3.update(dict2)    

print("Concatenation of dict1 and dict2 is:", dict3)

# or 
dict1 = {"name": "Rahul"}
dict2 = {"age": 22}

dict3 = {**dict1, **dict2}
print("Concatenation of dict1 and dict2 is:", dict3)

