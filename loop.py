# # if
# n=int(input("Enter any no"))
# if(n%2==0):
#     print(f'{n}even no')
#     print('even no=',n)
#     print("hello")
    
# # if-else
# n=int(input("Enter your age"))
# if n>=18:
#     print("Eligibal for vote")
# else:
#     print("not Eligible for vote")

# n=int(input("Enter your percentage:"))
# if (n>=100):
#     print("pleace enter valid no:")
# else:
#     if(n>=60):
#         print(f'{n} is 1st division')
#     elif(n<=45 and n<60):
#         print(f'{n} is 2nd division')
#     elif(n<=35 and n<45):
#         print(f'{n} is 3rd division')
    
# n=int(input("Enter any no"))
# i=1
# while i<=n:
#     print(i,end=',')
#     i=i+1
    
    
n=int(input("Enter any no"))
i=1
while i<=n:
    if i<n:
        print(i,end=',')
    else:
        print(i)    
    i=i+1
    

n=int(input("Enter any no"))
i=1
sum=0
while i<=n:
    sum=sum+i
    if i<n:
        print(i,end='+')
    else:
        print(i,end='=')    
    i=i+1
print(sum)
    

