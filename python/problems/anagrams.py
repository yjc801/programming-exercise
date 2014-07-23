import collections

def anagrams(strs):

	res = []
	cnt = collections.defaultdict(list)
	for string in strs:
		cnt[(''.join(sorted(string)))].append(string)

	for word, group in cnt.items():
		if len(group) > 1:
			res.extend(group)
	return res

if __name__ == '__main__':
	print anagrams(["",""])