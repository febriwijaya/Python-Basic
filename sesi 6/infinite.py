def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

is_generator = infinite_sequence()