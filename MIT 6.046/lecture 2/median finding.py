
"""This implementation give us 0(n) rank finding to an array as theoritical stand point"""


def pick(array):
    select = [array[i:i + 5] for i in range(0, len(array), 5)]
    for i in select:
        i.sort()
    select.sort(key=lambda x: x[len(x) // 2])
    x = select[len(select) // 2]
    return x[len(x) // 2]


def rank_finding(array, rank):
    x = pick(array)
    left = []
    right = []
    for i in array:
        if i >= x:
            right.append(i)
        else:
            left.append(i)
    if len(left) == rank:
        return x
    elif len(left) > rank:
        return rank_finding(left, rank)
    else:
        return rank_finding(right, rank - len(left))
