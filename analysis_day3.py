import pandas as pd

df = pd.read_csv("D:\data-journey\day1\exercise.csv")

print("Full Dataset:")
print(df.head())

low_fat = df[df["diet"] == "low fat"]

print("\nLow Fat Diet Records:")
print(low_fat)

print("\nAverage Pulse (Low Fat):", low_fat["pulse"].mean())

no_fat = df[df["diet"] == "no fat"]
print("Average Pulse (No Fat):", no_fat["pulse"].mean())

max_pulse = df["pulse"].max()
print("\nHighest Pulse Recorded:", max_pulse)

print(df[df["pulse"] == max_pulse])

print("\nActivity Count:")
print(df["kind"].value_counts())
