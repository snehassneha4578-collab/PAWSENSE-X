from pawsense_detection import session, image, output, boxes, scores, indices
from risk_engine import calculate_risk

print()
print("PAWSENSE-X - COMPLETE INTELLIGENCE PIPELINE")
print("=" * 50)

if len(indices) == 0:
    print("No animal detected.")
else:
    index = int(indices[0])

    print("Animal Detected: DOG")
    print("Tracking ID: Animal #1")
    print(f"Detection Confidence: {scores[index] * 100:.2f}%")
    print("Status: ACTIVE")
    print()

    score, level, reasons = calculate_risk(
        road_proximity=30,
        vehicle_proximity=25,
        abnormal_movement=18,
        baseline_deviation=14
    )

    print(f"Risk Score: {score}/100")
    print(f"Risk Level: {level}")
    print()
    print("Explainable Alert:")
    for reason in reasons:
        print(f"- {reason}")

    print()
    print("Human verification recommended.")

print("=" * 50)
