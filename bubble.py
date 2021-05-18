import time


# from numpy.random import seed
# from numpy.random import randint
# import matplotlib.pyplot as plt

def bubble_sort(arr):
    start = time.time()

    n = len(arr)

    for i in range(n - 1):

        flag = 0

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1
        if not flag:
            break

    print(f"Array sorted using Bubble Sort = {arr}\n")
    print(f"Runtime for sorting array using Bubble Sort = {time.time() - start}\n")
