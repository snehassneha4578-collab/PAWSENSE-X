def calculate_risk(road_proximity, vehicle_proximity, abnormal_movement, baseline_deviation):
    score = (
        road_proximity
        + vehicle_proximity
        + abnormal_movement
        + baseline_deviation
    )

    score = min(score, 100)

    if score <= 30:
        level = "LOW"
    elif score <= 60:
        level = "MODERATE"
    elif score <= 80:
        level = "HIGH"
    else:
        level = "CRITICAL"

    reasons = []

    if road_proximity > 0:
        reasons.append("Near danger zone")

    if vehicle_proximity > 0:
        reasons.append("Vehicle proximity detected")

    if abnormal_movement > 0:
        reasons.append("Abnormal movement pattern")

    if baseline_deviation > 0:
        reasons.append("Behavior differs from baseline")

    return score, level, reasons


print()
print("PAWSENSE-X - WELFARE RISK ENGINE")
print("=" * 42)

score, level, reasons = calculate_risk(
    road_proximity=30,
    vehicle_proximity=25,
    abnormal_movement=18,
    baseline_deviation=14
)

print("Animal: DOG")
print("Tracking ID: Animal #1")
print(f"Risk Score: {score}/100")
print(f"Risk Level: {level}")
print()
print("Explainable Alert:")
for reason in reasons:
    print(f"- {reason}")

print()
print("Human verification recommended.")
print("=" * 42)
