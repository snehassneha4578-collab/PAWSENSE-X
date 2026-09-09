from pathlib import Path

path = Path(r".\app.py")
text = path.read_text(encoding="utf-8")

old = 'st.subheader("🐕 Animal Intelligence")'
new = '''st.subheader("🐕 Animal Intelligence")

    image_path = Path(r"data/dog.png")
    if image_path.exists():
        st.image(str(image_path), caption="Detected Animal - Dog", width="stretch")'''

if old in text:
    text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")
    print("Dashboard updated: DOG image panel added.")
else:
    print("Animal Intelligence section not found.")
