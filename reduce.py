from functools import reduce
def mymax(x,y):
    if x>=y:
        return x
    else:
        return y
l1=eval(input("Enter any"))
p=reduce(mymax,l1)
print(p)