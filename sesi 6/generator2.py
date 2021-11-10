def counter_generator(low, high):
    while low <= high:
      yield low
      low += 1

# for i in counter_generator(2,22):
#   print(i, end=' ')

object_gen = counter_generator(5,10)
print(next(object_gen))
print(next(object_gen))
print(next(object_gen))
print(next(object_gen))
print(next(object_gen))
print(next(object_gen))