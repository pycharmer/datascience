import pandas as pd

df = pd.read_csv("/Users/vivekpradhan/Downloads/DataScience-Python3/PastHires.csv")
print(df.head())

#print(df.size,df.shape)

print(df["Hired"])
