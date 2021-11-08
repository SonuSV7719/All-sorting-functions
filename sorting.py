# Intertion Sort ----------------------------------------------------------->>>

def intertionSort(array):
    n = len(array)-1
    for i in range(n):
        j = i+1
        if array[i]>array[j]:
            array[i], array[j] = array[j], array[i]
        k = i
        while k>=0 and array[k-1]>array[k]:
            if (k-1)<0:
                break
            elif array[k]<array[k-1]:
                array[k], array[k-1] = array[k-1], array[k]
                k -= 1
            else:
                k -= 1
    return array

# shell sort -------------------------------------------------------------------------

def shellSort(array):
    gap = len(array) // 2 
    while gap > 0:
        i = 0
        j = gap
        while j < len(array):
     
            if array[i] >array[j]:
                array[i],array[j] = array[j],array[i]
             
            i += 1
            j += 1
            k = i
            while k - gap > -1:
                if array[k - gap] > array[k]:
                    array[k-gap],array[k] = array[k],array[k-gap]
                k -= 1
        gap //= 2
    return array 

# Quik Sort ---------------------------------------------------------------->>

def quikSort(array, start, end):
    if start < end:
        pivot = array[start]
        i = start+1
        j = end
        while True:
            while i<=j and array[i]<=pivot:
                i+=1
            while i<=j and array[j]>=pivot:
                j-=1
            if j<i:
                break
            else:
                array[i], array[j] = array[j], array[i]
        array[start], array[j] = array[j], array[start]
        quikSort(array, start, j-1)
        quikSort(array, j+1, end)
        return array

# Bubble Sort ------------------------------------------------------------->>

def bubbleSort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(n-1):
            if array[j]>array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
    return array

# Merge Sort ---------------------------------------------------------------->>

def sort(array, low, high):
    if high>low:
        mid = (low+high)/2
        sort(array, low, mid)
        sort(array, mid+1, high)
        merged = merge(array, low, high, mid)
        return merged

def merge(array, low, high, mid):
    merge1 = []
    merge2 = []
    n = mid-low+1
    m = high-mid
    for i in range(n):
        merge1.append(array[low+i])
    for i in range(m):
        merge2.append(array[mid+1+i])
    i=0
    j=0
    k=low
    while i<n and j<m:
        if merge1[i]<merge2[j]:
            array[k]=merge1[i]
            i+=1
            k+=1
        else:
            array[k]=merge2[j]
            j+=1
            k+=1
    while i<n:
        array[k] = merge1[i]
        i+=1
        k+=1
    while j<m:
        array[k]=merge2[j]
        j+=1
        k+=1
    return array

