import random

def rand_selection(array, start , stop, order_stat):
    if(start < stop):
        # Partition by random pivot and return pivot index
        pivotindex = partitionrand(array, start, stop)
        # Base case covered by len 1 and len 2 arrays as well as pivot = order stat
        # Recursion
        if(len(array) == 1):
            return array[0]
        elif(len(array) == 2):
            if(pivotindex == order_stat-1):
                return array[pivotindex]
            else:
                return array[pivotindex - 1]
        elif(pivotindex == order_stat-1):
            return array[pivotindex]
        elif(order_stat-1 < pivotindex):
            array = array[start:pivotindex]
            # Handle edge case (len = 1) of left side
            if(len(array) == 1):
                return array[0]
            return rand_selection(array , start , len(array)-1, order_stat) 
        elif(order_stat-1 > pivotindex):
            array = array[pivotindex+1:len(array)]
            # Handle edge case (len = 1) of right side
            if(len(array) == 1):
                return array[0]
            return rand_selection(array, 0, len(array)-1, (order_stat - pivotindex - 1))
        

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
print(rand_selection(array,0,n-1,8))
# print(array[0:n])
