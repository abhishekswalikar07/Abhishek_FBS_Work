# Convert the time entered in hh,min and sec into seconds.

hours=int(input("Enter the hours to be in seconds: "))
minutes=int(input("Enter the minutes to be in seconds: "))
seconds=int(input("Enter the  seconds: "))

total_seconds=(hours*3600)+(minutes*60)+seconds

print(f'Total seconds from {hours} hours, {minutes} minutes and {seconds} seconds is {total_seconds} seconds.')