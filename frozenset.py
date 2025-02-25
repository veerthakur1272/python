# s="Neeraj"
# fs=frozenset(s)
# print(fs)
# print(type(fs))

s={10,20,30,40}
s1=[2,4,6,10,20]
x=frozenset(s)
x1=frozenset(s1)
# print(x.union(x1))
# print(x.difference(x1))
# print(x.intersection(x1))
# print(x.symmetric_difference(x1))
print(x.isdisjoint(x1))
print(x.issubset(x1))
print(x.issuperset(x1))