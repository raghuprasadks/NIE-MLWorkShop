#https://www.w3resource.com/python-exercises/pandas/index-data-series.php
#1. Write a Python program to create and display a one-dimensional array-like object containing an array of data using Pandas module.


#Series is a one-dimensional labeled array capable of holding any data type
import pandas as pd
ds = pd.Series([2,4,6,8,10])
print('series of even numbers ',ds)

#2. Write a Python program to convert a Panda module Series to Python list and it's type.
print("Pandas Series and type")
print(ds)
print(type(ds))
print("Convert Pandas Series to Python list")
print(ds.tolist())
print(type(ds.tolist()))

#3. Write a Python program to add, subtract, multiple and divide two Pandas Series.
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
print("Add two Series:")
print(ds)
print("Subtract two Series:")
ds = ds1 - ds2
print(ds)
print("Multiply two Series:")
ds = ds1 * ds2
print(ds)
print("Divide Series1 by Series2:")
ds = ds1 / ds2
print(ds)

#4. Write a Python program to get the largest integer smaller or equal to the division of the inputs. Go to the editor
#Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])
print("Series1:")
print(ds1)
print("Series2:")
print(ds2)
print("Compare the elements of the said Series:")
print("Equals:")
print(ds1 == ds2)
print("Greater than:")
print(ds1 > ds2)
print("Less than:")
print(ds1 < ds2)

'''
5. Write a Python program to convert a dictionary to a Pandas series. Go to the editor 
Sample Series: 
Original dictionary:
{'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
Converted series:
a 100
b 200
c 300
d 400
e 800
dtype: int64 
'''
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
print("Original dictionary:")
print(d1)
new_series = pd.Series(d1)
print("Converted series:")
print(new_series)

'''
6. Write a Python program to convert a NumPy array to a Pandas series. Go to the editor 
Sample Series: 
'''
import numpy as np
np_array = np.array([10, 20, 30, 40, 50])
print("NumPy array:")
print(np_array)
new_series = pd.Series(np_array)
print("Converted Pandas series:")
print(new_series)
'''
7. Write a Python program to change the data type of given a column or a Series. Go to the editor 
Sample Series: 
'''
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s1)
print("Change the said data type to numeric:")
s2 = pd.to_numeric(s1, errors='coerce')
print(s2)

'''
8. Write a Python Pandas program to convert the first column of a DataFrame as a Series.
'''
d = {'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
s1 = df.ix[:,0]
print("\n1st column as a Series:")
print(s1)
print(type(s1))

'''
9. Write a Pandas program to convert a given Series to an array. 
'''
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s1)
print("Series to an array")
a = np.array(s1.values.tolist())
print (a)
'''
10. Write a Pandas program to convert Series of lists to one Series.
'''
s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
print("Original Series of list")
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True)
print("One Series")
print(s)
'''
11. Write a Pandas program to sort a given Series.
'''
s = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s)
new_s = pd.Series(s).sort_values()
print(new_s)
'''
12. Write a Pandas program to add some data to an existing Series. 
'''
s = pd.Series(['100', '200', 'python', '300.12', '400'])
print("Original Data Series:")
print(s)
print("\nData Series after adding some data:")
new_s = s.append(pd.Series(['500', 'php']))
print(new_s)

'''
13. Write a Pandas program to create a subset of a given series based on value and condition. 
'''
s = pd.Series([0, 1,2,3,4,5,6,7,8,9,10])
print("Original Data Series:")
print(s)
print("\nSubset of the above Data Series:")
n = 6
new_s = s[s < n]
print(new_s)

'''
14. Write a Pandas program to change the order of index of a given series.
'''
s = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C','D','E'])
print("Original Data Series:")
print(s)
s = s.reindex(index = ['B','A','C','D','E'])
print("Data Series after changing the order of index:")
print(s)

'''
15. Write a Pandas program to create the mean and standard deviation of the data of a given Series.
'''
s = pd.Series(data = [1,2,3,4,5,6,7,8,9,5,3])
print("Original Data Series:")
print(s)
print("Mean of the said Data Series:")
print(s.mean())
print("Standard deviation of the said Data Series:")
print(s.std())

'''
Pandas DataFrame
'''
'''
1. Write a Pandas program to get the powers of an array values element-wise. 
'''
df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
print(df)

'''
2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
'''
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print(df)

'''
3. Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data. 
'''
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("Summary of the basic information about this DataFrame and its data:")
print(df.info())
'''
4. Write a Pandas program to get the first 3 rows of a given DataFrame.
'''
import pandas as pd
import numpy as np

exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)
print("First three rows of the data frame:")
print(df.iloc[:3])

'''
5. Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame.
'''
print(df[['name', 'score']])
'''
6. Write a Pandas program to select the specified columns and rows from a given data frame. Go to the editor
Sample Python dictionary data and list labels:
Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.
'''
print("Select specific columns and rows:")
print(df.iloc[[1, 3, 5, 6], [1, 3]])

'''
7. Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.
'''
df = pd.DataFrame(exam_data , index=labels)
print("Select specific columns and rows:")
print(df.ix[[1, 3, 5], ['name', 'score']])

'''
8. Write a Pandas program to count the number of rows and columns of a DataFrame. 
'''
'''
9. Write a Pandas program to select the rows where the score is missing, i.e. is NaN.
'''
df = pd.DataFrame(exam_data , index=labels)
print("Rows where score is missing:")
print(df[df['score'].isnull()])

'''
10. Write a Pandas program to select the rows the score is between 15 and 20 (inclusive). 
'''
df = pd.DataFrame(exam_data , index=labels)
print("Rows where score between 15 and 20 (inclusive):")
print(df[df['score'].between(15, 20)])

'''
11. Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15
'''
print("Rows where score between 15 and 20 (inclusive):")
print(df[(df['attempts'] < 3) & (df['score'] > 15)])

'''
12. Write a Pandas program to change the score in row 'd' to 11.5. Go to the editor
Sample Python dictionary data and list labels:
'''
print("\nOriginal data frame:")
print(df)
print("\nChange the score in row 'd' to 11.5:")
df.loc['d', 'score'] = 11.5




