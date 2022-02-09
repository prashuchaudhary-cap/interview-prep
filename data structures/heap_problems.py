from heapq import heappop, heappush, heapify


# Given an array of size n, where every
# element is k away from its target
# position, sorts the array in O(nLogk) time.

m = n- k
O(k) + O((m) * log(k))
def sort_k(arr, n, k):
    heap = arr[:k+1]
    heapify(heap)

    sorted_array = []

    for index in range(k + 1, n):
        min_el = heappop(heap)
        sorted_array.append(min_el)
        heappush(heap, arr[index])

    while heap:
        el = heappop(heap)
        sorted_array.append(el)


#O(m*n*log(m))

def merge_m_sorted_array(mat, m, n):
    heap = []
    merged_array = []

    for i in range(m):
        heappush(heap, (mat[i][0], i, 0))

    while heap:
        min_el = heappop(heap)
        min_val, arr_idx, el_idx = min_el

        merged_array.append(min_val)

        if el_idx + 1 < n:
            heappush(heap, (mat[arr_idx][el_idx+1], arr_idx, el_idx+1))

    return merged_array


mat = [
    [10, 20, 30, 40 ],
    [15, 25, 35, 45 ],
    [27, 29, 37, 48 ],
    [32, 33, 39, 50 ],
    [16, 18, 22, 28 ]
]


def k_closest(arr, x, k):
    heap = []
    for i in range(k):
        heappush(heap, (-1*abs(arr[i]-x), arr[i]))

    for i in range(k, len(arr)):
        heappush(heap, (-1*abs(arr[i]-x), arr[i]))
        heappop(heap)

    while heap:
        item = heappop(heap)
        diff, val = item
        print(val)


arr = [10, 2, 14, 4, 7, 6]
k_closest(arr, 5, 3)


def k_top_frequent(freq, k):
    heap = []
    keys = list(freq.keys())
    for i in range(k):
        heappush(heap, (freq[keys[i]], keys[i]))

    for i in range(k, len(keys)):
        heappush(heap, (freq[keys[i]], keys[i]))
        heappop(heap)

    while heap:
        item = heappop(heap)
        diff, val = item
        print(val)


freq_map = {1: 3, 3: 1, 2:2, 4:3, 5:5}


arr = [7, 10, 4, 3, 20, 15]

def k_largest(arr, k):
    heap = []

    for i in range(k):
        heappush(heap, arr[i])

    for i in range(k, len(arr)):
        heappush(heap, arr[i])
        heappop(heap)

    return heap


def k_smallest(arr, k):
    heap = []

    for i in range(k):
        heappush(heap, -1*arr[i])

    for i in range(k, len(arr)):
        heappush(heap, -1*arr[i])
        heappop(heap)

    k_smallest_elements = []
    while heap:
        item = heappop(heap)
        k_smallest_elements.append(abs(item))

    return k_smallest_elements



def kth_smallest(arr, k):
    heap = []

    for i in range(k):
        heappush(heap, -1*arr[i])

    for i in range(k, len(arr)):
        heappush(heap, -1*arr[i])
        heappop(heap)

    return heappop(heap) * -1

