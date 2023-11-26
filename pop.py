from math import comb, factorial
MOD = 10**9 + 7
def count_enchanting_paths(N):
    if N == 1:
        return 2
    elif N == 2:
        return 3
    def nCr(n, r):
        return factorial(n) // (factorial(r) * factorial(n - r))
    totalpaths = 0
    for i in range(N // 2 + 1, N + 1):
        gold = nCr(N, i)
        silver = nCr(i + min(i - 1, N - i), i)
        totalpaths += (gold * silver) % MOD
    return totalpaths % MOD
N = int(input().strip())
result = count_enchanting_paths(N)
print(result)