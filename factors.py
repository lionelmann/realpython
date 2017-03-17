def divisor(x):
    for i in range(1, x + 1):
        if x % i == 0:
            print("{} is a divisor of {}".format(i, x))


integer = input("Enter a positive integer: ")

x = int(integer)

divisor(x)
