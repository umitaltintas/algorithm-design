
def DivConqPower(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:
        return DivConqPower(a, n/2) * DivConqPower(a, n/2)
    else:
        return DivConqPower(a, n//2) * DivConqPower(a, n//2) * a
    
print(DivConqPower(3, 5))


def BrutForcePower(a, n):
    if n == 1:
        return a
    else:
        return a * BrutForcePower(a, n-1)
print(BrutForcePower(3, 5))