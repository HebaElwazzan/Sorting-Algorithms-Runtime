# zero indexed (not like the reference's pseudocode)
def _left(i):
    return 2 * i + 1


def _right(i):
    return 2 * i + 2


def _max_heapify(array, heap_size, i):
    left = _left(i)
    right = _right(i)
    if left < heap_size and array[left] > array[i]:
        largest = left
    else:
        largest = i
    if right < heap_size and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        _max_heapify(array, heap_size, largest)


def _build_max_heap(array, heap_size):
    for i in range(heap_size // 2 - 1, -1, -1):
        _max_heapify(array, heap_size, i)


def heapsort(array):
    heap_size = len(array)
    _build_max_heap(array, heap_size)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heap_size -= 1
        _max_heapify(array, heap_size, 0)
