import time
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt

def bubbleSort(arr):
    n = len(arr)


    for i in range(n-1):



        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
