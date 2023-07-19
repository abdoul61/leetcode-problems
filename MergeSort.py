#This problem deal with multiple sorted arrays  
# The idea is to use a MinHeap that can take up to n elements
# assuming n is the number of arrays



import heapq
from typing import List
def MergeSort(A:List[int],B:List[int],C:List[int])->List[int]:
    result = []
    heap = []
    n = 0
    if len(A) < len(B) and len(B) < len(C):
        n = len(C)
    else:
        n = len(A)
    i = 0

    while i < n:
        a = A[i]
        b = B[i]
        c = C[i]
        heap.append(a)
        heap.append(b)
        heap.append(c)
        heapq.heapify(heap)
        el = heapq.heappop(heap)
        result.append(el)
        i += 1
    i1 = i
    i2  = i
    while i1 < len(B):
        el = B[i1]
        heap.append(el)
        heapq.heapify(heap)
        p = heapq.heappop(heap)
        result.append(p)
        i1 += 1

    while i2 < len(C):
        el = C[i2]
        heap.append(el)
        heapq.heapify(heap)
        p = heapq.heappop(heap)
        result.append(p)
        i2 += 1

    
    while heap:
        el = heapq.heappop(heap)
        result.append(el)

    return result

A = [3,5]
B = [8,9,12,13]
C = [1,6,7,11]
print(MergeSort(A,B,C))
