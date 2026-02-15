import pandas as pd
df=pd.read_csv("D:\data-journey\day1\exercise.csv")
print("first 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nAverage Pulse:", df["pulse"].mean())
print("Maximum pulse:", df["pulse"].max())

print("\nDiet Count:")
print(df["diet"].value_counts())