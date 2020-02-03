# https://www.listendata.com/2019/06/matplotlib-tutorial-learn-plot-python.html

import matplotlib.pyplot as plt
#Basic Plot

x = [1, 2, 3, 4, 5]
y = [5, 7, 3, 8, 4]
plt.bar(x,y)
plt.show()

#1. Bar Graph
x = ['ravi', 'ranga', 'rohit', 'rahim', 'roja']
y = [5, 7, 3, 8, 4]
plt.title("Simple Bar graph") # Name title of the graph
plt.xlabel('Students') # Assign the name of the x axis
plt.ylabel("Math Score") # Assign the name of the y axis
plt.bar(x, y, color='red') # Change bar color
plt.show()

#How to show values or labels on top of bar
barplot = plt.bar(x, y)
for bar in barplot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom') #va: vertical alignment y positional argument
    
plt.title("Simple Bar graph")
plt.xlabel('Students')
plt.ylabel("Math Score")

#How to hide axis
plt.yticks([])

#How to show string values in Bar Graph

x = ['A', 'B', 'C', 'D', 'E']
y = [5, 7, 3, 8, 4]
plt.bar(x, y)

#Horizontal Bar Chart
plt.barh(x,y)
plt.title("Simple Horizontal Bar graph")
plt.xlabel("Math Score")
plt.ylabel('Students')

#How to sort or order bars

y,x = zip(*sorted(zip(y,x)))
plt.barh(x,y)

#Reverse order of bars
plt.barh(x,y)
ax=plt.subplot()
ax.invert_yaxis()

#Use Professional Themes / Styles for Graphs
print(plt.style.available)
plt.style.use('fivethirtyeight')

# 2.Line Graph
import pandas as pd

df = pd.DataFrame({"Year" : [2014,2015,2016,2017,2018], 
                  "Sales" : [2000, 3000, 4000, 3500, 6000]})
# plot line chart
plt.plot(df["Year"], df["Sales"])
plt.title("Simple Line Plot")
plt.xlabel('Year')
plt.ylabel('Sales')

#Pandas can make graphs by calling plot directly from the data frame. 
#Plot can be called by defining plot type in kind= option. 
#Syntax of Plot in Pandas

df.plot(x="Year", y="Sales", kind="line")
'''
- 'line' for line plot (Default)
- 'bar'  for vertical bar plots
- 'barh' for horizontal bar plots
- 'hist' for histogram
- 'pie' for pie plots
- 'box' for boxplot
- 'kde' for density plots
- 'area' for area plots
- 'scatter' for scatter plots
- 'hexbin' for hexagonal bin plots
'''
df.plot(x="Year", y="Sales", kind="bar")

df.plot(x="Year", y="Sales", kind="scatter")

df.plot(x="Year", y="Sales", kind="pie")

#Add Marker in Line Plot
ax = df.plot(x="Year", y="Sales", kind="line", title ="Simple Line Plot", legend=False, style = 'ro--')
ax.set(ylabel='Sales', xlabel = 'Year', xticks =df["Year"])
'''
You can also use these styles ro, ro--, r+, rD-.. 
They refer to cirles, dash lines, dash-dotted lines. You can mention any color ('g' for green, 'b' for blue, 'k' for black etc.)
.set method is used to add x and y axis labels, limits and ticks. 
It can also be written like the code below -

'''
ax.set_ylabel('Sales')
ax.set_xlabel('Year')
ax.set_xticks(df["Year"])

'''
Syntax of ax.set family functions is equivalent to plt. styling functions. 
See comparison of some of them -
ax.set_ylabel() plt.ylabel()
ax.set_xlabel() plt.xlabel()
ax.set_xticks() plt.xticks()
'''

#Add Multiple Lines in Line Graph Pandas Way
import pandas as pd

product = pd.DataFrame({"Year" : [2014,2015,2016,2017,2018], 
                  "ProdASales" : [2000, 3000, 4000, 3500, 6000],
                  "ProdBSales" : [3000, 4000, 3500, 3500, 5500]})


# Multi line plot
ax = product.plot("Year", "ProdASales", kind="line", label = 'Product A Sales')
product.plot("Year", "ProdBSales", ax= ax , kind="line", label = 'Product B Sales', title= 'MultiLine Plot') #ax : axes object

# Set axes
ax.set(ylabel='Sales', xlabel = 'Year', xticks =df["Year"])

# 3. Scatter Plot
ax = product.plot("Year", "ProdASales", kind='scatter', color = 'red', title = 'Year by ProductA Sales')
ax.set(ylabel='ProductA Sales', xlabel = 'Year', xticks =df["Year"])
plt.show()

# 4. Pie Chart

share = [20, 12, 11, 4, 3]
companies = ['Google', 'Facebook', 'Apple', 'Microsoft', 'IBM', ]
comp = pd.DataFrame({"share" : share, "companies" : companies})
ax = comp.plot(y="share", kind="pie", labels = comp["companies"], autopct = '%1.0f%%', legend=False, title='Market Share')

# Hide y-axis label
ax.set(ylabel='')

#Customize Pie Chart

# Customize Pie Chart
ax = comp.plot(y="share", kind="pie", labels = comp["companies"], startangle = 90, shadow = True, 
        explode = (0.1, 0.1, 0.1, 0, 0), autopct = '%1.0f%%', legend=False, title='Market Share')
ax.set(ylabel='')
plt.show()

# 5.Histogram

'''
Histogram is used to show the frequency distribution of a continuous variable. 
Suppose you want to see the distribution of marks got by students.
'''

# Creating random data
import numpy as np
np.random.seed(1)
mydf = pd.DataFrame({"Age" : np.random.randint(low=20, high=100, size=50)})

# Histogram
ax = mydf.plot(bins= 5, kind="hist", rwidth = 0.7, title = 'Distribution - Marks', legend=False)
ax.set(xlabel="Bins")
plt.show()

#How to add multiple sub-plots
labels = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai']
x1 = [45, 30, 15, 10]
x2 = [25, 20, 25, 50]

finaldf = pd.DataFrame({"2017_Score":x1, "2018_Score" : x2, "cities" : labels})

#Method 1

fig = plt.figure()

ax1 = fig.add_subplot(121)
ax = finaldf.plot(x="cities",  y="2017_Score", ax=ax1, kind="barh", legend = False, title = "2017 Score")
ax.invert_yaxis()

ax2 = fig.add_subplot(122)
ax = finaldf.plot(x="cities",  y="2018_Score", ax=ax2, kind="barh", legend = False, title = "2018 Score")
ax.invert_yaxis()
ax.set(ylabel='')

#Method 2

fig, (ax0, ax01) = plt.subplots(1, 2)

ax = finaldf.plot(x="cities",  y="2017_Score", ax=ax0, kind="barh", legend = False, title = "2017 Score")
ax.invert_yaxis()

ax = finaldf.plot(x="cities",  y="2018_Score", ax=ax01, kind="barh", legend = False, title = "2018 Score")
ax.invert_yaxis()
ax.set(ylabel='')

#How to show sub-plots vertically
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax = finaldf.plot(x="cities",  y="2017_Score", ax=ax1, kind="barh", legend = False, title = "2017 vs 2018 Score")
ax.invert_yaxis()
plt.xticks(range(0,60,10))
ax.set(ylabel='')

ax2 = fig.add_subplot(212)
ax = finaldf.plot(x="cities",  y="2018_Score", ax=ax2, kind="barh", legend = False)
ax.invert_yaxis()
ax.set(ylabel='')

#How to save plot
# save plot
x = ['A','B','C', 'D']
y = [1,2,3,4]
fig = plt.figure()
plt.bar(x, y)
fig.savefig('firstimg.png')
plt.close(fig)