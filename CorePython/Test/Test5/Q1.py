# Q1: Minimum number of notes

denominations = [2000, 500, 200, 100, 50, 20, 10, 5]

amount = int(input("Enter the amount: "))
notes_count = {}

for note in denominations:
    if amount >= note:
        count = amount // note
        notes_count[note] = count
        amount = amount % note

print("Minimum notes required:")
total_notes = 0
for note, count in notes_count.items():
    print(f"{note} : {count}")
    total_notes += count

print("Total number of notes:", total_notes)
    


