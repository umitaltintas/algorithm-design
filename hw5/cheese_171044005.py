
def max_weight_price_comb(max_weight, weights, prices):
    size = len(weights)
    memo = [[0 for x in range(max_weight + 1)] for x in range(size + 1)]

    for i in range(size + 1):
        for weight in range(max_weight + 1):
            if i == 0 or weight == 0:
                memo[i][weight] = 0
            elif weights[i-1] <= weight:
                memo[i][weight] = max(prices[i-1]
                              + memo[i-1][weight-weights[i-1]],
                              memo[i-1][weight])                
            else:
                memo[i][weight] = memo[i-1][weight]

    return memo[size][max_weight]


prices = [60, 100, 120]
weights = [10, 20, 30]
max_weight = 50

print(max_weight_price_comb(max_weight, weights, prices))
