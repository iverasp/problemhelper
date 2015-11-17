import sys

sys.setrecursionlimit(100000)

memo = {}
def fib(n):
    if n in memo: return memo[n]
    
    if n == 1: return 1
    if n == 2: return 2
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]

print fib(9000)
