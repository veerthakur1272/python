# def sqr(n):
#     return n**2
# l1=eval(input("Enter any collection:"))
# x=map(sqr,l1)
# print(list(x))

# x=eval(input("Enter any collection:"))
# l1=[]
# for i in x :
#     y=i**2
#     l1.append(y)
# print(l1)


# l1=[1,2,3,4,5]
# l2=[2,3,4,5]
# l3=[3,4]

def add(x,y,z):
    return x+y+z 
l1=eval(input("enter any no:"))
l2=eval(input("enter any no:"))
l3=eval(input("enter any no:"))
p=tuple(map(add,l1,l2,l3))
print(p)

