def f(n: int) -> int:
    r = 0
    for i in range(n):
        r ^= n
    return r

if __name__ == '__main__':
    print(f(20))