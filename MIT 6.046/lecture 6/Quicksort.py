"""Intialise the counter i=j=first element of array and pivot=last element of array
   if array[j]< pivot swap array(i,j) and increment i
   last swap array(i,pivot) element
   this algorithm give in place 0(n) partitioning in 0(1) extra memory
"""


def pivot(array, a, b):
    i = a
    x = array[b - 1]
    for j in range(a, b - 1):
        if array[j] < x:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i], array[b - 1] = array[b - 1], array[i]
    return i


'''This Quicksort algorithms work on randomise input
   we can do better introducing randomisation to algorithm
'''


def Quicksort(array, start, end):
    if start < end:
        q = pivot(array, start, end)
        Quicksort(array, start, q)
        Quicksort(array, q + 1, end)

array=[1,3,4,6,9,7,5]
print(pivot(array,0,6))
print(array)
