#------------------------------------------------------------------------------------------------
#Memory Addresses

month = "May"
age = 18

print("Month Memory ID =", id(month))
print("Age Memory ID =", id(age))


#------------------------------------------------------------------------------------------------
#Creating Python Variables

counter = 100          # Creates an integer variable
miles   = 1000.0       # Creates a floating point variable
name    = "Zara Ali"   # Creates a string variable

print ("Integer: ", counter)
print ("Float: ", miles)
print ("String: ", name)


#------------------------------------------------------------------------------------------------
#Deleting Python Variables

counter = 100
print ("Counter: ", counter)

del counter
# print ("Counter: ", counter)


#------------------------------------------------------------------------------------------------
#Getting Type of a Variable

x = "Zara"
y =  10
z =  10.10

print(type(x))
print(type(y))
print(type(z))


#------------------------------------------------------------------------------------------------
#Casting Python Variables

x = str(10)    # x will be '10'
y = int(10)    # y will be 10 
z = float(10)  # z will be 10.0

print( "x =", x )
print( "y =", y )
print( "z =", z )


#------------------------------------------------------------------------------------------------
#Case-Sensitivity of Python Variables

age = 20
Age = 30

print( "age =", age )
print( "Age =", Age )


#------------------------------------------------------------------------------------------------
#Python Variables - Multiple Assignment

a = b = c = 100

print (a)
print (b)
print (c)


#------------------------------------------------------------------------------------------------
#Python Variables - Multiple Assignment

a,b,c = 1,2,"Zara Ali"

print (a)
print (b)
print (c)


#------------------------------------------------------------------------------------------------
#Python Variables - Naming Convention

counter = 100
_count  = 100
name1 = "Zara"
name2 = "Nuha"
Age  = 20
zara_salary = 100000

print (counter)
print (_count)
print (name1)
print (name2)
print (Age)
print (zara_salary)


#------------------------------------------------------------------------------------------------
#invalid Python variable names

# 1counter = 100
# $_count  = 100
# zara-salary = 100000

# print (1counter)
# print ($count)
# print (zara-salary)


#------------------------------------------------------------------------------------------------
#area and perimeter

width = 10
height = 20
area = width*height
perimeter = 2*(width+height)
print ("Area = ", area)
print ("Perimeter = ", perimeter)


#------------------------------------------------------------------------------------------------
#Python Local Variables

def sum(x,y):
   sum = x + y
   return sum
print(sum(5, 10))


#------------------------------------------------------------------------------------------------
#Python Global Variables

x = 5
y = 10
def sum():
   sum = x + y
   return sum
print(sum())


#------------------------------------------------------------------------------------------------
#Constants in Python

MAX_SIZE = 100
PI = 3.14159
DATABASE_NAME = "mydatabase"


#------------------------------------------------------------------------------------------------