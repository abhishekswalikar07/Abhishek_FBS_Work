# Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount. (Use looping to optimize
# the problem)


amount = int(input("Enter the amount: "))

print("\nMinimum notes required:")

total_notes = 0

for note in (2000, 500, 200, 100, 50, 20, 10, 5, 2, 1):
    if amount >= note:
        count = amount // note
        amount %= note
        total_notes += count
        print(f"{note} Rs: {count}")

print(f"\nTotal number of notes: {total_notes}")

