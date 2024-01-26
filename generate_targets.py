import os
import pandas as pd

python_dataset = {
    "program_id": [],
}

for x in os.listdir("./py-suite"):
    if "-" in x:
        continue
    python_dataset["program_id"].append(f"leetcode_python_{x}")

pd.DataFrame(python_dataset).to_csv("python_testables.csv")