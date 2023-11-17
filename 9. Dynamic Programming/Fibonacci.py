def fib1(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)
    
def fib2(n: int) -> int:
    if n == 0:
        return 0
    table = [0] * (n + 1)
    table[1] = 1
    for i in range (2, n+1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


if __name__ == '__main__':
    print(f'{fib2(8) = }')
    print(f'{fib2(42) = }')
    print(f'{[fib2(i) for i in range (10)] = }')