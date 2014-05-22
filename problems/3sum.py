def threeSum(num):
    if len(num) < 3:
        return []
    n = len(num)
    num = sorted(num)
    res = []

    for key,value in enumerate(num):
        if value > 0:
            continue
        if key + 2 < n - 1 and value == num[key+2]:
            if value == 0:
                res.append(tuple([0,0,0]))
            continue
        next_index = key + 1
        last_index = n - 1
        print key,next_index, last_index
        while next_index < last_index:
            if value + num[next_index] + num[last_index] < 0:
                next_index += 1
            elif value + num[next_index] + num[last_index] > 0:
                last_index -= 1
            else:
                temp = sorted([value,num[next_index],num[last_index]])
                res.append(tuple(temp))
                next_index += 1
                last_index -= 1
    return list(set(res))

if __name__ == '__main__':
    # A = [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
    # print sorted(A)
    A = [-1,-1,-1,0,0,0,0,0,0,1,2,3]
    print threeSum(A)