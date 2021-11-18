def add(*args):
    # print positional arguemnts
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 4, 5, 15, 32, 1))
