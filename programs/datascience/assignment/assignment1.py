import pandas as pd
df = pd.read_csv('studentrecord.csv')
print(df)

'''
1. Create a column called total
'''
df["total"] = df["sub1"]+df["sub2"]+df["sub3"]
print('After adding total column',df)
'''
2. Find the topper
'''
topper = df.total.max()
topperdetails = df.loc[df['total'] == topper]
lastone = df.total.min()
lastonedetails = df.loc[df['total'] == lastone]
sub1t = df.sub1.max()
indext = df.inde(df.total.max())