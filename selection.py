def selection_sort(array):
    for i in range(len(array)):
        i_min = i
        for j in range(i+1, len(array)):
            if array[j] < array[i_min]:
                i_min = j  # finding minimum value in unsorted array
        if i != i_min:
            array[i], array[i_min] = array[i_min], array[i]  # swap if a smaller value exists
