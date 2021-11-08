x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')


x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')


hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup")

hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
elif uang > hargaMajalah:
    print("beli majalah")
else:
    print("uang tidak cukup")

name = 'Hacktiv8'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Hacktiv8':
    print('Hello Hacktiv8')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

if 'a' in 'bar':
    print('foo')
elif 1/0:
    print("This won't happen")
elif var:
    print("This won't either")