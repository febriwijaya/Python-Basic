print()
print('1')
a = ['foo', 'bar', 'baz']
for i in a:
    print(i)


print()
print('2')
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

print()
print('3')
for k in d.values():
    print(k)

print()
print('3')
for k, v in d.items(): 
    print(k, ":", v) 