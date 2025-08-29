#list_methods

'''
append
extend
count 
index
remove
pop
insert

syntax: variable.method()
        print(variable)
'''

b=[1,2,3,1,4,5,2,"babu"]
print(type(b))
print(b)
print(len(b))
print(b)
b.append(35)
print(b)
b.extend([1,2,3,444])
print(b)
print(b.count(1))
print(b.index(3))
b.remove(3)
print(b)
b.pop(2)
print(b)
b.insert(4,"kumar")
print(b)
