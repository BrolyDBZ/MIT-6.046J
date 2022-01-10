from random import getrandbits


def getrandom(n):
    return [int(getrandbits(1)) for _ in range(n)]


def matrix_mult(A, b):
    return [sum([b[i] * k for i, k in enumerate(A[m])]) for m in range(len(A))]


def matrix_multiplication(A, B, C, epoch):
    for i in epoch:
        random = getrandom(len(A[0]))
        check = matrix_mult(A, random)
        result1 = matrix_mult(B, check)
        result2 = matrix_mult(C, random)
        if result1 != result2:
            return False
    return True
