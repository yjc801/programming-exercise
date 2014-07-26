def nextPermutation(num):
    if not num:
        return num
        
    last = len(num)-1
    pivot = last - 1
    while pivot >= 0 and num[pivot] >= num[pivot+1]:
        pivot-=1
    
    if pivot < 0:
        num.reverse()
        return num
    
    while num[last] <= num[pivot]:
        last-=1
    
    num[last],num[pivot] = num[pivot],num[last]
    
    num[pivot+1:] = reversed(num[pivot+1:])
    
    return num

if __name__ == '__main__':
    A = [1,3,2]
    print nextPermutation(A)