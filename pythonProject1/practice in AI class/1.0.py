import pandas as pd
df = pd.read_csv('iris.csv')
#print(df.head())
#print(df.tail())
#print(df.describe())
# print(df.dtypes)
# print(df.index)
# print(df.columns)
# print(df.values)
# print(df.values)
# print(df.shape)
# print(df.describe())
# print(df.sort_values(by='species',ascending=False))
print(df.sepal_length())
