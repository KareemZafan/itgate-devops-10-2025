import pandas as pd

# data={
#     "name":["abdelrahman","salma","hajar","anas"],
#     "age": [17,18,19,21]
# }


# print(data)

# df=pd.DataFrame(data)
# print(df)


df=pd.read_csv("/content/sample_data/products-100.csv")
print(df)


print(df.columns)
print(df.shape)
print(df.info())


cleaned_data=df.dropna()

print(df.head(10))

df["newPrice"] = df["Price"]*1.2
df["Color"]="red"

meanofPrice=df["Price"].mean()

print(meanofPrice)

nameAndPrice=df.groupby("Name")["Price"].mean()
print(nameAndPrice)
print(df.describe())

priceover500=df[df["Price"]>500]
print(priceover500)
print(df)