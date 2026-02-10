import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

print("Churn counts:")
print(df["Churn"].value_counts())

print("\nChurn percentages:")
print(df["Churn"].value_counts(normalize=True))

sns.countplot(x="Churn", data=df)
plt.title("Churn Distribution")
plt.show()

print("\nStatistical summary:")
print(df.describe())

sns.histplot(df["MonthlyCharges"], kde=True)
plt.title("Monthly Charges Distribution")
plt.show()
