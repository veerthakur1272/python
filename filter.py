# l1=[1,2,3,4,5,6,7,8,9]
def even(n):
    if n%2==0:
        return n
l1=eval(input("Enter any no:"))
x=list(filter(even,l1))
print(x)


def odd(n):
    if n%2!=0:
        return n
l1=eval(input("Enter any no:"))
x=list(filter(odd,l1))
print(x)