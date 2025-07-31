# Convert distant given in feet and inches into meter and centimeter

# Conversion factors
INCH_TO_CM = 2.54
FOOT_TO_CM = 30.48


feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distance in inches: "))


total_cm = (feet * FOOT_TO_CM) + (inches * INCH_TO_CM)
#print(total_cm)


meters = int(total_cm // 100)
centimeters = float(total_cm % 100)

print(f"Distance in meters and centimeters: {meters} meter(s) and {centimeters} centimeter(s)")
