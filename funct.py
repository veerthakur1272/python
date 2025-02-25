# def add(x,y,z):
#     "for addition of 3-variables"
#     return x+y+z
# p=int(input("Enter 1st no:"))
# q=int(input("Enter 2st no:"))
# r=int(input("Enter 3st no:"))
# res=add(p,q,r)
# print(res)
# print(add.__doc__)

# ====================================

# def add(x,y,z):
#     "for addition of 3-variables"
#     return x+y+z
# p=int(input("Enter 1st no:"))
# q=int(input("Enter 2st no:"))
# # r=int(input("Enter 3st no:"))
# res=add(p,q,)
# print(res)
# print(add.__doc__)

# ====================================

# def add(x,y,z):
#     print("x:",x)
#     print("y:",y)
#     print("z:",z)
#     return x+y+z
# p=int(input("Enter 1st no:"))
# q=int(input("Enter 2st no:"))
# r=int(input("Enter 3st no:"))
# res=add(z=p,y=q,x=r)
# print(res)

# ====================================

# def add(x,y,z):
#     print("x:",x)
#     print("y:",y)
#     print("z:",z)
#     return x+y+z
# p=int(input("Enter 1st no:"))
# q=int(input("Enter 2st no:"))
# r=int(input("Enter 3st no:"))
# res=add(r,p,q)
# print(res)

# ====================================

# def add(x=0,y=10,z=0):
#     print("x:",x)
#     print("y:",y)
#     print("z:",z)
#     return x+y+z
# p=int(input("Enter 1st no:"))
# q=int(input("Enter 2st no:"))
# r=int(input("Enter 3st no:"))
# res=add(10)
# print(res)

# ====================================

# def add(*n):
#     print(n)
#     print(type(n))


# res=add(2,4,6,8,10,2)

# ====================================

# def add(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum


# res=add(2,4,6,8,10,2)
# print(res)

# ====================================

# x=eval(input("Enter your value:"))
# print(x)
# print(type(x))

# ====================================

def add(*args):
    sum=0
    for i in args:
        for j in i:
          sum=sum+j
    return sum
x=eval(input("Enter ny typle:"))
res=add(*x)
print(res)

# ====================================

# def add(*args):
#     print(args)
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# x=eval(input("Enter ny typle:"))
# res=add(*x)