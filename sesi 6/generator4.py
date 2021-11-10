def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

x = simpleGeneratorFun()

print(next(x))
print(next(x))
print(next(x))
