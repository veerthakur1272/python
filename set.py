# s={10,20,30,'veer','raj','rahul',10,20}
# print(s)
# print(type(s))

# s1={10,20,30,10,30,60,40,50}
# print(max(s1))
# print(min(s1))
# print(sum(s1))
# print(type(s1))
# print(id(s1))
# print(len(s1))

# s1={10,20,10,30,60,40,50}
# s1.add(80)
# print(s1)
# print(s1.copy())
# s1.update('veer')
# print(s1)
# s1.discard(70)
# print(s1)
# print(s1.clear())
# s1.pop('name')  #targate any pair throught remove

# a={2,4,6,8}
# b={1,2,3,4}
# print(a.union(b))
# print(a)

# a={2,4,6,8}
# b={1,2,3,4}
# print(a.intersection(b))
# print(a)

# a={2,4,6,8}
# b={1,2,3,4}
# print(a.intersection_update(b))
# print(a)

# a={2,4,6,8}
# b={1,2,3,4}
# print(a.difference(b))
# print(a)

# a={2,4,6,8}
# b={1,2,3,4}
# print(a.symmetric_difference(b))
# print(a)

# a={2,4,6,8}
# b={1,2,3,4}
# b.intersection_update(a)
# print(b)

# a={2,4,6,8}
# b={1,2,3,4}
# b.difference_update(a)
# print(b)

a={2,4,6,8}
b={1,2,3,4}
a.symmetric_difference_update(a)
print(a)

