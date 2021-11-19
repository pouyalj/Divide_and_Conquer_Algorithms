

def MergeSort(input_list):
    
    if (len(input_list) == 0):
        return input_list
    elif (len(input_list) == 1):
        return input_list

    elif (len(input_list) > 1):
        # Recursion and Merge
        first_half = MergeSort(input_list[0:int(len(input_list)/2)])
        second_half = MergeSort(input_list[int(len(input_list)/2):])
        return merge(first_half, second_half)
        
        

def merge(first_array, second_array):

    merged_array = []
    i = 0
    j = 0
    for k in range(0, len(first_array) + len(second_array)):
        if (i < len(first_array) and j < len(second_array)):
            if (first_array[i] < second_array[j]):
                merged_array.append(first_array[i])
                i += 1
            elif (second_array[j] < first_array[i]):
                merged_array.append(second_array[j])
                j += 1
            elif (first_array[i] == second_array[j]):
                merged_array.append(first_array[i])
                merged_array.append(second_array[j])
                i += 1
                j += 1

        # Account for running out of index in each sub array | Or running out of index in both
        elif (i >= len(first_array) and j >= len(second_array)):
            return merged_array

        elif (i >= len(first_array)):
            merged_array.append(second_array[j])
            j += 1

        elif (j >= len(second_array)):
            merged_array.append(first_array[i])
            i += 1

    return merged_array


if (__name__ == "__main__"):

    print(MergeSort([12, 11, 13, 5, 6, 7]))