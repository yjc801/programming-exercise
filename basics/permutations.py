def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    print indices
    print cycles
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                print indices
                break
        else:
            return


def generate(array, r, res, n):
    if r == n:
        temp = ''.join(array[:r])
        if temp not in res:
            res+=[temp]
        return res

    for i in xrange(r,len(array)):
        array[r], array[i] = array[i], array[r]
        generate(array,r+1, res, n)
        array[r], array[i] = array[i], array[r]


if __name__ == '__main__':
    # print permutations('ABCD')
    a = '1234'
    res = []
    print generate(list(a),0,res, 2)
    print res