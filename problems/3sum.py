import collections

def threeSum(num):
    n, num, res= len(num), sorted(num), []

    for key,value in enumerate(num):
        # if value > 0:
        #     continue
        # if key + 2 < n - 1 and value == num[key+2]:
        #     if value == 0:
        #         res.append(tuple([0,0,0]))
        #     continue
        next_index, last_index = key + 1, n - 1

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
    # print res
    return list(set(res))

def threeSum2(num):
    num, res, i = sorted(num), [], 0
    while i < len(num) - 2:
        j, k = i + 1, len(num) - 1
        while j < k:
            if num[i] + num[j] + num[k] < 0:
                j += 1
            elif num[i] + num[j] + num[k] > 0:
                k -= 1
            else:
                res.append([num[i], num[j], num[k]])
                j, k = j + 1, k - 1
                while j < k and num[j] == num[j - 1]:
                    j += 1
                while j < k and num[k] == num[k + 1]:
                    k -= 1
        i += 1
        while i < len(num) - 2 and num[i] == num[i - 1]:
            i += 1
    return res

if __name__ == '__main__':
    # num = [7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
    # print sorted(num)
    num = [-1,-1,-1,0,0,0,0,0,0,1,2,3]
    print threeSum2(num) 
    print threeSum(num)