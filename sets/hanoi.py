"""
Si scriva un programma che calcoli in modo ricorsivo il numero minimo di mosse
necessario per risolvere il gioco della torre di Hanoi con n dischi.
Si scriva anche una versione che utilizzi la formula chiusa.
"""


def hanoi_recursive(n):
    if n == 1:
        return 1
    return 1 + 2*hanoi_recursive(n-1)


def hanoi(n):
    return 2**n - 1


if __name__ == '__main__':
    n = int(input("Insert number of disks: "))
    print("The number of moves is {}".format(hanoi(n)))
