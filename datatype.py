# datatype
# numeric- integer, float, complex

# string              
# list
# tuple
# dict--- maped data type
# set
# frozenset
# boolean

# collection
# ordered ------ string, list, tuple, dict
# unordered-------set, frozenset---its hold unqiue content-- can not use duplicate content.
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Numeric-
# Integer:-
# x=10
# y=20
# print(type(x))
# print(type(y))
# z=x+y
# print(type(z))
# output-<class 'int'>
# <class 'int'>
# <class 'int'>

# x=10
# y=20
# print(type(x))
# print(type(y))
# z=x-y
# print(type(z))

# x=10
# y=20
# print(type(x))
# print(type(y))
# z=x*y
# print(type(z))
# print(type(z))

# x=10
# y=20
# print(type(x))
# print(type(y))
# z=x/y
# print(type(z)) 
# output-<class 'float'>
# .........................................................................

# Float

# x=10.5
# y=20.5
# print(type(x))
# print(type(y))
# z=x+y
# print(type(z))

# x=10.5
# y=20.5
# print(type(x))
# print(type(y))
# z=x-y
# print(type(z))

# x=10.5
# y=20.5
# print(type(x))
# print(type(y))
# z=x*y
# print(type(z))

# x=10.5
# y=20.5
# print(type(x))
# print(type(y))
# z=x/y
# print(type(z))

# output-<class 'float'>
# ------------------------------------------------------------------------------------------

# complex

# x=10.5+3j
# y=20.5+5j
# print(type(x))
# print(type(y))
# z=x/y
# print(type(z))
# output-<class 'complex'>
# -------------------------------------------------------------------------------------------------

# 2.String:

# s1='Python'
# print(type(s1))
# output-<class 'str'>

# in-build function:

# print()
# s1='Python'
# print(type(s1))
# output-<class 'str'>

# input()
# x=input("enter your name :")
# print(x)
# print(type(x))
# output-anam
# id()

# x=input("enter your name :")
# print(x)
# print(id(x))
# output-anam
# 3019095911776

# max()
# s1='python'
# print(max(s1))
# output-y

# min()
# s1='python'
# print(min(s1))
# output-h

# len()
# s1='python'
# print(len(s1))
# output-6

# diffe between function and method

# Method:
# lower()
# upper()
# title()
# capitaliza()
# find()
# index()
# join()
# spilt()

str1="I love python"                
print(str1.lower())
print(str1.upper())
print(str1.title())
print(str1.capitalize())
print(str1.swapcase())
# output= i love python
# i love python
# I LOVE PYTHON
# I Love Python
# I love python
# i LOVE PYTHON

# print(str1.index('z')) -----------error
print(str1.find('P'))
# output=-1
print(str1.find('z'))
# output=-1= 
# the diff. between index and find is index is geneate ERROR and index provide -1

print(str1.split())
# ['I', 'love', 'python']---return in list form---by default spilt through space

print(str1.split('o'))
# output=['I l', 've pyth', 'n']

print(str1.split('o',1))
# output=['I l', 've python']
# -------------------------------------------------------------------------------------------------

# Join
li=['Anam','Sayyed','Bhopal']
print('*'.join(li).split('p'))
# output=['Anam*Sayyed*Bho', 'al']
x=','.join(li)
# output=Anam,Sayyed,Bhopal--------single obj. output
# print(type(x))
# output=<class 'str'>
# --------------------------------------------------------------------------------------------------

# Count
print(str1.count('o'))
# output=2
# --------------------------------------------------------------------------

# List

