import pandas as pd
df = pd.read_csv('iris.csv')
# df=(df.iloc[2:8,[0,2]])
# print(df[df['species'].isin(['Iris-virginica'])])
df['Area'] = df['sepal_length'] * df['sepal_width']
# print(df.head())
print(df)
#For deleting the column:
df=df.drop(columns=['sepal_length'])
print(df.head())

#For Renaming the columns:
df=df.rename(columns={"sepal_width": "sepal-width", "petal_width":"petal-width","Area":"Total Area"})
print(df.head())

to_append = [1.0,4.0,5.0,7.0,"Hybrid"]
df.loc[len(df)]=to_append
print(df)


