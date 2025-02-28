# x=(input("enter any no:"))
# y=(input("enter any no:"))
# res=lambda p,q: p+q
# print(res(x,y))


# x=(input("enter any no:"))
# y=(input("enter any no:"))
# res=lambda p,q: print(p+q)
# print(res(x,y))
# res(x,y)


# x=int(input("enter any no:"))
# res=lambda y:'even' if(y%2==0) else 'odd'
# print(res(x))


# l1=[]
# for i in range(3):
#     l1.append(10)
# print(l1)

# l1=[]
# for i in range(1,4):
#     l1.append(i)
# # print(l1)
# l2=[]
# for i in range(4):
#     l2.append(l2)
# print(l2)

# lambda collection:[i for i in collection]
# x='veer'
# z=lambda str1:[i for i in str1]
# print(z(x))

x=4
res=lambda p:[i for i in range(1,p) for k in range(p)]
print(res(x))
