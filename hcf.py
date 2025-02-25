# x=6
# y=30
# z=18
# p=min(x,y,z)
# q=1
# i=1
# while i<p:
#     if x%i==0 and y%i==0 and z%i==0:
#         q=q*i
#     i=i+1
# print("hcf is",q)

x=8
y=12
m=min(x,y)
while m>0:
    if x%m==0 and y%m==0:
        hcf=m
        break
    m=m-1
print("hcf is=",hcf)

