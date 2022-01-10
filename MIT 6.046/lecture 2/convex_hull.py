"""This function find the intersection between the verticle line to find the upper tanget and lower tangent"""


def point_of_intersection(point1, point2, xcord):
    return ((point1[1] - point2[1]) / (point1[0] - point2[0])) * (xcord - point1[0]) + point1[1]


'''Starting from the nearest point from vertical line xcord
   for upper tangent: 
                    rotate  array2 (greater side of xcord) in  clockwise direction
                    rotate  array1 (smaller side of xcord) in  anticlockwise direction
   for lowe tanget: 
                  rotate array2 in anticlockwise direction
                  rotate array1 in clockwise direction
'''


def little_finger(array1, array2, xcord):
    min1 = None
    temp = float('inf')
    for i in range(len(array1)):
        if abs(xcord - array1[i][0]) < temp:
            min1 = i
            temp = abs(xcord - array1[i][0])
    min2 = None
    temp2 = float('inf')
    for i in range(len(array2)):
        if abs(xcord - array2[i][0]) < temp2:
            min2 = i
            temp2 = abs(xcord - array2[i][0])
    i = min1
    j = min2
    length1 = len(array1)
    length2 = len(array2)
    while point_of_intersection(array1[i], array2[(j + 1) % length2], xcord) > point_of_intersection(array1[i],
                                                                                                     array2[j],
                                                                                                     xcord) or \
            point_of_intersection(array1[i - 1], array2[j], xcord) > point_of_intersection(array1[i], array2[j], xcord):
        if point_of_intersection(array1[i], array2[(j + 1) % length2], xcord) > point_of_intersection(array1[i],
                                                                                                      array2[j], xcord):
            j = (j + 1) % length2
        else:
            i = (i - 1) % length1
    m = min1
    n = min2
    while point_of_intersection(array1[m], array2[n - 1], xcord) < point_of_intersection(array1[m], array2[n], xcord) or \
            point_of_intersection(array1[(m + 1) % length1], array2[n], xcord) < point_of_intersection(array1[m],
                                                                                                       array2[n],
                                                                                                       xcord):
        if point_of_intersection(array1[m], array2[n - 1], xcord) < point_of_intersection(array1[m], array2[n], xcord):
            n = (n - 1) % length2
        else:
            m = (m + 1) % length1
    return (i, j), (m, n)


''' convex hull using divide and conquer
    merge :
            start from the right upper tanget vertex go clockwise till right lower tangert vertex
            jump to left lower tangent vertex go clockwise till left upper tanget vertex
'''


def convex_hull(array):
    if len(array) <= 2:
        return array
    array.sort(key=lambda x: x[0])
    array1 = convex_hull(array[:len(array) // 2])
    array2 = convex_hull(array[len(array) // 2:])
    xcord = (array[len(array) // 2 - 1][0] + array[len(array) // 2][0]) / 2
    (ti, tj), (li, lj) = little_finger(array1, array2, xcord)
    result = []
    i = tj
    while i != lj:
        result.append(array2[i])
        i = (i + 1) % len(array2)
    result.append(array2[lj])
    j = li
    while j != ti:
        result.append(array1[j])
        j = (j + 1) % len(array1)
    result.append(array1[ti])
    return result
