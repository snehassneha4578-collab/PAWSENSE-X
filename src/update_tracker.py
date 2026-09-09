from pathlib import Path

p = Path(r".\src\tracker.py")
s = p.read_text()

s = s.replace(
    'print("Press Q to quit.")',
    'print("Press Q to quit.")\n\nnext_animal_id = 1'
)

s = s.replace(
    'for animal_number, index in enumerate(indices, start=1):',
    'for animal_number, index in enumerate(indices, start=1):'
)

s = s.replace(
    'f"Dog #{animal_number} {scores[index] * 100:.1f}%"',
    'f"Animal #{animal_number} | Dog | {scores[index] * 100:.1f}%"'
)

p.write_text(s)
print("Tracker updated successfully.")
