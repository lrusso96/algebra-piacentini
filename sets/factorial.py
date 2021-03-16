from functools import reduce


def factorial_recursive(n):
    assert n >= 0
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


def factorial(n):
    assert n >= 0
    if n == 0 or n == 1:
        return 1
    return reduce(lambda a, b: a*b, [i for i in range(2, n+1)])


def main():
    n = int(input("Enter a non negative number n: "))
    print("{}! = {}".format(n, factorial(n)))


if __name__ == '__main__':
    main()
