import random

def quicksort(array, start , stop):
    if(start < stop):
        pivotindex = partitionrand(array, start, stop)
        # Recursion
        quicksort(array , start , pivotindex-1)
        quicksort(array, pivotindex + 1, stop)

# divide function
def partitionrand(array , start, stop):
 
    # Random Pivot
    randpivot = random.randrange(start, stop)
    array[start], array[randpivot] = array[randpivot], array[start]
    return partition(array, start, stop)
 
# Partition
def partition(array,start,stop):
    pivot = start
    i = start + 1
     
    # partition in the arrayay starts
    for j in range(start + 1, stop + 1):
         
        if array[j] <= array[pivot]:
            array[i] , array[j] = array[j] , array[i]
            i = i + 1
    array[pivot] , array[i-1] = array[i-1] , array[pivot]
    pivot = i - 1
    return pivot

# main
array = [3,8,2,5,1,4,7,6]
n = len(array)
quicksort(array,0,n-1)
print(array)
