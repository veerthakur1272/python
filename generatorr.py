# def first():
#     return 'hello'
# x=first()
# print(x)


# def first():
#     yield 'hello'
# x=first()
# print(x)


# def first():
#     yield 1
#     yield 2
#     yield 3
# x=first()
# print(x)
# print(list(x))

# def first():
#     yield 1
#     yield 2
#     yield 3
# x=first()
# print(next(x))
# print("hi")
# print("hello")
# print("welcome")
# print(next(x))

def natural_no(x):
    i=1
    while i<=x:
        yield i
        i=i+1
n=int (input("Enter any number:"))
p=natural_no(n)
print(next(p))
for i in p:
    print(i)

        