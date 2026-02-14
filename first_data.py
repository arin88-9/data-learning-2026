import pandas as pd

data = {
    "Name": ["Arin", "Rahim", "Karim", "Sadia"],
    "Department": ["CSE", "CSE", "EEE", "BBA"],
    "CGPA": [2.7, 3.1, 2.9, 3.5]
}

df = pd.DataFrame(data)

print(df)
print("\nAverage CGPA:", df["CGPA"].mean())
