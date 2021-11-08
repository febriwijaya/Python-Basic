print('1')
n = 5
while n > 0:
    n -= 1
    print(n)

print()
print('2')
i = 1
while i < 6:
  print(i)
  i += 1

print()
print('3')
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break # Break Statement
    print(n)
print('Loop ended.')

print()
print('4')
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')