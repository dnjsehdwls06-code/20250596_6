from pathlib import Path
import pandas as pd

csv_path = Path(__file__).with_name("scores.csv")
df = pd.read_csv(csv_path, encoding="utf-8")

df["score"] = pd.to_numeric(df["score"], errors="coerce")

result = df.groupby("category")["score"].mean().round(2)

print(result)
