import random
from collections import deque
import time
import sys

f = open("date.in", "r")
g = open("date.out", "w")
teste = int(f.readline().split()[0])

def test_sort(v):
    global v1
    for x in range(0, len(v)):
        if v[x] != v1[x]:
            return 0
    return 1

def radixsort_counting(n, m, v, baza):
    v2 = [0 for x in range(0,n)]
    exp = 1
    while (m // exp) > 0:
        count = [0 for x in range(0,baza)]
        for i in range(0,n):
            count[(v[i] // exp) % baza]+=1
        for i in range(1,baza):
            count[i] += count[i-1]
        for i in range(n-1,-1,-1):
            v2[count[(v[i] // exp) % baza] - 1] = v[i]
            count[(v[i] // exp) % baza]-=1
        for i in range(0,n):
            v[i] = v2[i]
        exp*=baza

def radixsort_bucket(m,v,baza):
    qt = []
    for x in range(0, baza):
        qu = deque()
        qt.append(qu)
    exp = 1
    while (m // exp) > 0:
        for x in v:
            poz = (x // exp) % baza
            qt[poz].appendleft(x)
        i = 0
        for queueindex in qt:
            while queueindex:
                element = queueindex.pop()
                v[i] = element
                i+=1
        exp*=baza

def radixsort_bucket_2at16(m,v):
    qt = []
    baza = 1<<16
    for x in range(0, baza):
        qu = deque()
        qt.append(qu)
    exp = 0
    while (m>>exp) > 0:
        power = 1<<exp
        for x in v:
            poz = (x >> exp) & (baza-1)
            qt[poz].appendleft(x)
        i = 0
        for queueindex in qt:
            while queueindex:
                element = queueindex.pop()
                v[i] = element
                i+=1
        exp += 16

def mergesort(v,st,dr):
    if st < dr:
        mij = (st+dr)//2
        mergesort(v,st,mij)
        mergesort(v,mij+1,dr)
        #merge rezultat
        left = v[st:mij+1]
        right = v[mij+1:dr+1]
        i = j = 0
        k = 0
        while(i < len(left) and j < len(right)):
            if left[i] < right[j]:
                v[st+k] = left[i]
                k+=1
                i+=1
            else:
                v[st+k] = right[j]
                k+=1
                j+=1
        while i < len(left):
            v[st+k] = left[i]
            k+=1
            i+=1
        while j < len(right):
            v[st+k] = right[j]
            k+=1
            j+=1

# def shellsort(v,n):
#     range = n//2
#     while range > 0:
#         dr = range
#         while dr < n:
#             tmp = v[dr]
#             second = dr
#             while second >= range and v[second - range] > tmp:
#                 v[second] = v[second - range]
#                 second -= range
#             v[second] = tmp
#             dr += 1
#         range = range // 2

# pentru quicksort 
sys.setrecursionlimit(10**8)

def shellsort(v,n):
    range = 2
    while (range<<1)-1 < n:
        range = range<<1
    range-=1
    while range > 0:
        dr = range
        while dr < n:
            tmp = v[dr]
            second = dr
            while second >= range and v[second - range] > tmp:
                v[second] = v[second - range]
                second -= range
            v[second] = tmp
            dr += 1
        range = range>>1


def quicksort(v,st,dr):
    if st == dr - 1:
        if v[st] > v[dr]:
            v[st], v[dr] = v[dr], v[st]
    elif st < dr - 1:

        # aleg pivot cu mediana de 3:

        mijloc = (st+dr)//2
        if v[mijloc] < v[st]:
            v[st], v[mijloc] = v[mijloc], v[st]
        if v[dr] <= v[st]:
            v[st], v[mijloc], v[dr] = v[dr], v[st], v[mijloc]
        elif v[dr] <= v[mijloc]:
            v[mijloc], v[dr] = v[dr], v[mijloc]

        pivot = v[mijloc]

        i = st
        j = st
        k = dr

        while j <= k:
            if v[j] < pivot:
                v[i], v[j] = v[j], v[i]
                i+=1
                j+=1
            elif v[j] > pivot:
                v[k], v[j] = v[j], v[k]
                k-=1
            else:
                j += 1
        
        quicksort(v, st, i-1)
        quicksort(v, j, dr)

def heap_max_make(v, n, index):
    change = index
    st = 2 * index + 1
    dr = 2 * index + 2
    if st < n and v[st] > v[change]:
        change = st
    if dr < n and v[dr] > v[change]:
        change = dr
    if change != index:
        v[change], v[index] = v[index], v[change]
        heap_max_make(v, n, change)

def heapsort(v, n):

    for i in range(n//2-1, -1, -1):
        heap_max_make(v, n, i)

    for i in range(n-1, 0, -1):
        v[0], v[i] = v[i], v[0]
        heap_max_make(v,i,0)




for test in range(teste): # pentru fiecare test
    date = f.readline().split()
    n = int(date[0])
    m = int(date[1])
    g.write("Testul "+ str(test+1) + " N = " + date[0] + " M = " + date[1] + "\n\n")
    v1 = []
    v2 = []
    v3 = []
    v4 = []
    v5 = []
    v6 = []
    v7 = []
    v8 = []

    #generez testul 
    for nr in range(n):
        x = random.randint(0, m)
        v1.append(x)
        v2.append(x)
        v3.append(x)
        v4.append(x)
        v5.append(x)
        v6.append(x)
        v7.append(x)
        v8.append(x)

    ## in cazul in care doresc teste custom:

    # v1 = [x for x in range(1000000)]
    # v2 = [x for x in range(1000000)]
    # v3 = [x for x in range(1000000)]
    # v4 = [x for x in range(1000000)]
    # v5 = [x for x in range(1000000)]
    # v6 = [x for x in range(1000000)]
    # v7 = [x for x in range(1000000)]
    # v8 = [x for x in range(1000000)]

    # sort nativ python

    g.write("Sort Python - ")
    ti = time.process_time()
    v1.sort()
    tf = time.process_time() - ti
    g.write(str(tf) + " secunde ")
    g.write("\n")

    # radix sort pe baza custom folosind counting sort

    g.write("Radix Sort folosind Counting Sort - ")
    ti = time.process_time()
    radixsort_counting(n,m,v2,10) # inloc de 10 se poate pune orice baza dorita
    tf = time.process_time() - ti
    g.write(str(tf) + " secunde ")
    if test_sort(v2) == 1: # verific daca este ok sortarea
        g.write("E ok sortarea!")
    else:
        g.write("Nu e ok sortarea")
    g.write("\n")

    # radix sort pe baza 10 folosind bucket sort

    g.write("Radix Sort folosind Bucket Sort - Baza 10 - ")
    ti = time.process_time()
    radixsort_bucket(m,v3,10)
    tf = time.process_time() - ti
    g.write(str(tf) + " secunde ")
    if test_sort(v3) == 1: # verific daca este ok sortarea
        g.write("E ok sortarea!")
    else:
        g.write("Nu e ok sortarea")
    g.write("\n")

    # radix sort pe baza 2^16 folosind tot bucket sort

    g.write("Radix Sort folosind Bucket Sort - Baza 2^16 - ")
    ti = time.process_time()
    radixsort_bucket_2at16(m,v4)
    tf = time.process_time() - ti
    g.write(str(tf) + " secunde ")
    if test_sort(v4) == 1: # verific daca este ok sortarea
        g.write("E ok sortarea!")
    else:
        g.write("Nu e ok sortarea")
    g.write("\n")

    # merge sort 

    g.write("Merge Sort - ")
    ti = time.process_time()
    mergesort(v5,0,n-1)
    tf = time.process_time() - ti
    g.write(str(tf) + " secunde ")
    if test_sort(v5) == 1: # verific daca este ok sortarea
        g.write("E ok sortarea!")
    else:
        g.write("Nu e ok sortarea")
    g.write("\n")

    # shell sort
    
    g.write("ShellSort - ")
    ti = time.process_time()
    shellsort(v6,n)
    tf = time.process_time() - ti
    g.write(str(tf) + " secunde ")
    if test_sort(v6) == 1: # verific daca este ok sortarea
        g.write("E ok sortarea!")
    else:
        g.write("Nu e ok sortarea")
    g.write("\n")

    # Quicksort - Dutch Flag & Mediana din 3

    g.write("Quicksort - ")
    ti = time.process_time()
    quicksort(v7,0,n-1)
    tf = time.process_time() - ti
    g.write(str(tf) + " secunde ")
    if test_sort(v7) == 1: # verific daca este ok sortarea
        g.write("E ok sortarea!")
    else:
        g.write("Nu e ok sortarea")
    g.write("\n")

    # Heap Sort

    g.write("Heap Sort - ")
    ti = time.process_time()
    heapsort(v8, n)
    tf = time.process_time() - ti
    g.write(str(tf) + " secunde ")
    if test_sort(v8) == 1: # verific daca este ok sortarea
        g.write("E ok sortarea!")
    else:
        g.write("Nu e ok sortarea")
    g.write("\n")
    g.write("\n")

