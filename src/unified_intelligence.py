from pawsense_detection import scores, indices
from behavior_analysis import analyze_movement
from danger_zone import check_danger_zone
from risk_engine import calculate_risk

print()
print("PAWSENSE-X - UNIFIED INTELLIGENCE REPORT")
print("=" * 55)

# Animal Detection
confidence = scores[int(indices[0])] * 100 if len(indices) else 0

print("ANIMAL")
print("-" * 55)
print("Species: DOG")
print("Tracking ID: Animal #1")
print(f"Detection Confidence: {confidence:.2f}%")
print("Status: ACTIVE")

# Behavior Analysis
positions = [
    (100, 200),
    (115, 205),
    (140, 215),
    (175, 230),
    (220, 250),
    (280, 275)
]

distance, behavior_status = analyze_movement(positions)

print()
print("BEHAVIOR")
print("-" * 55)
print(f"Movement Distance: {distance:.2f} pixels")
print(f"Behavior Status: {behavior_status}")

# Danger Zone
animal_x = 520
animal_y = 280
road_zone = (450, 150, 620, 400)

danger, zone_status = check_danger_zone(
    animal_x,
    animal_y,
    road_zone[0],
    road_zone[1],
    road_zone[2],
    road_zone[3]
)

print()
print("ENVIRONMENT")
print("-" * 55)
print(f"Position: ({animal_x}, {animal_y})")
print(f"Zone Status: {zone_status}")

# Risk Engine
score, level, reasons = calculate_risk(
    road_proximity=30,
    vehicle_proximity=25,
    abnormal_movement=18,
    baseline_deviation=14
)

print()
print("WELFARE RISK")
print("-" * 55)
print(f"Risk Score: {score}/100")
print(f"Risk Level: {level}")

print()
print("EXPLAINABLE ALERT")
print("-" * 55)

for reason in reasons:
    print(f"- {reason}")

print()
print("RECOMMENDATION")
print("-" * 55)
print("Human verification recommended.")

print("=" * 55)
print("PAWSENSE-X INTELLIGENCE PIPELINE: READY")
print("=" * 55)
