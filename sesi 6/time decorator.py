import time
def timer(fn):
    def wrapper(x, y):
        start = time.time()
        res = fn(x, y)
        print('Waktu : ', time.time() - start)
        return res
    return wrapper
@timer
def add(x, y):
    return x + y
@timer
def sub(x, y):
    return x - y
print('Hasil: ', add(1, 2))
print('Hasil: ', add(3, 4))
print('Hasil: ', add(10, 20))
print('Hasil: ', sub(50, 20))
print('Hasil: ', sub(40, 10))
print('Hasil: ', sub(20, 1))