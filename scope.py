# # local variable
# x=10   
# def new():
#     y=20
#     print(x)
#     print(y)
# new()
# print(x)
# # print(y)


# x=10   
# def update(p):
#     global x
#     x=p
#     print(x)
# print("before update call",x) 
# x=int(input("Enter any number :"))
# update(x)
# print("after update call",x)

# x=10   
# def update(p):
#     global x
#     x=p
#     print("before update:",globals()['x']) 
# y=int(input("Enter any number :"))
# print("before update:",x) 
# update(y)
# print("after update call",x)



# palindrom
n=int(input("Enter any number:"))
x=n
rev=0
while n>0:
    last_digit=n%10
    rev=rev*10+last_digit
    n=n//10
if(rev==x):
    print("palinder")
else:
    print("not palinder")


