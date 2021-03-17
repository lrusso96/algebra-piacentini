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
    print(
        f"So the relation is {'' if reflexive and symmetric and transitive else 'NOT'} an equivalence relation!")


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
    print(
        f"So the relation is {'' if reflexive and antisymmetric and transitive else 'NOT'} a partial order!")


def is_reflexive(relation):
    for i in range(len(relation)):
        if relation[i][i] == 0:
            print(f"Element at index {i} does not satisfy refelxivity")
            return False
    return True


def is_symmetric(relation):
    for i in range(len(relation)):
        for j in range(i):
            if relation[i][j] != relation[j][i]:
                print(f"Elements at index ({i}, {j}) do not satisfy symmetry")
                return False
    return True


def is_antisymmetric(relation):
    for i in range(len(relation)):
        for j in range(i):
            if relation[i][j] == 1 and relation[j][i] == 1:
                print(
                    f"Elements at index ({i}, {j}) do not satisfy antisymmetry")
                return False
    return True


def is_transitive(relation):
    for i in range(len(relation)):
        for j in range(len(relation)):
            if i != j and relation[i][j] == 1:
                for k in range(len(relation)):
                    if i != k and relation[j][k] == 1 and relation[i][k] == 0:
                        print(
                            f"Elements at index ({i}, {j}, {k}) do not satisfy transitivity")
                        return False
    return True


def is_total_order(relation):
    for i in range(len(relation)):
        for j in range(i):
            if relation[i][j] == 0 and relation[j][i] == 0:
                print(f"Elements at index {i}, {j}, are not comparable!")
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
