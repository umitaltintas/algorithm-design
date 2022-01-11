def polynomial(x,a_list):
    ans = 0
    for n in range(len(a_list)):
        ans += a_list[n]*(x**n)
    return ans

print(polynomial(3,[1, 1, 1, 0, 1] ))