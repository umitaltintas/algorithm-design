def cut_candy(arr):
    size = len(arr)
    memo = [0 for x in range(size+1)]
    memo[0] = 0

    for i in range(1, size+1):
        max_profit = -float('inf')
        for j in range(i):
             max_profit = max(max_profit, arr[j] + memo[i-j-1])
        memo[i] = max_profit
    print(memo)
    return memo[size]




prices = [1, 5, 8, 9, 10, 17, 17, 20]

print( cut_candy(prices))



