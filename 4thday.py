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
x=10
y=20
print(id(x),id(y))

# string
x='anam'
y='sayyed'
print(id(x), id(y))                     

# tuple
x=(10,20,30)
y=(10,20,30)
print(id(x), id(y))

# same memory location int,string, tuple

# mutable natutre
# # list
x1=[10,20,30,'anam']
x2=[10,20,30,'anam']
print(id(x1), id(x2))

# output -2715897717056 2715897865600--[different memory location]

# dictionary
x1={'anam':'sayyed','age' :37, 'city': 'Bhopal'}
x2={'anam':'sayyed','age' :37, 'city': 'Bhopal'}
print(id(x1), id(x2))

# output=2532868743040 2532869137408--[different memory location]

# set
x1={10,20,30,40,'anam',20,30}
x2={10, 20, 30,40,'anam',20,30}
print(id(x1), id(x2))
#  output= 2288130392800 2288130678048---[different memory location]

#frozenset
x1=frozenset({10, 20, 30,40,'anam',20,30})
x2=frozenset({10, 20, 30,40,'anam',20,30})
print(id(x1), id(x2))

# output- 2335581036480 2335581036928---[different memory location]
# ...........................................................................................


# indexing
# two types of indexing
# positive indexing +ve
# negative indexing -ve

# use for find object in collection