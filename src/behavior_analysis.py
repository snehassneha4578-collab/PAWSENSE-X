import math

def analyze_movement(positions):
    if len(positions) < 2:
        return 0, "INSUFFICIENT DATA"

    distances = []

    for i in range(1, len(positions)):
        x1, y1 = positions[i - 1]
        x2, y2 = positions[i]

        distance = math.sqrt(
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        )

        distances.append(distance)

    total_distance = sum(distances)
    average_distance = total_distance / len(distances)

    if average_distance < 10:
        status = "NORMAL"
    elif average_distance < 30:
        status = "ACTIVE"
    else:
        status = "ABNORMAL MOVEMENT"

    return total_distance, status


print()
print("PAWSENSE-X - BEHAVIOR ANALYSIS")
print("=" * 42)

positions = [
    (100, 200),
    (115, 205),
    (140, 215),
    (175, 230),
    (220, 250),
    (280, 275)
]

distance, status = analyze_movement(positions)

print("Animal: DOG")
print("Tracking ID: Animal #1")
print(f"Total Movement Distance: {distance:.2f} pixels")
print(f"Behavior Status: {status}")

if status == "ABNORMAL MOVEMENT":
    print("Alert: Unusual movement pattern detected.")
else:
    print("Movement pattern is within monitored range.")

print("=" * 42)
