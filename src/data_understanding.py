import pandas as pd

df = pd.read_csv("data/customer_churn.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df["Churn"].value_counts())