from pathlib import Path

csv_path = Path(__file__).with_name("scores.csv")
with csv_path.open("r", encoding="utf-8") as f:
    lines = f.readlines()

header = lines[0].strip().split(",")
cat_idx = header.index("category")
score_idx = header.index("score")

totals = {}
counts = {}

for line in lines[1:]:
    parts = line.strip().split(",")
    raw = parts[score_idx].strip()
    if raw == "":
        continue
    try:
        score = float(raw)
    except ValueError:
        continue
    category = parts[cat_idx]
    if category not in totals:
        totals[category] = 0.0
        counts[category] = 0
    totals[category] += score
    counts[category] += 1

for category in sorted(totals):
    average = totals[category] / counts[category]
    print(category, round(average, 2))
