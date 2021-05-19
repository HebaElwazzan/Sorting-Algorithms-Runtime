from matplotlib import pyplot as plt
import random
import time
import bubble
import insertion
import selection
import merge
import quick
import heapsort


def copy_array(array):  # function to copy contents of array
    size = len(array)
    temp = [0] * size  # temporary array to pass to the functions

    for j in range(size):
        temp[j] = array[j]

    return temp


def generate_dataset(size):
    array = [0] * size  # initializing an array of zeros

    for i in range(size):  # loop to replace the zeros in array with random numbers
        array[i] = int(random.random() * 10)  # random numbers from 0 to 9

    return array


# function that runs specified sort and returns time in milliseconds taken for run
def run_sort(array, sorting_func):
    temp = copy_array(array)
    if sorting_func == quick.sort_by_quicksort:
        start_time = time.time()
        sorting_func(temp, 0, len(array) - 1)
        end_time = time.time()
    else:
        start_time = time.time()
        sorting_func(temp)
        end_time = time.time()
    return (end_time - start_time) * 1000


def generate_data():
    size_values = [10, 50, 100, 200, 500, 750, 1000, 2000, 5000, 7500, 10000]
    bubble_values = []
    insertion_values = []
    selection_values = []
    merge_values = []
    quick_values = []
    heap_values = []
    for value in size_values:
        array = generate_dataset(value)
        bubble_values.append(run_sort(array, bubble.bubble_sort))
        insertion_values.append(run_sort(array, insertion.sort_by_insertion))
        selection_values.append(run_sort(array, selection.selection_sort))
        merge_values.append(run_sort(array, merge.merge_sort))
        quick_values.append(run_sort(array, quick.sort_by_quicksort))
        heap_values.append(run_sort(array, heapsort.heapsort))
    plt.plot(size_values, bubble_values, label="Bubble Sort")
    plt.plot(size_values, insertion_values, label="Insertion Sort")
    plt.plot(size_values, selection_values, label="Selection Sort")
    plt.plot(size_values, merge_values, label="Merge Sort")
    plt.plot(size_values, quick_values, label="Quick Sort")
    plt.plot(size_values, heap_values, label="Heapsort")
    plt.title("Time Performance of Sorting Algorithms")
    plt.xlabel("Array size")
    plt.ylabel("Time (milliseconds)")
    plt.legend()
    plt.show()
