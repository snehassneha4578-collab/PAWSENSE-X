from datetime import datetime

events = []

def add_event(animal_id, event_type, message, severity):
    events.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "animal": animal_id,
        "type": event_type,
        "message": message,
        "severity": severity
    })


add_event(
    "Animal #1",
    "DETECTION",
    "Dog detected with 89.69% confidence",
    "INFO"
)

add_event(
    "Animal #1",
    "BEHAVIOR",
    "Abnormal movement pattern detected",
    "WARNING"
)

add_event(
    "Animal #1",
    "DANGER ZONE",
    "Animal entered critical zone",
    "CRITICAL"
)

add_event(
    "Animal #1",
    "RISK",
    "Welfare risk score reached 87/100",
    "CRITICAL"
)


print()
print("PAWSENSE-X - EVENT TIMELINE")
print("=" * 60)

for event in events:
    print(
        f"[{event['time']}] "
        f"{event['animal']} | "
        f"{event['type']} | "
        f"{event['severity']}"
    )
    print(f"  {event['message']}")

print("=" * 60)
print(f"Total Events: {len(events)}")
