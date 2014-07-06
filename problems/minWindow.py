def minWindow(S, T):
	if len(S) < len(T):
		return ""
	elif S == T:
		return T

	visited = {}
	T= set(T)
	min_window = 0
	res = float('inf')
	start,end = 0,0
	k = 0	
	for i in xrange(len(S)):
		if S[i] in T:
			visited[S[i]] = i
			if len(visited) == len(T):
				start = min(visited.values())
				end = max(visited.values())
				min_window = end - start
				print end,start,visited
				if min_window < res:
					res = min_window
					k = start
	print k,res
	return S[k:k+res+1] if res != float('inf') else ""


if __name__ == '__main__':
	# S = "ADOBECODEBANC"
	# T = "ABC"
	S = "aa"
	T = "aa"
	print minWindow(S,T)


