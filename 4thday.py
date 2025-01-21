# py call by refrence
# x=10
# y=20
# print(id(x))
# print(id(y))
# output-140709877253320
# 140709877253640-memory location 

# py call by obj refrence
# types of 1-mutable, 2-immutable

# integer
# x=10
# y=20
# print(id(x),id(y))

# string
# x='anam'
# y='sayyed'
# print(id(x), id(y))                     

# tuple
# x=(10,20,30)
# y=(10,20,30)
# print(id(x), id(y))

# same memory location int,string, tuple

# mutable natutre
# # list
# x1=[10,20,30,'anam']
# x2=[10,20,30,'anam']
# print(id(x1), id(x2))

# output -2715897717056 2715897865600--[different memory location]

# dictionary
# x1={'anam':'sayyed','age' :37, 'city': 'Bhopal'}
# x2={'anam':'sayyed','age' :37, 'city': 'Bhopal'}
# print(id(x1), id(x2))

# output=2532868743040 2532869137408--[different memory location]

# set
# x1={10,20,30,40,'anam',20,30}
# x2={10, 20, 30,40,'anam',20,30}
# print(id(x1), id(x2))
#  output= 2288130392800 2288130678048---[different memory location]

#frozenset
# x1=frozenset({10, 20, 30,40,'anam',20,30})
# x2=frozenset({10, 20, 30,40,'anam',20,30})
# print(id(x1), id(x2))

# output- 2335581036480 2335581036928---[different memory location]
# ...........................................................................................


# indexing
# two types of indexing
# positive indexing +ve
# negative indexing -ve

# use for find object in collection

# str1= 'python'
# print(str1.index('p'))
# output=0

# str1= 'python'
# print(str1.index('o'))
# output-4

# str1= 'python'
# print(str1.index('p',1))
# output=substring not found-error

# str1= 'python'
# print(str1.index('p',0,1))
# output-0


# str1= 'python'
# print(str1(0))  

# l1=[10,20,30,40,'Anam',50]
# print(l1.index(10))
# output-0

# l1=[10,20,30,40,'Anam',10,50]
# print(l1.index(10,1))
# output=5

# l1=[10,20,30,40,'Anam',10,50]
# print(l1.index(20,1,3))
# output=1

# '''''''''''''.............................................'''''''''''''''''''''

# tuple
# l1=(10,20,30,40,'Anam',10,50)
# print(l1.index(40))
# output-3
# .........................................................................

# Slicing
# Slicing examples with different data types

# String slicing
str1 = "Python Programming"
print(str1[0:6])      # Python
print(str1[7:])       # Programming
print(str1[-11:-1])   # rogrammin
print(str1[::2])      # Pto rgamn
print(str1[::-1])     # gnimmargorP nohtyP

# List slicing 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1[0:5])     # [1, 2, 3, 4, 5]
print(list1[::2])     # [1, 3, 5, 7, 9]
print(list1[2:7:2])   # [3, 5, 7]
print(list1[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Tuple slicing
tuple1 = (10, 20, 30, 40, 50, 60)
print(tuple1[1:4])    # (20, 30, 40)
print(tuple1[::2])    # (10, 30, 50)
print(tuple1[::-1])   # (60, 50, 40, 30, 20, 10)


 