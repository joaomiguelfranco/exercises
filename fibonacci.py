
def fibonacciIteration(n):
    accumulator = {0:1, 1:1}
    for i in range(2, n+1):
        if i in accumulator: return accumulator[i]
        accumulator[i] = accumulator[i-1] + accumulator[i-2]
    return accumulator[n]


def fibonacciRecursion(n):
    if n <= 1 : return 1
    return fibonacciRecursion(n-1) + fibonacciRecursion(n-2)

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        n_2 = 1
        n_1 = 2 
        for i in range(3,n+1):
            r = n_1 + n_2
            n_2 = n_1
            n_1 = r
        return r

if __name__ == '__main__':
    assert fibonacciRecursion(3) == 3
    assert fib(5) == 8

    assert fib(29) == 832040
    # fibonacciRecursion(980) # this takes too much time using recursion
    assert fib(980) == 4649326900163660310919854588034777960785795767174042210878678322288756043258320098018630118437425368286091440984485413634511629642042032827880286278313342328421326891037271717682651493171103066962116698306
    fib(1500000)
