def check_danger_zone(animal_x, animal_y, zone_x1, zone_y1, zone_x2, zone_y2):
    inside = (
        zone_x1 <= animal_x <= zone_x2
        and
        zone_y1 <= animal_y <= zone_y2
    )

    if inside:
        return True, "CRITICAL ZONE"
    else:
        return False, "SAFE ZONE"


print()
print("PAWSENSE-X - DANGER ZONE ANALYSIS")
print("=" * 42)

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

print("Animal: DOG")
print("Tracking ID: Animal #1")
print(f"Animal Position: ({animal_x}, {animal_y})")
print(f"Danger Zone: {road_zone}")
print(f"Zone Status: {zone_status}")

if danger:
    print("Alert: Animal is inside the danger zone.")
else:
    print("Animal is outside the danger zone.")

print("=" * 42)
