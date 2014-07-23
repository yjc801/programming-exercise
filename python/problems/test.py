A = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]

n = len(A)
m = len(A[0])

print A
print m,n



x = -5
counter = 0
x = abs(x)
while x:
    x = x>>1
    counter+=1

print counter

A = [1,2]
n = len(A)
# A[A[0]],A[0] = A[0],A[A[0]]
for i in xrange(n):
    while A[i] != i:
        if A[i] >= n:
            break
        A[A[i]],A[i] = A[i],A[A[i]]
print A
for i in xrange(1,n):
	if A[i]!=i:
		print i
print n

def heapsort(lst):
  ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''
 
  # in pseudo-code, heapify only called once, so inline it here
  for start in range((len(lst)-1)/2, -1, -1):
    siftdown(lst, start, len(lst)-1)
 
  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  return lst
 
def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    
    if child > end:
        break
    
    if child + 1 <= end:
        child = max(child,child+1,key = lambda x:lst[x])

    if lst[root] < lst[child]:
        lst[root], lst[child] = lst[child], lst[root]
        root = child
    else:
        break

print heapsort([1,2,1,4,8,3])


def max_sub(A):
    temp = 0
    res = -float('inf')
    # n = len(A)
    # res = [0]*n
    # start = [0]*n
    for key, value in enumerate(A):
        temp = max(value,temp+value)
        if temp > res:
            res = temp
        # if res[key-1]+value > value:
            # res[key] = res[key-1]+value
            # start[key] = start[key-1]
        # else:
            # res[key] = value
            # start[key] = key
    return res


A = [4,-1,-2,1,-1,4,2,-5]
print max_sub(A)

from functools import wraps

def memo(func):
    cache={}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args]=func(*args)
        return cache[args]
    return wrap


cache = {}
def dp(A,i):
    if i in cache:
        return cache[i]
    if i == 0:
        cache[i] = A[0]
    else:
        cache[i] = max(dp(A,i-1)+A[i],A[i])
    return cache[i]

A = [-4]
print dp(A,len(A)-1)
print max(cache.values())