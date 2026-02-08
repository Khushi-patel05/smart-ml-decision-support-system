import pandas as pd

df = pd.read_csv("data/customer_churn.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df["Churn"].value_counts())
print("Missing values per column:")
print(df.isnull().sum())
if df["TotalCharges"].isnull().sum()>0:
    df["TotalCharges"]=df["TotalCharges"].fillna(df["TotalCharges"].median())
for col in df.select_dtypes(include="object").columns:
    df[col]=df[col].fillna(df[col].mode()[0])
print("Missing values after cleaning:")
print(df.isnull().sum())
