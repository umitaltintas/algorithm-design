def schedule(intervals):
    result = []
    while intervals:
        f = 0
        for i in range(len(intervals)):
            if intervals[i][1] < intervals[f][1]:
                f = i
        current = intervals.pop(f)
        result.append(current)

        finish = current[1]
        compatibles = []
        for i in range(len(intervals)):
            if intervals[i][0] >= finish:
                compatibles.append(intervals[i])

        intervals = compatibles.copy()
        print(intervals)
    return result


intervals = [
    [1, 2],
    [3, 4],
    [0, 3],
    [5, 7],
    [8, 9],
    [5, 9]
]
res = schedule(intervals)
print(len(res))
