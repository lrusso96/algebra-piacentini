"""
A relation is represented here as a tuple of tuples.
Each tuple is a row vector.
"""


def print_relation(relation):
    for row in relation:
        print(row)


def check_equivalence(relation):
    print("Going to check the equivalence of relation")
    print_relation(relation)
    print("Is it reflexive?")
    reflexive = is_reflexive(relation)
    if reflexive:
        print("YES")
    print("Is it symmetric?")
    symmetric = is_symmetric(relation)
    if symmetric:
        print("YES")
    print("Is it transitive?")
    transitive = is_transitive(relation)
    if transitive:
        print("YES")
    print("So the relation is {} an equivalence relation!".format(
        "" if reflexive and symmetric and transitive else "NOT"))


def check_partial_order(relation):
    print("Going to check the partial order of the relation")
    print_relation(relation)
    print("Is it reflexive?")
    reflexive = is_reflexive(relation)
    if reflexive:
        print("YES")
    print("Is it antisymmetric?")
    antisymmetric = is_antisymmetric(relation)
    if antisymmetric:
        print("YES")
    print("Is it transitive?")
    transitive = is_transitive(relation)
    if transitive:
        print("YES")
    print("So the relation is {} a partial order!".format(
        "" if reflexive and antisymmetric and transitive else "NOT"))


def is_reflexive(relation):
    for i in range(len(relation)):
        if relation[i][i] == 0:
            print("Element at index {} does not satisfy refelxivity".format(i))
            return False
    return True


def is_symmetric(relation):
    for i in range(len(relation)):
        for j in range(i):
            if relation[i][j] != relation[j][i]:
                print("Elements at index ({}, {}) do not satisfy symmetry".format(i, j))
                return False
    return True


def is_antisymmetric(relation):
    for i in range(len(relation)):
        for j in range(i):
            if relation[i][j] == 1 and relation[j][i] == 1:
                print(
                    "Elements at index ({}, {}) do not satisfy antisymmetry".format(i, j))
                return False
    return True


def is_transitive(relation):
    for i in range(len(relation)):
        for j in range(len(relation)):
            if i != j and relation[i][j] == 1:
                for k in range(len(relation)):
                    if i != k and relation[j][k] == 1 and relation[i][k] == 0:
                        print(
                            "Elements at index ({}, {}, {}) do not satisfy transitivity".format(i, j, k))
                        return False
    return True


def is_total_order(relation):
    for i in range(len(relation)):
        for j in range(i):
            if relation[i][j] == 0 and relation[j][i] == 0:
                print("Elements at index {}, {}, are not comparable!".format(i, j))
                return False
    return True


def main():
    print("We express relations as Python tuples of tuples")
    print("For example, this is the 'equality' relation defined over a set of n=4 elements")

    relation = (
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1)
    )

    print_relation(relation)

    print("\nLet's make an example with a custom relation.")
    relation = (
        (0, 1, 1, 1),
        (1, 0, 0, 1),
        (1, 0, 0, 0),
        (1, 1, 0, 0)
    )

    check_equivalence(relation)

    print("\nWe can also test if a relation is a partial order.")
    print("We now test the 'lower than' relation...")
    relation = (
        (1, 0, 0, 0),
        (1, 1, 0, 0),
        (1, 1, 1, 0),
        (1, 1, 1, 1)
    )

    check_partial_order(relation)
    print("Let's if it is a total order...")
    print("Yes it is!" if is_total_order(relation) else "So it is not!")

    print("\nConsider the following instead ('is subset' defined on the Powerset).")
    relation = (
        (1, 1, 1, 1),
        (0, 1, 0, 1),
        (0, 0, 1, 1),
        (0, 0, 0, 1)
    )

    check_partial_order(relation)
    print("Let's if it is a total order...")
    print("Yes it is!" if is_total_order(relation)
          else "So it is not a total order!")


if __name__ == '__main__':
    main()
