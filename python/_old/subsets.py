def subsets(S):
    if not S:
        return []
    S = list(set(S))
    result = []
    n = len(S)
    comb = pow(2,n)
    for i in S:
        temp = []
        for j in xrange(0,i):
            if get_bit(i,j):
                temp.append(S[j])
        result.append(temp)
    return result

def get_bit(num,bit):
    num &= 1<<bit
    return 1 if num else 0


if __name__ == '__main__':
    # A = [5,4,5,4,3,3,1,1,1,2]
    A = [1,2,2]
    print subsets(A)