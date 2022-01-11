

def sort_pairs(boxes, gifts):
    l = len(boxes)-1
    quickSort(boxes, gifts, 0, l)


def partition(arr, low, high, pivot):
    i = low
    j = low
    while j < high:
        if (arr[j] < pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif (arr[j] == pivot):
            arr[j], arr[high] = arr[high], arr[j]
            j -= 1
        j += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i



def quickSort(arr, arr2, low, high):
    if low < high:
        pi = partition(arr, low,high, arr2[high])
        partition(arr2,low,high, arr[pi])
        quickSort(arr, arr2, low, pi-1)
        quickSort(arr, arr2, pi+1, high)


a = [1, 3, 4, 5 ,6 ,7 ,8, 2]
b = [8, 3, 5 ,7, 4 ,6 ,1 ,2]

sort_pairs(a, b)
print(a, b)
