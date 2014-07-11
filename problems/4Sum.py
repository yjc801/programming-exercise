import collections

def fourSum(num, target):
    num = sorted(num)
    i,n,res = 0,len(num),[]
    
    cache = collections.defaultdict(list)

    while i < n:
        j = i+1
        while j < n:
            cache[num[i]+num[j]].append((i,j))
            j+=1
            while j < n and num[j] == num[j-1]:
                j+=1
        i+=1
        while i < n and num[i]==num[i-1]:
            i+=1

    return res

if __name__ == '__main__':
    A = [1,0,-1,0,-2,2,0,0]
    target = 0
    print fourSum(A,target)