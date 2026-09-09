from pathlib import Path

path = Path(r".\app.py")
text = path.read_text(encoding="utf-8")

if "from pathlib import Path" not in text:
    text = "from pathlib import Path\n" + text
    path.write_text(text, encoding="utf-8")
    print("Fixed: Path import added to app.py")
else:
    print("Path import already exists.")
