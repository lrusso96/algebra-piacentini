"""
A matrix is represented here as a tuple of tuples.
Each tuple is a row vector.
"""


def print_relation(matrix):
    for row in matrix:
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
    print("So the matrix is {} an equivalence relation!".format(
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
    print("So the matrix is {} a partial order!".format(
        "" if reflexive and antisymmetric and transitive else "NOT"))


def is_reflexive(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            print("Element at index {} does not satisfy refelxivity".format(i))
            return False
    return True


def is_symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] != matrix[j][i]:
                print("Elements at index ({}, {}) do not satisfy symmetry".format(i, j))
                return False
    return True


def is_antisymmetric(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] == 1 and matrix[j][i] == 1:
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

print("We can also test if a relation is a partial order.")
relation = (
    (1, 0, 1, 1),
    (1, 1, 1, 1),
    (1, 0, 1, 0),
    (0, 0, 1, 1)
)

check_partial_order(relation)
