def count_reversed(numbers):
    mid = len(numbers) // 2
    if len(numbers) <= 1:
        return 0
    left = numbers[:mid]
    right = numbers[mid:]
    left_count = count_reversed(left)
    right_count = count_reversed(right)
    count = merge(left, right, numbers)
    return count+left_count+right_count


def merge(left, right, numbers):
    i = j = k = count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i = i+1
        else:
            numbers[k] = right[j]
            j = j+1
            count = count+len(left) - i
        k = k+1

    while i < len(left):
        numbers[k] = left[i]
        i = i+1
        k = k+1
    while j < len(right):
        numbers[k] = right[j]
        j = j+1
        k = k+1

    return count

arr = [1, 20, 6, 4, 5]
print(count_reversed(arr))