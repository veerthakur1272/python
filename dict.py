# d={'name':'veer',
# 'age':20,
# 'quali':'b.comm'}
# print(d)
# print(type(d))

# d={'name':'Veer','age':'20','Quit':'B.com'}
# print(max(d))
# print(min(d))
# print(len(d))
# print(id(d))
# print(type(d))

# x=dict()
# print(x)     # for empty dict
# print(type(x))

# d1={'name':'ajay','age':20,'quali':'b.com'}
# print(d1.get('name'))


# d1={'name':'ajay','age':20,'qualifactin':'b.com'}
# print(d1.keys())
# print(d1.values())
# print(d1.items())
# d1.pop('name')  #targate any pair throught remove
# print(d1)
# d1.popitem()     remove last items
# print(d1)

# d1.setdefault('name','rahul')
# print(d1)
# d1.update({'name':'rahul','grad':'first'})
# print(d1)

s='veer'
x=dict.fromkeys(s,50)
print(x)
