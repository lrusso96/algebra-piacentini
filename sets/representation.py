# coding=utf-8

"""
Utilizzando la notazione dei sottoinsiemi di un dato universo U = {a1, a2, ...
an} sotto forma di n-ple di 0 e 1, si scriva un programma che trovi unione,
intersezione, complementari, ecc. di sottoinsiemi di U
"""

from gmpy2 import mpz


class Set(object):

    @classmethod
    def mpz_to_padded_string(cls, m: mpz, size: int):
        return m.digits(2).zfill(size)

    def to_string_repr(self):
        return Set.mpz_to_padded_string(self.repr, self.size)

    @classmethod
    def to_set(cls, s):
        ss = ""
        for i, c in enumerate(s):
            if c == "1":
                ss += f"a{i+1}, "
        ss = "{" + ss[:-2] + "}"
        return ss

    def to_set_repr(self):
        return Set.to_set(self.to_string_repr())

    def __init__(self, name, repr: str, mask=None, size=None):
        self.name = name
        if repr == None:
            assert mask != None and size != None
            self.repr = mask
            self.size = size
        else:
            self.size = len(repr)
            self.repr = mpz(repr, 2)

    def __len__(self):
        return self.to_string_repr().count('1')

    def __str__(self):
        return f"{self.name}: {self.to_set_repr()}"

    def union(self, b):
        assert self.size == b.size
        name = f"({self.name} ∪ {b.name})"
        return Set(name, None, self.repr | b.repr, self.size)

    def intersect(self, b):
        assert self.size == b.size
        name = f"({self.name} ∩ {b.name})"
        return Set(name, None, self.repr & b.repr, self.size)

    def comp(self):
        u = Set("u", "1"*self.size)
        name = f"C({self.name})"
        return Set(name, None, self.repr ^ u.repr, self.size)

    def diff(self, b):
        assert self.size == b.size
        i = self.intersect(b)
        name = f"({self.name} - {b.name})"
        return Set(name, None, self.repr ^ i.repr, self.size)


def main():

    s1 = Set("S1", "010")
    s2 = Set("S2", "110")
    print(f"{s1} has {len(s1)} element{'' if len(s1) == 1 else 's'}")
    print(f"Its string representation is {s1.to_string_repr()}")
    print(f"{s2} has {len(s2)} element{'' if len(s2) == 1 else 's'}")
    print(f"Its string representation is {s2.to_string_repr()}")

    s3 = s1.union(s2)
    print(f"The union set between {s1.name} and {s2.name} is the set {s3}")
    print(f"Its string representation is {s3.to_string_repr()}")

    s3 = s1.intersect(s2)
    print(
        f"The intersection set between {s1.name} and {s2.name} is the set {s3}")
    print(f"Its string representation is {s3.to_string_repr()}")

    c1 = s1.comp()
    print(f"The complement of the set {s1.name} is the set {c1}")
    print(f"Its string representation is {c1.to_string_repr()}")

    s3 = s1.diff(s2)
    print(
        f"The difference set between {s1.name} and {s2.name} is the set {s3}")
    print(f"Its string representation is {s3.to_string_repr()}")

    s3 = s2.diff(s1)
    print(
        f"The difference set between {s2.name} and {s1.name} is the set {s3}")
    print(f"Its string representation is {s3.to_string_repr()}")


if __name__ == '__main__':
    main()
