raining = False
print("Let's go to the", 'beach' if not raining else 'library')

raining = True
print("Let's go to the", 'beach' if not raining else 'library')

age = 12
s = 'teen' if age < 21 else 'adult'
s

'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'