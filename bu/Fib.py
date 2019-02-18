def fib (n,k):
    fib = []
    for i in range(int(0), n):
        if i < 2:
            fib.append(1)
        else:
            fib.append(fib[i-2]*k + fib[i-1])

    return fib[-1]

with open('fib', 'r') as f:
    n, k = f.readline().split()
    print fib(int(n), int(k))