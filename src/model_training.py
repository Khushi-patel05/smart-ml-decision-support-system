import pandas as pd

df=pd.read_csv("data/customer_churn_cleaned.csv")

print(df.shape)
print(df.head())

y=df["Churn"]

X = df.drop(["Churn", "customerID"], axis=1)

print("Feature shape:",X.shape)
print("Target shape:",y.shape)

X=pd.get_dummies(X,drop_first=True)
print("Encoded feature shape:",X.shape)

from sklearn.model_selection import train_test_split 

X_train,X_test,y_train,y_test=train_test_split(
    X,y,
    test_size=0.2,
    random_state=42
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)
