# import string

# spc_chr = string.punctuation
# print(spc_chr)
# print (len(spc_chr))
# x=string.ascii_letters
# y=string.ascii_lowercase
# z=string.ascii_uppercase
# p=string.digits
# q=string.hexdigits
# r=string.printable
# print(x)
# print(y)
# print(z)
# print(q)

# x=10
# X=10
# _x=10
# print(x,X,_x)

# # 1x=10
# # print(1x)

# name="Veer"
# print(name)

# Veer="1234"
# print(Veer)

# x1="10"
# print(x1)


# x=10
# y=20
# z=30
# print(not (x>y) and (y<z))


# # membership   (in, not in)
# str1="veer"
# print('n' not in str1)


# identity (is ,is not)
# python lag is call by value
# x=10
# y=10
# print(x is y)

# # or

# x=[10]
# y=[10]
# print(x is y)

# x=10
# y=10
# print(id(x))
# print(id(y))

# x=[10]
# y=[10]
# print(id(x),id(y)) #object check adderss by identity operator is ,is not 

# bitwise operator 

# x=10
# y=20
# print(x&y)

# x=10
# y=20
# print(x|y)

# x=10
# print(~x)

# x=10
# y=20
# print(x^y)

# Left shift is(<<)
# x=10
# print(10<<1)

# Right shift is(>>)
# x=20
# print(x>>2)

# return value= Arithmetic,assigriment,bitwisw
# return boolean= campairision(compaire value)true/false,logical,identity(compair memory address)true/false,membership


# # Inbuilt - function

# 1. Print()==> check output
# 2. input()==> To take runtime input
# 3. Id ()==> To check address
# Print (id(x))
# 4. type()==> To check data type
# Print(type(x))
# 5. Min()==>
# 6. Max()==>
# 7. Len()==>
# 8. Som()==>

# Literals 
# type of literals
# 1. numeric = integar,float, complex
# 2. string = collection of charactors 
#    => represented in
# I'  '      single-line string
# II "  "    
# III '''  '''  multi-line string

# exp:-
# x='n'
# print(x)
# print(type(x))
    
# y="n"
# print(y)
# print(type(y))
    
# y='''n'''
# print(y)
# print(type(y))


# x='''  *
#     **
#       ***
#      ****
#     *****'''
# print(x)
# print(type(x))
# x=''''this
#            is
#               pythone class'''
# print(x)
# print(type(x))

# list:-
#   => collection of object
#   => repersented by [ ] with comma(,) seperated object
  
#  object=> Homogeneus =>(sema dta-type)
#  =>hetrogenous =>(diff data-type)
 
# l1=[10,25,10+2j,'veer',[10,20,30]]
# print(l1)
# print(type(l1))
# #  print(type(l1))
 
 
# l1=[10,20,30]
# l2=[10,20,30]
# print(id(l1),id(l2))
#     #  |
#     # diffarent
#     #    |
#     #   multable data-type 

# # tuple:-
# # => collection of object(homog,hetog)
# # => respresnted in ( )
# # with comma(.) seperated objects.
# # => immutable in nuture
# # exp:-
# t1=(10,20,30,'veer')
# print(t1)
# print(type(t1))
# t2=(10,20,20.5,'veer')
# print(id(t1),id(t2))
# #      |
# #  same adders
# #      |      
# # imutable


# Dict 
# => collection of object
#          |
#       kay valui
#          |
#          object
         
# => represented in{ } with
# comma(,) seperated object
# =>mutable in nuture

# Ex;-
#  d1['name':'veer','age':18],'qua'
#   raha gya hai or







# # Set 
# => collection of unique object
# =>represtented in{ } with
# comma(,) seperated object
# =>mutable in nutare



s1={10,20,'veer','jai','ray'}
print(s1)
print(type(s1))
s2={10,20,'veer','raja','sandeep'}
print(id(s1),id(s2))
#          |
#   differant memory adderss
#          |
#        mutable       

