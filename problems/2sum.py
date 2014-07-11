import collections

def twoSum(numbers, target):
	sorted_nums = sorted(numbers)
	S = set(numbers)
	number2 = None
	while number2 not in S:
		number1 = sorted_nums.pop()
		number2 = target - number1
	index1 = numbers.index(number1)
	numbers[index1] = None
	index2 = numbers.index(number2)
	return min(index1+1,index2+1),max(index1+1,index2+1)


def twoSum2(numbers, target):
    dictionary = collections.defaultdict(list)
    for index, value in enumerate(numbers):
        dictionary[value].append(index+1)
    
    for index, value in enumerate(numbers):
        search = target - value
        if dictionary.has_key(search):
        	item = dictionary[search]
        	size = len(item)
        	if search != value:
        	    return (index+1,item[0])
        	if size > 1:
        	    return (item[0],item[1])

def twoSum3(num, target):
    map = {}
    res = []
    for key, value in enumerate(num):
        map[value] = key
        
    for i in xrange(len(num)):
        gap = target - num[i]
        if map.get(gap):
            res.append([i+1,map[gap]+1])
            
            # res = [i+1,map[gap]+1]
            # break
    return tuple(res)


if __name__ == '__main__':
	A = [1,3,2]
	# print twoSum(A,4)
	print twoSum2(A,4)
	print twoSum3(A,4)