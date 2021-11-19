# Inversion:
# if i < j then A[i] > A[j] would be an inversion for any pair of (i,j)


count = 0

def inver_count(input_list):
    
    global count

    if (len(input_list) == 1):
        return input_list

    # Recursion and count
    else:
        first_half = inver_count(input_list[0:int(len(input_list)/2)])
        second_half = inver_count(input_list[int(len(input_list)/2):])
        return merge_and_count(first_half, second_half)


def merge_and_count(first_array, second_array):

    global count
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
                count = count + (len(first_array) - i)
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




print(inver_count([12,11,13,5,6,7]))
print(count)