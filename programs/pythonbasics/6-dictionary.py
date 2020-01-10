#Dictionary
tele ={'raghu':9845547471,'rakesh':9898989898,'govind':8787676765}

print(tele['rakesh'])

tele ={'raghu':9845547471,'rakesh':9898989898,'govind':8787676765,'raghu':9845547472}
print(tele['raghu'])

#copying
duptele = tele.copy()
print(duptele)

#Update

tele.update({'rakesh':8888888888})
print(tele)

tele.update({'raghu':9888888888})
print(tele)

#Delete key

del tele ['rakesh']
print(tele)

# keys
print("keys ", tele.keys())

#values 
print("Values ", tele.values())

#items
print("items %s :",tele.items())
#check for existance of keys
Common = {'Tim': 19,'Charlie':12,'Tiffany':22,'Robert':25}

Boys = {'Tim': 18,'Charlie':12,'Rakesh':25}

Girls = {'Tiffany':22,'Sanjana':18}

for key in Boys.keys():

    if key in Common.keys():
        print(True)
    else:
        print(False)


#Built in function

#len
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print(" %d elements are in dictionary " % len (Dict))
print("Length : %d",len (Dict))
#print(len(Dict), "elements are in dictionary")

#variable type

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("variable Type: %s" %type (Dict))


Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("printable string:%s" % str (Dict))

# empty dictionary
my_dict = {}

my_dict['Raghu'] = 8383838838

my_dict['Raghavendra'] = 9383838838

print('new dictionary is ',my_dict)

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})
print('dict ',my_dict)
# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
print('dict:sequence ',my_dict)
#Accessing elements
my_dict = {'name':'Jack', 'age': 26}
# Output: Jack
print(my_dict['name'])
# Output: 26
print(my_dict.get('age'))

# Trying to access keys which doesn't exist throws error
# my_dict.get('address')
# my_dict['address']

#How to change or add element to dictionary

my_dict = {'name':'Jack', 'age': 26}

# update value
my_dict['age'] = 27

#Output: {'age': 27, 'name': 'Jack'}
print(my_dict)

# add item
my_dict['address'] = 'Downtown'  

# Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
print(my_dict)

# Remove or delete elements
# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}  

# remove a particular item
# Output: 16
print(squares.pop(4))  
# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item
# Output: (1, 1)
print(squares.popitem())

# Output: {2: 4, 3: 9, 5: 25}
print(squares)

# delete a particular item
del squares[5]  

# Output: {2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del squares

# Throws Error
# print(squares)


marks= {}.fromkeys(['Math','English','Science'], 100)

# Output: {'English': 100, 'Math': 100, 'Science': 100}
print(marks)
for item in marks.items():
    print(item)

# Output: ['English', 'Math', 'Science']
list(sorted(marks.keys()))


#Python Dictionary Comprehension
#Dictionary comprehension is an elegant and concise way to create new dictionary from an iterable in Python.

#Dictionary comprehension consists of an expression pair (key: value) followed by for statement inside curly braces {}.

#Here is an example to make a dictionary with each item being a pair of a number and its square.

squares = {x: x*x for x in range(6)}

# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares)
#This code is equivalent to
squares = {}
for x in range(6):
   squares[x] = x*x


#Dictionary Membership Test
squares= {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# Output: True
print(7 in squares)
# Output: True
print(2 not in squares)

# membership tests for key only not value
# Output: False
print(49 in squares)

#Iterating Through a Dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(i)

# Output: 5
print(len(squares))

# Output: [1, 3, 5, 7, 9]
print(sorted(squares))

#printing key and values

for k, v in squares.items():
    print(k, v)

# Dynamically creating a dictionary

myfamily = {}
myfamily['raghu'] = 9845547471
myfamily['vidya'] = 9008663619
print(myfamily)

#name = 'satvik'
#phone = 8888888888

name = input("enter the name ")
phone = int(input("enter the mobile"))

myfamily[name] = phone

print(myfamily)

