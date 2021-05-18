import random
import time
import insertion
import quick
import bubble
import merge
import selection


def copy_array(array, n):  # function to copy contents of array

    for j in range(n):
        temp[j] = array[j]

    return temp


size = int(input("Enter size of array: "))
ar = [0] * size  # initializing an array of zeros
temp = [0] * size  # temporary array to pass to the functions
beg = 0  # start of array
end = size - 1  # end of array

for i in range(size):  # loop to replace the zeros in array with random numbers
    ar[i] = int(random.random() * 10)  # random numbers from 0 to 9

temp = copy_array(ar, size)  # copies contents of original array to temporary array

print(f"\nGenerated array = {ar}\n")

insertion.sort_by_insertion(temp, len(temp))

temp = copy_array(ar, size)
start = time.time()  # start time for Quicksort

quick.sort_by_quicksort(temp, beg, end)

print(f"Array sorted using Quicksort = {temp}\n")
print(f"Runtime for sorting array using Quicksort = {time.time() - start}\n")

temp = copy_array(ar, size)

bubble.bubble_sort(temp)

temp = copy_array(ar, size)
start = time.time()  # start time for Merge sort

merge.merge_sort(temp)

print(f"Array sorted using Merge sort = {temp}\n")
print(f"Runtime for sorting array using Merge sort = {time.time() - start}\n")

temp = copy_array(ar, size)
start = time.time()  # start time for selection sort

selection.selection_sort(temp)

print(f"Array sorted using Selection sort = {temp}\n")
print(f"Runtime for sorting array using Selection sort = {time.time() - start}\n")
