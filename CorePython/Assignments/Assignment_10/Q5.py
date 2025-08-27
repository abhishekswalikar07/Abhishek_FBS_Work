# Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

li=[12,43,56,27,67,43]
count=0

ele=int(input("Enter element to check present or not in list and how many time it is present:"))

for i in range(0,len(li)):
    if ele == li[i]:
        count+=1
if count > 0:
    print(f"{ele} is present in the list {count} time(s).")
else:
    print(f"{ele} is not present in the list.")