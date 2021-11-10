def my_generator():
  print("Inside my generator")
  yield 'a'
  yield 'b'
  yield 'c'

print('print with for')
for char in my_generator():
  print(char)