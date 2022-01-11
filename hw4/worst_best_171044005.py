
def max_min(numbers):
    if len(numbers) == 1:
        return numbers[0], numbers[0]
    elif len(numbers) == 2:
        return max(numbers[0], numbers[1]), min(numbers[0], numbers[1])
    else:
        mid = int(len(numbers)/2)
        (max1, min1) = max_min(numbers[:mid])
        (max2, min2) = max_min(numbers[mid:])
        return max(max1, max2), min(min1, min2)


# array of number between 0 and 1 disordered
numbers = [0.4, 0.7, 0.9, 0.2, 0.5, 0.1, 0.3]

print(max_min(numbers))

