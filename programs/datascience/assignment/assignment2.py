import pandas as pd
df = pd.read_csv('studentrecord-1.csv')
print(df)

'''
1. Create a column called total
'''
df["total"] = df["sub1"]+df["sub2"]+df["sub3"]
print('After adding total column',df)
'''
2. Find the duplicate
'''
count = df.loc[df.duplicated(),:].count()
print('count of duplicate')
df.loc[df.duplicated(keep="first"),:]

countnull = df.isnull().sum()
shapenew = df.shape[0]
shapeafterdrop = df.dropna(how = "any").shape[0]
