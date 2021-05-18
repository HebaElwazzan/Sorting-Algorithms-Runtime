import time  # imports time class to measure time taken by sorting method


def sort_by_insertion(array, n):

    start = time.time()  # start time of sorting

    for x in range(1, n):  # x starts from 1 since first element in array is automatically put in sorted part
        key = array[x]  # key = first element in unsorted part
        hole = x  # hole = index of the end of sorted part

        while hole > 0 and array[hole - 1] > key:  # loops till sorted part has been passed completely or if selected element is smaller than key
            array[hole] = array[hole - 1]  # replaces value of current element with value of previous element
            hole -= 1  # decrements hole to go over next element in the sorted part

        array[hole] = key  # replaces value of current element with value of key

    print(f"Array sorted using Insertion Sort = {array}\n")
    print(f"Runtime for sorting array using Insertion Sort = {time.time() - start}\n")
