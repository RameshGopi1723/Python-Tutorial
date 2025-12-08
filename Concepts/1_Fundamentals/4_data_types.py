#------------------------------------------------------------------------------------------------
#Python Numeric Data Types

var1 = 1       # int data type
var2 = True    # bool data type
var3 = 10.023  # float data type
var4 = 10+3j   # complex data type


#------------------------------------------------------------------------------------------------
#Example of Numeric Data Types

# integer variable.
a=100
print("The type of variable having value", a, " is ", type(a))

# float variable.
c=20.345
print("The type of variable having value", c, " is ", type(c))

# complex variable.
d=10+3j
print("The type of variable having value", d, " is ", type(d))


#------------------------------------------------------------------------------------------------
#Python String Data Type

str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string


#------------------------------------------------------------------------------------------------
#Python Sequence Data Types
    # -List Data Type
    # -Tuple Data Type
    # -Range Data Type

#Python List Data Type
#Python Lists are the most versatile compound data types. A Python list contains items separated by commas and enclosed within square brackets ([]). To some extent, Python lists are similar to arrays in C. One difference between them is that all the items belonging to a Python list can be of different data type where as C array can store elements related to a particular data type.

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(type(list))
print(list)            # Prints complete list
print(list[0])         # Prints first element of the list
print(list[1:3])       # Prints elements starting from 2nd till 3rd 
print(list[2:])        # Prints elements starting from 3rd element
print(tinylist * 2)    # Prints list two times
print(list + tinylist) # Prints concatenated lists


#------------------------------------------------------------------------------------------------
#Python Tuple Data Type

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples


#------------------------------------------------------------------------------------------------
#Python Range Data Type

#range(start, stop, step)

for i in range(5):
  print(i)

for i in range(2, 5):
  print(i)
  
for i in range(1, 5, 2):
  print(i)
  
#------------------------------------------------------------------------------------------------
#Python Dictionary Data Type

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

#------------------------------------------------------------------------------------------------
