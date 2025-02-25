# x=6
# y=12
# z=8
# p=max(x,y,z)
# while True:
#     if p%x==0 and p%y==0 and p%z==0:
#         break
#     p=p+1
# print(f'lcm of {x}, {y} and {z} is {p}')

            #  OR

x=6
y=12
z=8
p=q=max(x,y,z)
i=1
while True:
    if q%x==0 and q%y==0 and q%z==0:
        break
    i=i+1
    q=p*i
print("lcm is =",q)