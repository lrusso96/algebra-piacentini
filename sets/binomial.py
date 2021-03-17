from functools import reduce


def binomial_dumb(n, k):
    assert n >= 0 and k >= 0

    def factorial(x):
        if x == 0 or x == 1:
            return 1
        return x * factorial(x-1)

    return factorial(n) // (factorial(n-k) * factorial(k))


def binomial(n, k):
    assert n >= 0 and k >= 0

    def prod(a, b):
        return a*b

    diff = n - k
    num = max(diff, k)
    den = min(diff, k)
    numerator = reduce(prod, [i for i in range(den + 1, n + 1)] + [1])
    denominator = reduce(prod, [i for i in range(1, num + 1)] + [1])

    return numerator // denominator


def main():
    n = int(input("Insert n: "))
    k = int(input("Insert k: "))
    print(f'Binomial ({n} / {k}): {binomial(n, k)}')


if __name__ == '__main__':
    main()
