# def outer_fun(new):
#     def inner_fun():
#         print("Hello")
#     return inner_fun
# @outer_fun
# def new():
#     pass 
# new()

def outer_fun(s):
    def inner_fun(p,q):
        p=p+10
        q=q+10
        r=s(p,q)
        print(r)
    return inner_fun
@outer_fun
def new(x,y):
    return x+y
p=int (input("Enter any number"))
q=int(input("Enter any number"))
new(p,q) 