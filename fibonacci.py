def fib(n, memo={}):
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

def fib2(n):
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)

def main():
    print(fib(35))
    print(fib2(35))

main()
