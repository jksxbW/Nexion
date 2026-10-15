"""Prüft, dass alle Content-Dateien gültiges JSON sind und jeder Content ein Sprite hat."""
import glob
import json
import os
import sys

errors = []

try:
    mod = json.load(open("mod.json", encoding="utf-8"))
    for key in ("name", "version", "minGameVersion"):
        if key not in mod:
            errors.append(f"mod.json: Feld '{key}' fehlt")
except Exception as e:
    errors.append(f"mod.json: {e}")

files = glob.glob("content/**/*.json", recursive=True)
for f in files:
    try:
        json.load(open(f, encoding="utf-8"))
    except Exception as e:
        errors.append(f"{f}: ungültiges JSON ({e})")

sprites = {os.path.splitext(os.path.basename(p))[0] for p in glob.glob("sprites/**/*.png", recursive=True)}
for f in files:
    name = os.path.splitext(os.path.basename(f))[0]
    # Erze nutzen Varianten name1, name2, name3
    if name not in sprites and f"{name}1" not in sprites:
        errors.append(f"{f}: kein Sprite '{name}.png' gefunden")

print(f"{len(files)} Content-Dateien, {len(sprites)} Sprites geprüft.")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("Alles in Ordnung.")
