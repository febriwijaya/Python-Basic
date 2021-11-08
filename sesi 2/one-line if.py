if 'a' in 'bar':
    print('foo')
elif 1/0:
    print("This won't happen")
elif var:
    print("This won't either")

if 'f' in 'foo': print('1'); print('2'); print('3')

if 'z' in 'foo': print('1'); print('2'); print('3')

x = 2

if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

x = 3
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

x = 3
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')