# Distances between consecutive locations in meters (clockwise)
distances = [1000, 3500, 5800, 2400, 6200, 4500]
locations = ["s1", "s2", "s3", "s4", "s5", "s6"]

def calculate_fare(start, end):
    i = locations.index(start)
    j = locations.index(end)

    # Clockwise distance
    cw = 0
    while i != j:
        cw += distances[i]
        i = (i + 1) % len(locations)

    # Counter-clockwise distance
    total = sum(distances)
    ccw = total - cw

    # Shortest distance
    shortest = min(cw, ccw)

    # Convert to km and calculate fare
    km = shortest / 1000
    fare = km * 5

    return f"Distance: {shortest} meters ({km:.2f} km), Fare = Rs {fare:.2f}"


start = input("Enter start location (s1-s6): ").lower()
end = input("Enter end location (s1-s6): ").lower()

print(calculate_fare(start, end))