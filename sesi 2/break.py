print()
print('1')
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)

print()
print('2')
for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')

print()
print('3')
for i in ['foo', 'bar', 'baz', 'qux']:
  if i == 'bar':
    break
  print(i)
else:
  print('Done.') 