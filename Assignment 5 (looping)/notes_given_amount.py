"""5. Write a program to accept an integer amount from user and tell minimum
number of notes needed for representing that amount. (Use looping to optimize
the problem)"""
amount = int(input("Enter total amount to distribute in minimum notes: "))

note = 500
total_notes = 0

while note >= 10:
    count = amount // note
    print("Notes for", note, ":", count)
    total_notes += count
    amount %= note  

    
    if note == 500:
        note = 200
    elif note == 200:
        note = 100
    elif note == 100:
        note = 50
    elif note == 50:
        note = 20
    elif note == 20:
        note = 10
    elif note == 10:
        break  

print("Minimum number of notes needed for representing that amount is:", total_notes)


    
